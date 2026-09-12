from flet.controls.colors import Colors
from flet.controls.core.column import Column
from flet.controls.core.icon import Icon
from flet.controls.core.row import Row
from flet.controls.core.text import Text
from flet.controls.material.container import Container
from flet.controls.material.icon_button import IconButton
from flet.controls.material.icons import Icons
from flet.controls.material.slider import Slider
from flet.controls.page import Page
from flet.controls.types import FontWeight, MainAxisAlignment, ThemeMode


class BangerWaveLayout:
    """Master Viewport Panel Framework for BangerWave."""

    def __init__(self, page: Page):
        self.page = page
        self.page.title = "BangerWave Stream Client"
        self.page.theme_mode = ThemeMode.DARK
        self.page.bgcolor = Colors.BLACK

    def _build_sidebar(self) -> Container:
        """Returns a fixed left panel container for main navigation."""
        return Container(
            width=230,
            bgcolor=Colors.SURFACE_CONTAINER_LOW,
            padding=15,
            border_radius=8,
        )

    def _build_viewport(self) -> Container:
        """Returns an expanding fluid panel container for track view displays."""
        return Container(
            expand=True,
            bgcolor=Colors.BLACK,
            padding=15,
        )

    def _build_player_bar(self) -> Container:
        """Returns a fixed bottom console container block for track timeline controls."""
        left_zone = Container(
            content=Column([
                Text(value="No Track Selected", weight=FontWeight.BOLD, size=14),
                Text(value="Unknown Artist", size=11, color=Colors.GREY_400),
            ]),
            width=200,
        )

        center_zone = Column([
            Row([
                IconButton(icon=Icons.SHUFFLE_ROUNDED, icon_size=18),
                IconButton(icon=Icons.PLAY_CIRCLE_FILLED_ROUNDED, icon_size=36),
                IconButton(icon=Icons.REPEAT_ROUNDED, icon_size=18),
            ], alignment=MainAxisAlignment.CENTER),
            Row([
                Text(value="0:00", size=11),
                Slider(expand=True, active_color=Colors.GREEN_ACCENT_400),
                Text(value="0:00", size=11),
            ])
        ], expand=True)

        right_zone = Container(
            content=Row([
                Icon(Icons.VOLUME_UP_ROUNDED, size=18),
                Slider(width=100,min=0,max=100,value=80),
            ]),
            width=200,
        )

        return Container(
            content=Row([
                left_zone,
                center_zone,
                right_zone,
            ], alignment=MainAxisAlignment.SPACE_BETWEEN),
            height=90,
            bgcolor=Colors.SURFACE_CONTAINER_HIGH,
            padding=15,
            border_radius=12,
        )

    def assemble(self) -> None:
        """Assembles and renders the structural panel arrays directly into the page."""
        self.page.clean()

        main_workspace = Row([
            self._build_sidebar(),
            self._build_viewport(),
        ], expand=True)

        self.page.add(
            Column([
                main_workspace,
                self._build_player_bar(),
            ], expand=True)
        )
