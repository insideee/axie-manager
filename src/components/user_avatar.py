from PySide6.QtCore import QPoint, QRect, QSize, Qt
from PySide6.QtGui import QBrush, QColor, QPaintEvent, QPainter, QPen, QPixmap
from PySide6.QtWidgets import QApplication, QLabel
import sys


class UserAvatar(QLabel):

    def __init__(self, img: str, guest: bool) -> None:
        super(UserAvatar, self).__init__()

        # properties
        self.guest = guest
        self.size = QSize(80, 80)
        self.image = QPixmap(img)
        
        # config
        self.setMinimumSize(self.size)
        self.setMaximumSize(self.size)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""background-color: rgba(0, 0, 0, 0);
                            border: 0px
                            """)
        
        if self.guest:
            self.image_painted = self.paint_image()
            self.setPixmap(self.image_painted.scaled(QSize(self.width()*0.6, self.height()*0.6), 
                                            Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def paintEvent(self, arg__1: QPaintEvent) -> None:
        if self.guest:
            margin_w = self.width() * 0.1
            margin_h = self.width() * 0.1
            height = self.height() - margin_h
            width = self.width() - margin_w

            draw_rect = QRect(QPoint(margin_w/2, margin_h/2),
                            QSize(width, height))

            paint = QPainter()
            paint.begin(self)
            paint.setRenderHint(QPainter.Antialiasing)

            paint.setPen(Qt.NoPen)
            paint.drawRect(draw_rect)
            paint.setBrush(QBrush(QColor(0xF4F4F4)))
            paint.drawEllipse(draw_rect)

        return super().paintEvent(arg__1)

    def paint_image(self) -> QPixmap:
        new_image = QPixmap(self.image)
        paint = QPainter(new_image)
        paint.setCompositionMode(QPainter.CompositionMode_SourceIn)
        paint.fillRect(new_image.rect(), '#DEDEDE')
        paint.end()

        return new_image

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserAvatar()
    window.show()
    sys.exit(app.exec())