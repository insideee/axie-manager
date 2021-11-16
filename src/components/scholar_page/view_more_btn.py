from PySide6.QtCore import QEvent, QSize, Qt
from PySide6.QtGui import QEnterEvent, QPixmap
from PySide6.QtWidgets import QToolButton


class MoreMenuBtn(QToolButton):
    """Custom button for the view more menu.
    """

    def __init__(self, parent, default_image: QPixmap, painted_image: QPixmap):
        super().__init__(parent=parent)

        # properties
        self.default_image = default_image
        self.painted_image = painted_image

        # config
        self.setObjectName('view_more_menu')
        self.setCursor(Qt.PointingHandCursor)
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.setStyleSheet('background-color: none;\
                            border: none')
        self.setIcon(self.default_image)
        self.setIconSize(QSize(25, 25))

    def enterEvent(self, arg__1: QEnterEvent) -> None:
        self.setIcon(self.painted_image)

        return super().enterEvent(arg__1)

    def leaveEvent(self, arg__1: QEvent) -> None:
        self.setIcon(self.default_image)

        return super().leaveEvent(arg__1)