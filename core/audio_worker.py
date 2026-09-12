import asyncio
import concurrent.futures
from typing import Any, Dict, Iterable, Optional, cast
import yt_dlp

class AudioWorker:
    """
    Thread-Isolated Network Extraction Engine for BangerWave.
    Wraps synchronous yt_dlp scraping targets inside a persistent ThreadPoolExecutor
    to protect the asynchronous Flet UI main loop from blocking during network I/O.
    """
    def __init__(self, max_workers: int = 2):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)
        
        self.ydl_opts = {
            'format': 'bestaudio/best',      # Targets optimal direct compression audio formats
            'noplaylist': True,               # Restricts processing to single isolated nodes
            'quiet': True,                    # Strips standard out stdout logging overhead
            'skip_download': True,            # Intercepts links only; stops hard drive downloads
            'extract_flat': False,            # Deep resolves streaming tokens explicitly
        }

    def _extract(self, query: str) -> Optional[Dict[str, Any]]:
        """Synchronous core executed exclusively within the background worker thread."""
        search_target = f"ytsearch1:{query}"
        
        with yt_dlp.YoutubeDL(cast(Any, self.ydl_opts)) as ydl:
            info = ydl.extract_info(search_target, download=False)
            
            if info:
                entries = cast(
                    Iterable[Dict[str, Any]],
                    info.get("entries") or [],
                )
                
                target_entry = next(iter(entries), None)
                if target_entry is not None:
                    return {
                        "id": target_entry.get('id'),
                        "title": target_entry.get('title', 'Unknown Track'),
                        "duration": float(target_entry.get('duration', 0.0)),
                        "url": target_entry.get('url'),  # Raw unexpired HTTP CDN streaming link
                        "query": query                     
                    }
            return None

    async def resolve_stream(self, query: str) -> Optional[Dict[str, Any]]:
        """Asynchronously delegates blocking yt-dlp extraction to a thread pool worker."""
        if not query.strip():
            return None

        loop = asyncio.get_running_loop()
        try:
            return await loop.run_in_executor(self.executor, self._extract, query)
        except Exception as e:
            print(f"[ENGINE EXCEPTION] Link resolution failed for query '{query}': {e}")
            return None

    def shutdown(self) -> None:
        """Halts the execution pipeline and terminates background workers cleanly."""
        self.executor.shutdown(wait=True)
