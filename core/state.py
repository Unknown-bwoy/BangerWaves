from typing import Any, Callable, Dict, List, Optional


class Appstate:
    def __init__(self):
        self.current_track: Optional[Dict[str, Any]] = None
        self.is_playing: bool = False
        self.volume: float = 0.8
        self._listeners: List[Callable[[], None]] = []

    def subscribe(self, call_back_function: Callable[[], None]) -> None:
        if call_back_function not in self._listeners:
            self._listeners.append(call_back_function)

    def notify(self) -> None:
        for callback in list(self._listeners):
            callback()

    def update_track(self, track_data: Optional[Dict[str, Any]]) -> None:
        self.current_track = track_data
        self.is_playing = track_data is not None
        self.notify()

    def set_playing_state(self, is_playing: bool) -> None:
        self.is_playing = is_playing
        self.notify()

    @staticmethod
    def set_playing_state_static(state: "Appstate", is_playing: bool) -> None:
        state.set_playing_state(is_playing)

    def update_volume(self, incoming_volume: float) -> None:
        self.volume = max(0.0, min(1.0, incoming_volume))
        self.notify()

    