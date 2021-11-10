from PySide6.QtWidgets import QApplication, QGraphicsEffect, QFrame
from PySide6.QtCore import QSize, QRect, Qt
from PySide6.QtGui import QPainter, QPen, QColor, QLinearGradient, QGradient, QBrush, QFont


class DailyGoalWidget(QFrame):
    
    def __init__(self, width):
        super().__init__()
        self.setObjectName('daily_widget')

        # properties
        self.c_width = width
        self.progress_width = 49
        self.value = 72
        self.font_family = 'Montserrat Medium'

        color_gradient = QLinearGradient(self.c_width/4, self.c_width/4, 
                        self.c_width, self.c_width)
        color_gradient.setSpread(QGradient.PadSpread)
        color_gradient.setColorAt(0, '#c1a0cb')
        color_gradient.setColorAt(1, '#a676b2')
        self.color = color_gradient

        # configs
        self.setMinimumSize(QSize(self.c_width, self.c_width))
        self.setMaximumSize(QSize(self.c_width, self.c_width))

    def paintEvent(self, event):
        value = (360 / 100) * self.value
        width = self.c_width - 50
        height = width 
        margin = (self.width() / 2) - (width / 2)

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setFont(QFont(self.font_family, 50, QFont.Bold))
        painter.drawRect(QRect(int(margin), int(margin), width, height))
        
        pen = QPen()
        brush = QBrush(self.color)        
        pen.setBrush(brush)
        pen.setWidth(self.progress_width)
        pen.setCapStyle(Qt.SquareCap)
        
        painter.setPen(pen)
        painter.drawArc(int(margin), int(margin), width, height, 
                        -90 * 16, int(-value * 16))
        painter.drawText(QRect(int(margin), int(margin), width, height), Qt.AlignCenter, f'{self.value}%')
        painter.end()
        
        return event
    
