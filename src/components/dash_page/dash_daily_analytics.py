from PySide6.QtWidgets import QFrame
from PySide6.QtCore import QSize, QRect, Qt
from PySide6.QtGui import QPaintEvent, QPainter, QPen, QLinearGradient, QGradient, QBrush, QFont


class DailyGoalWidget(QFrame):
    
    """Custom widget for the dashboard showing 
        the partial daily profit
    """

    def __init__(self, width: int, gradient_color_1: str, gradient_color_2: str) -> None:
        """Initialize with property definitions

        Args:
            width (int): Define the maximum width of the widget
        """
        
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
        color_gradient.setColorAt(0, gradient_color_1)
        color_gradient.setColorAt(1, gradient_color_2)
        self.color = color_gradient

        # configs
        self.setMinimumSize(QSize(self.c_width, self.c_width))
        self.setMaximumSize(QSize(self.c_width, self.c_width))

    def update_value(self, value: int) -> None:
        """Update the percent value and repaint the widget

        Args:
            value (int): Percent value
        """
        
        self.value = value
        self.repaint()

    def paintEvent(self, event: QPaintEvent) -> None:
        """Paint the widget

        Args:
            event (QPaintEvent): Automatic event triggered
        """
        
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
        painter.drawText(QRect(int(margin), int(margin), width,
                         height), Qt.AlignCenter, f'{self.value}%')
        painter.end()
