from PySide6 import QtGui
from PySide6.QtCore import QAbstractAnimation, QEasingCurve, QEvent, QObject, QPoint, QPropertyAnimation, QRect, QSize, Qt, Signal
from PySide6.QtGui import QColor, QEnterEvent, QMouseEvent, QPainter, QPixmap
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QCheckBox, QFrame, QGraphicsDropShadowEffect, QGridLayout, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QToolButton, QVBoxLayout
from resources import resource


class DataWidget(QFrame):

    def __init__(self, obj_name: str) -> None:
        """Initialize with custom properties, style and the wrapper layout.
        
        Args:
            obj_name (str): Custom object name.
        """

        super(DataWidget, self).__init__()

        # configs
        self.setObjectName(f'entry_{obj_name}')

        # properties
        self.default_stylesheet = """QFrame { background-color: #FFFFFF;
                                    border-bottom: 1px solid #D9D5EC;
                                    border-radius: 0px }"""
        self.selected_stylesheet = """QFrame { background-color: #F4F2FF;
                                    border-bottom: 1px solid #D9D5EC;
                                    border-radius: 0px }"""

        self.expand_image = self.paint_image(image=':/img/img/expand.svg',
                                             color=QColor('#8B83BA'),
                                             size=QSize(20, 20))
        self.minimize_image = self.paint_image(image=':/img/img/minimize.svg',
                                               color=QColor('#8B83BA'),
                                               size=QSize(20, 20))

        self.setStyleSheet(self.default_stylesheet)

        self.wrap_layout = QHBoxLayout(self)
        self.wrap_layout.setObjectName('wrap_layout')
        self.wrap_layout.setAlignment(Qt.AlignLeft)
        self.wrap_layout.setContentsMargins(0, 0, 0, 1)
        self.wrap_layout.setSpacing(0)

        # select expand variables
        self.select_expand_container = None
        self.select_expand_layout = None
        self.check_select_container = None  # for drop shadow container
        self.check_select_container_layout = None
        self.check_box_select = None
        self.expand = None
        self.select_expand_config()

        # data variables
        self.data_config()

        # view more variables
        self.view_more_container = None
        self.view_more_layout = None
        self.view_more_btn = None
        self.view_more_menu_btn = None
        self.view_more_menu_icon = self.paint_image(image=':/img/img/more_menu.svg',
                                                    color=QColor('#8B83BA'),
                                                    size=QSize(25, 25))
        self.view_more_menu_icon_painted = self.paint_image(image=':/img/img/more_menu.svg',
                                                            color=QColor(
                                                                '#6D5BD0'),
                                                            size=QSize(25, 25))
        self.view_more_menu_exit_icon = self.paint_image(image=':/img/img/exit_popup.svg',
                                                         color=QColor(
                                                             '#8B83BA'),
                                                         size=QSize(18, 18))
        self.popup = None

        self.view_more_config()

    def select_expand_config(self):
        """Select and expand buttons.
        """

        self.select_expand_container = QFrame(self)
        self.select_expand_container.setObjectName('select_expand_container')
        self.select_expand_container.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.select_expand_container.setMaximumWidth(100)
        self.select_expand_container.setMinimumWidth(100)
        self.select_expand_container.setStyleSheet('border: none;\
                                                    background-color: none')
        self.wrap_layout.addWidget(self.select_expand_container)

        self.select_expand_layout = QHBoxLayout(self.select_expand_container)
        self.select_expand_layout.setObjectName('select_expand_layout')
        self.select_expand_layout.setContentsMargins(0, 0, 0, 0)
        self.select_expand_layout.setSpacing(0)

        # checkbox
        self.check_select_container = QFrame()
        self.check_select_container.setObjectName('check_container')
        self.check_select_container.setMinimumSize(QSize(22, 22))
        self.check_select_container.setMaximumSize(QSize(22, 22))
        self.check_select_container.setStyleSheet('border-radius: 4px;\
                                    border: none;')
        self.select_expand_layout.addWidget(self.check_select_container)
        self.set_shadow_effect(self.check_select_container)

        self.check_select_container_layout = QHBoxLayout(
            self.check_select_container)
        self.check_select_container_layout.setObjectName(
            'select_expand_layout')
        self.check_select_container_layout.setContentsMargins(0, 0, 0, 0)
        self.check_select_container_layout.setSpacing(0)

        self.check_box_select = QCheckBox()
        self.check_box_select.setCursor(Qt.PointingHandCursor)
        self.check_select_container_layout.addWidget(self.check_box_select)
        self.check_box_select.setStyleSheet("""QCheckBox{ background-color: none;
                                                    border: none;
                                                    border-radius: 5px;
                                        }
                                        QCheckBox::indicator{
                                                        background-color: none;
                                                        border: 2px solid #8B83BA;
                                                        width: 18;
                                                        height: 18;
                                                        border-radius: 4px;}
                                        QCheckBox::indicator::checked{
                                                            background-color: #8B83BA;
                                                            image: url(:/img/img/checked.svg)}""")
        self.check_box_select.stateChanged.connect(
            self.checkbox_select_pressed)

        self.expand = CustomExpBtn(image=self.expand_image)
        self.expand.clicked.connect(self.expand_pressed)
        self.select_expand_layout.addWidget(self.expand)

    def data_config(self):
        self.data_container = QFrame(self)
        self.data_container.setObjectName('data_container')
        self.data_container.setStyleSheet('background-color: none;\
                                            border: none')
        self.data_container.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.wrap_layout.addWidget(self.data_container)

        self.data_layout = QGridLayout(self.data_container)
        self.data_layout.setObjectName('data_layout')
        self.data_layout.setAlignment(Qt.AlignTop)
        self.data_layout.setContentsMargins(0, 0, 0, 0)
        self.data_layout.setSpacing(0)

        size = QSize(144, 50)

        self.data_name = QLabel(self.data_container)
        self.data_name.setObjectName('data_name')
        self.data_name.setAlignment(Qt.AlignCenter)
        self.data_name.setMinimumSize(size)
        self.data_name.setMaximumSize(size)
        self.data_name.setText('name')
        self.data_name.move(0, 0)

        self.data_today = QLabel(self.data_container)
        self.data_today.setObjectName('data_today')
        self.data_today.setAlignment(Qt.AlignCenter)
        self.data_today.setMinimumSize(size)
        self.data_today.setMaximumSize(size)
        self.data_today.setText('today')
        self.data_today.move(144, 0)

        self.data_yesterday = QLabel(self.data_container)
        self.data_yesterday.setObjectName('data_yesterday')
        self.data_yesterday.setAlignment(Qt.AlignCenter)
        self.data_yesterday.setMinimumSize(size)
        self.data_yesterday.setMaximumSize(size)
        self.data_yesterday.setText('yesterday')
        self.data_yesterday.move(288, 0)

        self.data_total = QLabel(self.data_container)
        self.data_total.setObjectName('data_total')
        self.data_total.setAlignment(Qt.AlignCenter)
        self.data_total.setMinimumSize(size)
        self.data_total.setMaximumSize(size)
        self.data_total.setText('total')
        self.data_total.move(432, 0)

        self.data_next_claim = QLabel(self.data_container)
        self.data_next_claim.setObjectName('data_next_claim')
        self.data_next_claim.setAlignment(Qt.AlignCenter)
        self.data_next_claim.setMinimumSize(size)
        self.data_next_claim.setMaximumSize(size)
        self.data_next_claim.setText('next_claim')
        self.data_next_claim.move(576, 0)

        self.data_winrate = QLabel(self.data_container)
        self.data_winrate.setObjectName('data_winrate')
        self.data_winrate.setAlignment(Qt.AlignCenter)
        self.data_winrate.setMinimumSize(size)
        self.data_winrate.setMaximumSize(size)
        self.data_winrate.setText('winrate')
        self.data_winrate.move(0, 50)

        self.data_average = QLabel(self.data_container)
        self.data_average.setObjectName('data_average')
        self.data_average.setAlignment(Qt.AlignCenter)
        self.data_average.setMinimumSize(size)
        self.data_average.setMaximumSize(size)
        self.data_average.setText('average')
        self.data_average.move(144, 50)

        self.data_elo = QLabel(self.data_container)
        self.data_elo.setObjectName('data_elo')
        self.data_elo.setAlignment(Qt.AlignCenter)
        self.data_elo.setMinimumSize(size)
        self.data_elo.setMaximumSize(size)
        self.data_elo.setText('elo')
        self.data_elo.move(288, 50)

        self.data_scholar_slp = QLabel(self.data_container)
        self.data_scholar_slp.setObjectName('data_scholar_slp')
        self.data_scholar_slp.setAlignment(Qt.AlignCenter)
        self.data_scholar_slp.setMinimumSize(size)
        self.data_scholar_slp.setMaximumSize(size)
        self.data_scholar_slp.setText('scholar_slp')
        self.data_scholar_slp.move(432, 50)

        self.data_manager_slp = QLabel(self.data_container)
        self.data_manager_slp.setObjectName('data_manager_slp')
        self.data_manager_slp.setAlignment(Qt.AlignCenter)
        self.data_manager_slp.setMinimumSize(size)
        self.data_manager_slp.setMaximumSize(size)
        self.data_manager_slp.setText('manager_slp')
        self.data_manager_slp.move(576, 50)

    def view_more_config(self):
        self.view_more_container = QFrame(self)
        self.view_more_container.setObjectName('view_more_container')
        self.view_more_container.setMinimumWidth(100)
        self.view_more_container.setMaximumWidth(100)
        self.view_more_container.setStyleSheet('border: none')
        self.view_more_container.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.wrap_layout.addWidget(self.view_more_container)

        self.view_more_layout = QHBoxLayout(self.view_more_container)
        self.view_more_layout.setObjectName('view_more_layout')
        self.view_more_layout.setAlignment(Qt.AlignVCenter)
        self.view_more_layout.setContentsMargins(0, 0, 0, 0)
        self.view_more_layout.setSpacing(0)

        self.view_more_btn = QPushButton(self.view_more_container)
        self.view_more_btn.setObjectName('view_more_btn')
        self.view_more_btn.setCursor(Qt.PointingHandCursor)
        self.view_more_btn.setText('View More')
        self.view_more_btn.setStyleSheet("""QPushButton{ background-color: none;
                                                        color: #8B83BA;
                                                        border: none;}
                                          QPushButton::hover{ color: #6D5BD0
                                              }""")
        self.set_font(target=self.view_more_btn,
                      size=9, font_name=':/fonts/fonts/Montserrat-Medium.ttf',
                      bold=False, index=1)
        self.view_more_layout.addWidget(self.view_more_btn)

        self.view_more_menu_btn = CustomMenuBtn(default_image=self.view_more_menu_icon,
                                                painted_image=self.view_more_menu_icon_painted)

        self.view_more_menu_btn.clicked.connect(
            self.view_more_menu_btn_pressed)

        self.view_more_layout.addWidget(self.view_more_menu_btn)

    def view_more_menu_btn_pressed(self):
        global_pos = self.view_more_container.mapToGlobal(QPoint(0, 0))
        move_to = global_pos - QPoint(15, 10)

        if self.popup == None:
            self.popup = MoreMenuPopup(image=self.view_more_menu_exit_icon,
                                       pos_spawn=move_to)
            for frame in [self.popup.bg_container, self.popup.exit_btn]:
                self.set_shadow_effect(frame, blur=10, opacity=40)

            for btn in [self.popup.edit_btn, self.popup.delete_btn]:
                self.set_font(target=btn,
                              size=9, font_name=':/fonts/fonts/Montserrat-Medium.ttf',
                              bold=False, index=1)

        else:
            self.popup.move(move_to)

        self.popup.show()

    def checkbox_select_pressed(self):
        """Change the style and handle with selected functionality.
        """
        if self.check_box_select.isChecked():
            self.setStyleSheet(self.selected_stylesheet)
        else:
            self.setStyleSheet(self.default_stylesheet)

    def expand_pressed(self, expand):
        """Method triggered when expand button pressed.

        Args:
            expand (bool): True for expanding and false for minimizing
        """

        if expand:
            self.expand.setPixmap(self.minimize_image)
        else:
            self.expand.setPixmap(self.expand_image)

        # check if has one already maximized
        another_max, widget_maximized = self.check_another_maximized()

        if another_max:
            self.animation_expand(widget_maximized, self)
        else:
            self.animation_expand(self)

    def check_another_maximized(self) -> list:
        """Check if any other data entry is maximized the return it.

        Returns:
            list: Bool with the result, none if false otherwise return the QWidget. 
        """
        parent = self.parent()

        for widget in parent.findChildren(QFrame):
            if widget.objectName().startswith('entry'):
                if widget.height() > 50 and widget.objectName() != self.objectName():
                    return [True, widget]

        return [False, None]

    def animation_expand(self, widget, next_animation=None):
        """Handle with the expand/minimize animation.

        Args:
            widget (QWidget): Target of the animation
            next_animation (QWidget, optional): If already one maximized, the target its the
            widget to be minimized and next_animatiom is the widget in queue. Defaults to None.
        """

        # get width
        height = widget.height()
        max_extend = 100
        standard = 48

        change_minimum = False

        if height <= 50:
            height_extend = max_extend
        else:
            height_extend = standard
            change_minimum = True

        widget.animation = QPropertyAnimation(widget, b'minimumHeight')
        widget.animation.setDuration(180)
        widget.animation.setStartValue(height)
        widget.animation.setEndValue(height_extend)
        widget.animation.setEasingCurve(QEasingCurve.InQuad)
        widget.animation.start(QAbstractAnimation.DeleteWhenStopped)

        widget.animation.finished.connect(lambda: self.end_animation_handle(main_widget=widget,
                                                                            need_set_minimum=change_minimum,
                                                                            next_animation=next_animation))

    def end_animation_handle(self, main_widget, need_set_minimum, next_animation):
        """Verify if the animation is minimizing, if yes then set the
        minimum back to 0, so the others animations dont bug. Start the second 
        animation if needed.

        Args:
            main_widget (QFrame): This is the primary animation
            need_set_minimum (bool): If minimizing this will be true
            next_animation (QFrame): If this is different of None will
                                        have another animation
        """
        if need_set_minimum:
            main_widget.setMinimumHeight(0)

        if next_animation != None:
            main_widget.expand.state_clicked = False
            main_widget.expand.setPixmap(self.expand_image)
            self.animation_expand(next_animation)

    def set_shadow_effect(self, element, blur=1, opacity=30):
        """The shadow effect method.

        Args:
            element (QObject): Target for the shadow effect.
            blur (int, optional): Blur for effect. Defaults to 1.
            opacity (int, optional): Opacity for the effect. Defaults to 30.
        """

        drop_shadow = QGraphicsDropShadowEffect(element)
        drop_shadow.setBlurRadius(blur)
        drop_shadow.setOffset(0)
        drop_shadow.setColor(QtGui.QColor(0, 0, 0, opacity))
        element.setGraphicsEffect(drop_shadow)
        drop_shadow.setEnabled(True)

    def paint_image(self, image: str, color: QColor, size: QSize) -> QtGui.QPixmap:
        """Paint image method.

        Args:
            image (str): Path of the image
            color (QColor): Color to be painted
            size (QSize): Size for the image resize.

        Returns:
            QtGui.QPixmap: The image already painted
        """

        svg_render = QSvgRenderer(image)
        new_image = QPixmap(QSize(size))

        painter = QPainter()

        new_image.fill(Qt.transparent)

        painter.begin(new_image)
        svg_render.render(painter)
        painter.end()

        paint = QPainter(new_image)
        paint.setRenderHint(QPainter.Antialiasing)
        paint.setCompositionMode(QPainter.CompositionMode_SourceIn)
        paint.fillRect(new_image.rect(), color)
        paint.end()

        return new_image

    def set_font(self, target: QObject, size: int, font_name: str, bold: bool, index: int = 0) -> None:
        """Set font for the target object.

        Args:
            target (QObject): Target for the font applier
            size (int): Size of the font
            font_name (str): Font name
            bold (bool): Bold or not
            index (int, optional): Index of the font family. Defaults to 0.
        """

        # temp
        font_id = QtGui.QFontDatabase.addApplicationFont(f'{font_name}')
        font_nam = QtGui.QFontDatabase.applicationFontFamilies(font_id)
        font = QtGui.QFont(font_nam[index])
        font.setPointSize(size)
        font.setBold(bold)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)

        target.setFont(font)


class CustomExpBtn(QLabel):
    """Custom button for better image resolution and custom event
    """

    clicked = Signal(bool)

    def __init__(self, image: QPixmap):
        super(CustomExpBtn, self).__init__()

        self.state_clicked = False

        self.setObjectName('expand')
        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumSize(20, 20)
        self.setMaximumSize(20, 20)
        self.setStyleSheet('background-color: none;\
                                  border: none;\
                                    ')
        self.setPixmap(image)
        self.setScaledContents(True)

    def mousePressEvent(self, ev: QMouseEvent) -> None:

        if not self.state_clicked:
            self.state_clicked = True
        else:
            self.state_clicked = False

        self.clicked.emit(self.state_clicked)

        return super().mousePressEvent(ev)


class CustomMenuBtn(QToolButton):
    """Custom button for the view more menu.
    """

    def __init__(self, default_image: QPixmap, painted_image: QPixmap):
        super(CustomMenuBtn, self).__init__()

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


class MoreMenuPopup(QFrame):
    """Custom popup for the more menu button.
    """

    def __init__(self, image, pos_spawn):
        super(MoreMenuPopup, self).__init__()

        # properties
        self.exit_icon = image

        # config
        self.setGeometry(QRect(pos_spawn, QSize(120, 105)))
        self.setMinimumSize(QSize(120, 105))
        self.setMaximumSize(QSize(120, 105))

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setObjectName('main_layout')
        self.main_layout.setContentsMargins(5, 15, 15, 5)
        self.main_layout.setSpacing(0)

        self.setWindowFlags(Qt.FramelessWindowHint |
                            Qt.WindowStaysOnTopHint | Qt.NoDropShadowWindowHint | Qt.Popup)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.bg_container = QFrame(self)
        self.bg_container.setObjectName('bg_container')
        self.bg_container.setStyleSheet("""background-color: #FFFFFF;
                        border: none;
                        border-radius: 10px""")
        self.main_layout.addWidget(self.bg_container)

        self.bg_layout = QVBoxLayout(self.bg_container)
        self.bg_layout.setObjectName('bg_layout')
        self.bg_layout.setContentsMargins(5, 5, 5, 5)
        self.bg_layout.setSpacing(5)
        self.bg_layout.setAlignment(Qt.AlignTop)

        self.exit_btn = QToolButton(self)
        self.exit_btn.setGeometry(90, 4, 20, 20)
        self.exit_btn.setStyleSheet("""background-color: #FFFFFF;
                                        border: none;
                                        border-radius: 10px
                                    """)
        self.exit_btn.setIcon(self.exit_icon)
        self.exit_btn.setIconSize(QSize(18, 18))
        self.exit_btn.setCursor(Qt.PointingHandCursor)
        self.exit_btn.setMouseTracking(True)

        self.exit_btn.clicked.connect(self.exit_btn_clicked_handle)

        self.edit_btn = QPushButton(self.bg_container)
        self.edit_btn.setObjectName('edit_btn')
        self.edit_btn.setCursor(Qt.PointingHandCursor)
        self.edit_btn.setText('Edit')
        self.edit_btn.setStyleSheet("""QPushButton{background-color: none;
                                            border: none;
                                            border-radius: 10px;
                                            padding: 10px;
                                            text-align: left;
                                            color: #8B83BA
                                        }
                                        QPushButton::hover{ 
                                            background-color: #D9D5EC
                                        }
                                    """)
        self.edit_btn.clicked.connect(self.edit_btn_clicked_handle)
        self.bg_layout.addWidget(self.edit_btn)

        self.delete_btn = QPushButton(self.bg_container)
        self.delete_btn.setObjectName('delete_btn')
        self.delete_btn.setCursor(Qt.PointingHandCursor)
        self.delete_btn.setText('Delete')
        self.delete_btn.setStyleSheet("""QPushButton{background-color: none;
                                            border: none;
                                            border-radius: 10px;
                                            padding: 10px;
                                            text-align: left;
                                            color: #D30000
                                        }
                                        QPushButton::hover{ 
                                            background-color: #D9D5EC
                                        }
                                    """)
        self.delete_btn.clicked.connect(self.delete_btn_clicked_handle)
        self.bg_layout.addWidget(self.delete_btn)

    def exit_btn_clicked_handle(self):
        self.close()

    def edit_btn_clicked_handle(self):
        pass

    def delete_btn_clicked_handle(self):
        pass
