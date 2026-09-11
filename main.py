import flet as ft
from core.state import Appstate
from core.audio_worker import AudioWorker
from database.manager import BangerWaveDatabase
from ui.layout import BangerWaveLayout

def main(page: ft.Page):
    # 1. Initialize your core system layers inside runtime memory
    state = Appstate()
    worker = AudioWorker()
    db = BangerWaveDatabase()

    # 2. Instantiate and assemble your visual multi-pane window framework
    layout = BangerWaveLayout(page)
    layout.assemble()

    # 3. Defensive Cleanup: Intercept window closing events to kill background threads safely
    def handle_window_event(e):
        if e.data == "close":
            print("[SYSTEM TEARDOWN] Cleaning up engine worker threads...")
            worker.shutdown()
            page.window_destroy()

    page.on_window_event = handle_window_event

# Launch the full cross-platform application interface instance
if __name__ == "__main__":
    ft.app(target=main)
