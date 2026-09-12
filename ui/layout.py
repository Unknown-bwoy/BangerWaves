from typing import Any

if __package__:
    from .flet_compat import ft
    from .search_view import BangerWaveSearchView
else:
    from flet_compat import ft
    from search_view import BangerWaveSearchView


class BangerWaveLayout:
    """Master Viewport Panel Framework for BangerWave using clean top-level imports."""

    def __init__(
        self,
        page: Any,
        state: Any,
        worker: Any,
    ):
        self.page = page
        self.state = state
        self.worker = worker
        
        self.page.title = "BangerWave Stream Client"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.bgcolor = ft.Colors.BLACK

    def _build_sidebar(self) -> Any:
        """Returns a fixed left panel container for main navigation."""
        return ft.Container(
            content=ft.Column([
                ft.Text("BangerWave", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_ACCENT_400),
                ft.Divider(),
                ft.Row([ft.Icon(ft.Icons.SEARCH_ROUNDED), ft.Text("Search Dashboard")]),
                ft.Row([ft.Icon(ft.Icons.LIBRARY_MUSIC_ROUNDED), ft.Text("Your Playlists")])
            ], spacing=15),
            width=230,
            bgcolor=ft.Colors.SURFACE_CONTAINER_LOW,
            padding=15,
            border_radius=8,
        )

    def _build_viewport(self) -> Any:
        """Returns an expanding fluid panel container embedding the active search display."""
        # Instantiate your search view panel using Dependency Injection
        search_panel = BangerWaveSearchView(self.page, self.state, self.worker)
        
        return ft.Container(
            content=search_panel.build(), # Inject the compiled column layout
            expand=True,
            bgcolor=ft.Colors.BLACK,
            padding=15,
        )

    def _build_player_bar(self) -> Any:
        """Returns a fixed bottom console container block for track timeline controls."""
        left_zone = ft.Container(
            content=ft.Column([
                ft.Text(value="No Track Selected", weight=ft.FontWeight.BOLD, size=14),
                ft.Text(value="Unknown Artist", size=11, color=ft.Colors.GREY_400),
            ]),
            width=200,
        )

        center_zone = ft.Column([
            ft.Row([
                ft.IconButton(icon=ft.Icons.SHUFFLE_ROUNDED, icon_size=18),
                ft.IconButton(icon=ft.Icons.PLAY_CIRCLE_FILLED_ROUNDED, icon_size=36, icon_color=ft.Colors.BLUE_ACCENT_400),
                ft.IconButton(icon=ft.Icons.REPEAT_ROUNDED, icon_size=18),
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                ft.Text(value="0:00", size=11),
                ft.Slider(expand=True, min=0, max=100, value=0, active_color=ft.Colors.BLUE_ACCENT_400),
                ft.Text(value="0:00", size=11),
            ])
        ], expand=True)

        right_zone = ft.Container(
            content=ft.Row([
                ft.Icon(ft.Icons.VOLUME_UP_ROUNDED, size=18),
                ft.Slider(width=100, min=0, max=100, value=80),
            ]),
            width=200,
        )

        return ft.Container(
            content=ft.Row([
                left_zone,
                center_zone,
                right_zone,
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            height=90,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGH,
            padding=15,
            border_radius=12,
        )

    def assemble(self) -> None:
        """Assembles and renders the structural panel arrays directly into the page."""
        self.page.clean()

        main_workspace = ft.Row([
            self._build_sidebar(),
            self._build_viewport(),
        ], expand=True)

        self.page.add(
            ft.Column([
                main_workspace,
                self._build_player_bar(),
            ], expand=True)
        )
