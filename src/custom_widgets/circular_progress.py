from PySide6.QtGui import QPaintEvent, QPainter, QColor, QPen, QFont
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PySide6.QtCore import QRect, Qt, QSize


class CircularProgress(QWidget):
    def __init__(self, width=150, height=150, enable_shadow=True, font_family='Segoe UI'):
        super(CircularProgress, self).__init__()

        # custom properties
        self.value = 0
        self.width = width
        self.height = height
        self.progress_width = 10
        self.reference_width = 5
        self.progress_rounded_cap = True
        self.progress_color = 0xE64C3C
        self.reference_color = 0x737373
        self.progress_color_complete = 0x00e600
        self.max_value = 100
        self.font_family = font_family
        self.font_size = 22
        self.suffix = '%'
        self.text_color = 0xE64C3C
        self.shadow = enable_shadow
        self.shadow_blur_radius = 6

        self.setMinimumSize(QSize(self.width, self.height))
        self.setMaximumSize(QSize(self.width, self.height))

    def update_value(self, value):
        self.value = value
        self.repaint()

    def set_progress_color(self, color):
        self.progress_color = color
        self.repaint()

    def enable_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect()
            self.shadow.setBlurRadius(self.shadow_blur_radius)
            self.shadow.setOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 90))
            self.setGraphicsEffect(self.shadow)

    def paintEvent(self, event: QPaintEvent) -> None:

        # set progress parameters
        width = self.width - 30
        height = self.height - 30
        margin = self.progress_width / 2
        value = (360 / self.max_value) * self.value

        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)  # remove pixelated edges
        paint.setFont(QFont(self.font_family, self.font_size))

        rect = QRect(0, 5, self.width, height)
        paint.setPen(Qt.NoPen)

        paint.drawRect(rect)

        # pen
        pen = QPen()
        pen.setColor(QColor(self.reference_color))
        pen.setWidth(self.reference_width)

        # set round cap
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # create arc reference
        paint.setPen(pen)
        paint.drawArc(15, int(margin), width, height, -90 * 16, -360 * 16)

        # progress arc    
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)

        paint.setPen(pen)
        paint.drawArc(15, int(margin), width, height, -90 * 16, int(-value * 16))

        # create data text
        paint.drawText(rect, Qt.AlignCenter, f'{self.value}{self.suffix}')

        # create label text
        pen.setColor(self.reference_color)
        paint.setFont(QFont(self.font_family, 10))
        paint.setPen(pen)
        
        paint.drawText(60, 195, 'SLP Daily Goal')

        paint.end()
