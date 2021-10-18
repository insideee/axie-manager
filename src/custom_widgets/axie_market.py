from PySide2.QtGui import QPaintEvent, QPainter, QColor, QPen, QFont
from PySide2.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PySide2.QtCore import QRect, Qt, QSize

class HomeMarketFeature(QWidget):
    def __init__(self, width, height, font_size=12, font_family='Segoi') -> None:
        super(HomeMarketFeature, self).__init__()

        #custom properties
        self.width = width
        self.height = height
        self.text_color = 0xE64C3C
        self.reference_color = 0x737373
        self.font_size = font_size
        self.font_family = font_family


        self.setMinimumSize(QSize(self.width, self.height))
        self.setMaximumSize(QSize(self.width, self.height))

    def paintEvent(self, event: QPaintEvent) -> None:
        paint = QPainter()
        paint.begin(self)
        paint.setFont(QFont(self.font_family, self.font_size))

        pen = QPen()

        # draw rect
        pen.setColor(self.reference_color)
        pen.setWidth(5)
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(pen)
        paint.drawRect(rect)


        # draw text
        pen.setColor(self.text_color)
        paint.setPen(pen)
        paint.drawText(rect, Qt.AlignCenter, 'Home Market Feature')

        paint.end()
        


