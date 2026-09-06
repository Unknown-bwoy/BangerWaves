from typing import Dict,Any,List,Callable, Optional
class Appstate: 
    def subscribe(self,call_back_function): 
        self._listeners.append(call_back_function) 

    def notify(self): 
        for callback in self._listeners: 
            callback()  

    def __init__(self): 
        self.current_track: Optional[Dict[str,Any]] = None 
        self.is_playing: bool = False 
        self._listeners: List[Callable] = []  

    def update_track(self,track_data): 
        self.current_track = track_data 
        self.is_playing = True 


    def set_playing_state(state: Appstate, is_playing: bool) -> None:
        state.is_playing = is_playing
        state.notify() 

    def update_volume(self, incoming_volume): 
        self.volume = max(0.0,min(1.0, incoming_volume))  


    