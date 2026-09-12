import flet as ft

# Building a track container block card
track_result_card = ft.Container(
    content=ft.Row([
        # Left side design icon
        ft.Icon(ft.Icons.MUSIC_NOTE_ROUNDED, color=ft.Colors.GREEN_ACCENT_400),
        
        # Center metadata column
        ft.Column([
            ft.Text("Track Title Name", weight=ft.FontWeight.BOLD),
            ft.Text("3:45", size=11, color=ft.Colors.GREY_400)
        ], expand=True),
        
        # Right action execution button
        ft.IconButton(
            icon=ft.Icons.PLAY_ARROW_ROUNDED,
            on_click=lambda e: print("Play button clicked!")
        )
    ]),
    bgcolor=ft.Colors.SURFACE_CONTAINER,
    padding=12,
    border_radius=8
)

#TO DO Fix the errors and continue from where i i did not finnish