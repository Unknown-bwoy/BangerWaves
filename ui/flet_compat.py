from types import SimpleNamespace

from flet.controls.colors import Colors
from flet.controls.core.column import Column
from flet.controls.core.icon import Icon
from flet.controls.core.list_view import ListView
from flet.controls.core.row import Row
from flet.controls.core.text import Text
from flet.controls.material.container import Container
from flet.controls.material.divider import Divider
from flet.controls.material.elevated_button import ElevatedButton
from flet.controls.material.icon_button import IconButton
from flet.controls.material.icons import Icons
from flet.controls.material.progress_ring import ProgressRing
from flet.controls.material.slider import Slider
from flet.controls.material.textfield import TextField
from flet.controls.page import Page
from flet.controls.types import FontWeight, MainAxisAlignment, ThemeMode


ft = SimpleNamespace(
    Colors=Colors,
    Column=Column,
    Container=Container,
    Divider=Divider,
    ElevatedButton=ElevatedButton,
    FontWeight=FontWeight,
    Icon=Icon,
    IconButton=IconButton,
    Icons=Icons,
    ListView=ListView,
    MainAxisAlignment=MainAxisAlignment,
    Page=Page,
    ProgressRing=ProgressRing,
    Row=Row,
    Slider=Slider,
    Text=Text,
    TextField=TextField,
    ThemeMode=ThemeMode,
)
