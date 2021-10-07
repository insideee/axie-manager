from PySide2.QtGui import QPaintEvent, QPainter, QColor, QPen, QFont
from PySide2.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PySide2.QtCore import QRect, Qt, QSize
from custom_widgets.ui import Ui_main

class AddPopUp(QWidget):
    def __init__(self, width=200, height=200) -> None:
        super(AddPopUp, self).__init__()
        self.ui = Ui_main()
        self.ui.setupUi(self)

        #custom properties
        self.shadow_blur_radius = 5

        # shadow
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(self.shadow_blur_radius)
        self.shadow.setOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 90))
        self.ui.bg.setGraphicsEffect(self.shadow)


        self.setMinimumSize(QSize(self.width, self.height))
        self.setMaximumSize(QSize(self.width, self.height))
