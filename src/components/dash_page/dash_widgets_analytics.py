from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor, QIcon, QPainter, QPixmap
from PySide6.QtWidgets import QFrame, QGridLayout, QLabel, QSizePolicy, QToolButton
from PySide6.QtSvg import QSvgRenderer


class CustomWidgets(QFrame):
    
    """Custom widget for for the dashpage, showing the data of some categories.
    """

    def __init__(self, info: str, icon_path: str, btn_icon: str, width: int) -> None:
        """Initialize the custom widget.

        Args:
            info (str): Used for the object name and for the info label
            icon_path (str): Path for the icon image
            btn_icon (str): Path for the button icon image
            width (int): Defines the max width of the widget
        """
        super(CustomWidgets, self).__init__()

        # properties
        self.img = self.paint_image(image=icon_path)
        self.btn_icon = QIcon(self.paint_image(image=btn_icon))
        self.max_width = width
        self.info = info
        self.reset_style = 'background-color: none; \
                            color: #FFFFFF;\
                            border: 0px'

        # configs
        self.setObjectName(self.info)
        self.setMinimumWidth(self.max_width)
        self.setMaximumWidth(self.max_width)

        self.main_layout = QGridLayout(self)
        self.main_layout.setObjectName('main_layout')
        self.main_layout.setContentsMargins(0, (0.04 * self.height()), 0, 0)
        self.main_layout.setAlignment(Qt.AlignHCenter)
        self.main_layout.setSpacing(5)
        
        self.icon_label = QLabel(self)
        self.icon_label.setObjectName('icon_label')
        size = QSize(0.35 * self.width(), 0.35 * self.width())
        self.icon_label.setMinimumSize(size)
        self.icon_label.setMaximumSize(size)
        self.icon_label.setStyleSheet(self.reset_style)
        self.icon_label.setPixmap(self.img)
        self.icon_label.setScaledContents(True)
        self.main_layout.addWidget(
            self.icon_label, 0, 0, alignment=Qt.AlignCenter)

        self.data_label = QLabel(self)
        self.data_label.setObjectName('data_label')
        self.data_label.setMinimumWidth(self.width())
        self.data_label.setMinimumHeight(0.3 * self.width())
        self.data_label.setStyleSheet(self.reset_style)
        self.data_label.setText('0')
        self.data_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.data_label)

        self.info_label = QLabel(self)
        self.info_label.setObjectName('info_label')
        self.info_label.setMinimumWidth(self.width())
        self.info_label.setMaximumHeight(0.15 * self.height())
        self.info_label.setStyleSheet(self.reset_style)
        self.info_label.setText(self.info)
        self.info_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.info_label)

        self.goto_btn = QToolButton(self)
        self.goto_btn.setObjectName('goto_btn')
        size = QSize(0.08 * self.height(), 0.08 * self.height())
        self.goto_btn.setMinimumSize(size)
        self.goto_btn.setMaximumSize(size)
        self.goto_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.goto_btn.setIcon(self.btn_icon)
        self.goto_btn.setIconSize(QSize(20, 20))
        self.goto_btn.setStyleSheet(self.reset_style)
        self.goto_btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.goto_btn.setCursor(Qt.PointingHandCursor)
        self.main_layout.addWidget(self.goto_btn, 3, 0, alignment=Qt.AlignCenter)
        
    def update_data(self, new_data: int) -> None:
        """Update the widget data.

        Args:
            new_data (int): New value
        """
        
        self.data_label.setText(str(new_data))

    def paint_image(self, image: str) -> QPixmap:
        """Method for paint the icon image with the selected color.

        Args:
            image (str): Path of the image
            color (str): Color to paint

        Returns:
            QPixmap: Return the image painted for the icon
        """
        
        svg_render = QSvgRenderer(image)   
        new_image = QPixmap(QSize(0.35 * self.width(), 0.35 * self.width()))
        
        painter = QPainter()
        
        new_image.fill(Qt.transparent)
        
        painter.begin(new_image)
        svg_render.render(painter)
        painter.end()
        
        paint = QPainter(new_image)
        paint.setRenderHint(QPainter.Antialiasing)
        paint.setCompositionMode(QPainter.CompositionMode_SourceIn)
        paint.fillRect(new_image.rect(), QColor(0xFFFFFF))
        paint.end()
        
        return new_image
