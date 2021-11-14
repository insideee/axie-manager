from PySide6.QtCore import QEvent, QSize, Qt
from PySide6.QtGui import QEnterEvent, QMouseEvent
from PySide6.QtWidgets import QSizePolicy, QToolButton
from functions import Functions as func

class BtnNav(QToolButton):
    
    """Custom QToolButton for the application menu.
    """
    
    def __init__(self: str, text: str, image: str, default_style: str, clicked_style: str, hover_style: str, colorscheme: dict) -> None:
        """Initialize and customize the button.

        Args:
            text (str): Text for the button
            image (str): Path for the icon image
            default_style (str): Stylesheet for the default style
            clicked_style (str): Stylesheet for the clicked style
            hover_style (str): Stylesheet for the hover style
        """
        
        super(BtnNav, self).__init__()
        
        # properties
        self.image = image
        self.text = text
        self.icon_default = func.paint_image(self.image, color=colorscheme['main colors']['menu_icon'], size=QSize(25, 25))
        self.icon_hover = func.paint_image(self.image, color=colorscheme['main colors']['menu_hover_icon'], size=QSize(25, 25))
        self.change_color = True
        self.default_style = default_style
        self.clicked_style = clicked_style
        self.hover_style = hover_style
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
        """Event triggered when mouse hover the widget.
        """
        
        if self.change_color:
            self.setStyleSheet(self.hover_style)
            self.setIcon(self.icon_hover)
            self.setIconSize(QSize(25, 25))

        return super().enterEvent(arg__1)
    
    def leaveEvent(self, arg__1: QEvent) -> None:
        """Event triggered when mouse leave the button.
        """
        
        if self.change_color:
            self.setStyleSheet(self.default_style)
            self.setIcon(self.icon_default)
            self.setIconSize(QSize(25, 25))
        return super().leaveEvent(arg__1)
    
    def mousePressEvent(self, arg__1: QMouseEvent) -> None:
        """Event triggered when mouse click the button.
        """
        
        if arg__1.button() == Qt.LeftButton:
            self.change_color = False
            self.setStyleSheet(self.clicked_style)
            self.setIcon(self.icon_default)
            self.setIconSize(QSize(25, 25))
        return super().mousePressEvent(arg__1)
    