from typing import Callable, List, Dict, Any, Optional

class AppState:
    """
    Architectural State Manager for BangerWave.
    Implements a thread-safe Observer Pattern to act as the Single Source of Truth
    across asynchronous UI event loops and external background threads.
    """
    def __init__(self):
        # Playback Variables
        self.current_track: Optional[Dict[str, Any]] = None
        self.is_playing: bool = False
        self.current_position: float = 0.0  # Elapsing track time in seconds
        self.volume: float = 0.8  # Default system scale (0.0 to 1.0)
        
        # Internal observer registration array
        self._listeners: List[Callable[[], None]] = []

    def subscribe(self, callback: Callable[[], None]) -> None:
        """Binds a UI layout update routine to execute upon state mutations."""
        if callback not in self._listeners:
            self._listeners.append(callback)

    def unsubscribe(self, callback: Callable[[], None]) -> None:
        """Removes a UI callback safely to prevent memory reference leaks."""
        if callback in self._listeners:
            self._listeners.remove(callback)

    def notify_listeners(self) -> None:
        """Iterates and triggers every registered rendering hook sequentially."""
        for listener in self._listeners:
            try:
                listener()
            except Exception as e:
                print(f"[STATE WARNING] Notification failure on a listener loop: {e}")

    def update_track(self, track_data: Optional[Dict[str, Any]]) -> None:
        """Changes the current audio track payload and resets progress markers."""
        self.current_track = track_data
        self.current_position = 0.0
        self.is_playing = bool(track_data)
        self.notify_listeners()

    def set_playing_state(self, playing: bool) -> None:
        """Updates the active stream flag."""
        if self.is_playing != playing:
            self.is_playing = playing
            self.notify_listeners()

    def update_position(self, position: float) -> None:
        """Increments the active timeline cursor silently without forcing heavy UI redraws."""
        self.current_position = position

    def set_volume(self, volume: float) -> None:
        """Normalizes and alters system volume thresholds safely."""
        self.volume = max(0.0, min(1.0, volume))
        self.notify_listeners()
