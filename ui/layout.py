import flet as ft

class BangerWaveLayout:
    """Master Viewport Panel Framework for BangerWave."""
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "BangerWave Stream Client"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.bgcolor = ft.Colors.BLACK

    def _build_sidebar(self) -> ft.Container:
        """Returns a fixed left panel container for main navigation."""
        return ft.Container(
            width=230,
            bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
            padding=15,
            border_radius=8
        )

    def _build_viewport(self) -> ft.Container:
        """Returns an expanding fluid panel container for track view displays."""
        return ft.Container(
            expand=True,
            bgcolor=ft.Colors.BLACK,
            padding=15
        )

    def _build_player_bar(self) -> ft.Container:
        """Returns a fixed bottom console container block for track timeline controls."""
        left_zone = ft.Container(
            content=ft.Column([
                ft.Text("No Track Selected", weight=ft.FontWeight.BOLD, size=14),
                ft.Text("Unknown Artist", size=11, color=ft.Colors.GREY_400)
            ]),
            width=200
        )

        center_zone = ft.Column(
            controls=[
                ft.Row([
                    ft.IconButton(icon=ft.Icons.SHUFFLE_ROUNDED, icon_size=18),
                    ft.IconButton(icon=ft.Icons.PLAY_CIRCLE_FILLED_ROUNDED, icon_size=36, icon_color=ft.Colors.GREEN_ACCENT_400),
                    ft.IconButton(icon=ft.Icons.REPEAT_ROUNDED, icon_size=18),
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.Text("0:00", size=11),
                    ft.Slider(expand=True, active_color=ft.Colors.GREEN_ACCENT_400),
                    ft.Text("0:00", size=11)
                ])
            ],
            expand=True
        )

        right_zone = ft.Container(
            content=ft.Row([
                ft.Icon(ft.Icons.VOLUME_UP_ROUNDED, size=18),
                ft.Slider(width=100, value=80)
            ]),
            width=200
        )

        return ft.Container(
            content=ft.Row([left_zone, center_zone, right_zone], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            height=90,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGH,
            padding=15,
            border_radius=12
        )

    def assemble(self) -> None:
        """Assembles and renders the structural panel arrays directly into the page."""
        self.page.clean()
        
        main_workspace = ft.Row(
            controls=[self._build_sidebar(), self._build_viewport()],
            expand=True
        )
        
        self.page.add(
            ft.Column(
                controls=[main_workspace, self._build_player_bar()],
                expand=True
            )
        )
