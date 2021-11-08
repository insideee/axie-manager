from PySide6.QtCore import QEvent, QObject, QSize, Qt
from PySide6.QtGui import QEnterEvent, QIcon, QMouseEvent, QPainter, QPixmap
from PySide6.QtWidgets import QSizePolicy, QToolButton


class BtnNav(QToolButton):
    
    def __init__(self, text: str, image: str, default_style: str, clicked_style: str) -> None:
        super(BtnNav, self).__init__()
        
        # properties
        self.image = image
        self.text = text
        self.icon_default = QIcon(self.paint_image(self.image, color='#F4F4F4'))
        self.icon_hover = QIcon(self.paint_image(self.image, color='#f69cfc'))
        self.change_color = True
        self.default_style = default_style
        self.clicked_style = clicked_style
        self.hover_style = 'QToolButton{border-radius: 0px; \
                            border: 0px; \
                            border-top-left-radius: 12px; \
                            border-bottom-left-radius: 12px; \
                            padding-left: 15px; \
                            color: rgb(246,156,252)}'
        self.size = QSize(180, 40)

        # config
        self.setText(f'   {self.text.upper()}')
        self.setStyleSheet(self.default_style)
        self.setMinimumSize(self.size)
        self.setIcon(self.icon_default)
        self.setIconSize(QSize(25, 25))
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.setCursor(Qt.PointingHandCursor)
        self.setObjectName(f"btn_{self.text.lower()}")
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def enterEvent(self, arg__1: QEnterEvent) -> None:
        if self.change_color:
            self.setStyleSheet(self.hover_style)
            self.setIcon(self.icon_hover)
            self.setIconSize(QSize(25, 25))

        return super().enterEvent(arg__1)
    
    def leaveEvent(self, arg__1: QEvent) -> None:
        if self.change_color:
            self.setStyleSheet(self.default_style)
            self.setIcon(self.icon_default)
            self.setIconSize(QSize(25, 25))
        return super().leaveEvent(arg__1)
    
    def mousePressEvent(self, arg__1: QMouseEvent) -> None:
        if arg__1.button() == Qt.LeftButton:
            self.change_color = False
            self.setStyleSheet(self.clicked_style)
            self.setIcon(self.icon_default)
            self.setIconSize(QSize(25, 25))
        return super().mousePressEvent(arg__1)
    
    def paint_image(self, image: str, color: str) -> QPixmap:
        new_image = QPixmap(image)
        paint = QPainter(new_image)
        paint.setCompositionMode(QPainter.CompositionMode_SourceIn)
        paint.fillRect(new_image.rect(), color)
        paint.end()

        return new_image