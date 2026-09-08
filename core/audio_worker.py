import asyncio
import concurrent.futures
from typing import Any, Dict, Optional, cast

import yt_dlp


class AudioWorker:
	def __init__(self, max_workers: int = 2):
		self.executor = concurrent.futures.ThreadPoolExecutor(
			max_workers=max_workers
		)
		self.ydl_opts: Any = {
			"format": "bestaudio/best",
			"noplaylist": True,
			"quiet": True,
			"skip_download": True,
			"extract_flat": False,
		}

	def _extract(self, query: str) -> Optional[Dict[str, Any]]:
		"""Synchronously extract audio information using yt_dlp."""
		search_target = f"ytsearch1:{query}"

		with yt_dlp.YoutubeDL(cast(Any, self.ydl_opts)) as ydl:
			info = ydl.extract_info(search_target, download=False)

			if info and "entries" in info:
				target_entry = next(iter(info["entries"]), None)
				if target_entry is None:
					return None
				duration = target_entry.get("duration")
				return { 
					"id": target_entry.get("id"),
					"title": target_entry.get("title", "Unknown Track"),
					"duration": float(duration) if duration is not None else 0.0,
					"url": target_entry.get("url"),
					"query": query,
				}
		return None

	async def resolve_stream(self, query: str) -> Optional[Dict[str, Any]]:
		"""Delegate blocking extraction to the background thread pool."""
		current_loop = asyncio.get_running_loop()
		return await current_loop.run_in_executor(
			self.executor, self._extract, query
		)

	def shutdown(self) -> None:
		"""Shut down the executor and free its worker threads."""
		self.executor.shutdown(wait=True)
