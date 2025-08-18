from pathlib import Path

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFormLayout

from quincE import ItemWidget, TextDescription
from quincE.custom_widgets import SpinBox

NAME = "Simultaneous"
ICON = QIcon(str(Path(__file__).parent.joinpath("arrow-in.png")))


class SimultaneousWidget(ItemWidget):
    """Run the nested items at the same time; widget."""

    def __init__(self):
        ItemWidget.__init__(
            self,
            None,
            NAME,
            ICON,
            TextDescription(
                NAME,
                "Run the nested items at the same time "
                "(in reality, the sequence rapidly switches between them).",
                {},
            ),
        )
