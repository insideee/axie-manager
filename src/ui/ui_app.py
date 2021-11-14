from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import os

from .app_style import stylesheet
from components import BtnNav, UserAvatar, DashPage, ScholarPage
from resources import resource
from .functions import UIFunctions
from functions import Functions as func
import configs


class Ui_App(object):
    def init_gui(self, app):
        app.setObjectName('app')
        self.func = UIFunctions()
        
        # color schema
        dir_color = os.path.join(os.path.dirname(configs.__file__), 'colorscheme.json')
        self.colorscheme = func.read_json(dir_color)
        
        self.color_gradient_value_1 = self.colorscheme['main colors']['main_color_gradient']
        self.color_gradient_value_2 = self.colorscheme['main colors']['main_color']

        # configs do app
        app.setWindowTitle(' ')
        app.setMinimumSize(QSize(1200, 700))
        app.setMaximumSize(QSize(1200, 700))
        app.setWindowIcon(QIcon(QPixmap(':/img/img/logo.png')))
        app.setGeometry(QStyle.alignedRect(
                        Qt.LeftToRight,
                        Qt.AlignCenter,
                        app.size(),
                        QGuiApplication.primaryScreen().availableGeometry(),
                        ))

        # bg
        self.bg_frame = QFrame(app)
        self.bg_frame.setObjectName('bg_frame')
        self.bg_frame.setStyleSheet(stylesheet['bg'])

        self.bg_layout = QHBoxLayout(self.bg_frame)
        self.bg_layout.setObjectName('bg_layout')
        self.bg_layout.setContentsMargins(0, 0, 0, 0)
        self.bg_layout.setSpacing(0)

        # main frames
        self.nav_frame = QFrame(self.bg_frame)
        self.nav_frame.setObjectName('nav_frame')
        self.nav_frame.setMinimumWidth(220)
        self.nav_frame.setMaximumWidth(220)
        self.nav_frame.setStyleSheet(stylesheet['nav_frame'])
        self.bg_layout.addWidget(self.nav_frame)

        self.nav_layout = QVBoxLayout(self.nav_frame)
        self.nav_layout.setObjectName('nav_layout')
        self.nav_layout.setContentsMargins(0, 0, 5, 0)
        self.nav_layout.setSpacing(0)

        self.content_frame = QFrame(self.bg_frame)
        self.content_frame.setObjectName('content_frame')
        self.bg_layout.addWidget(self.content_frame)

        self.content_layout = QVBoxLayout(self.content_frame)
        self.content_layout.setObjectName('content_layout')
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # nav frame elements
        # user
        self.user_nav_config()

        # menu
        self.menu_nav_config()

        # version
        self.version_nav_config()

        # content frame elements
        # header
        self.header_config()

        # pages
        self.pages_frame = QFrame(self.content_frame)
        self.pages_frame.setObjectName('pages_frame')
        self.content_layout.addWidget(self.pages_frame)

        self.pages_layout = QVBoxLayout(self.pages_frame)
        self.pages_layout.setObjectName('pages_layout')
        self.pages_layout.setContentsMargins(30, 10, 30, 10)
        self.pages_layout.setSpacing(0)

        self.pages_config()

        # info bar
        self.info_bar_frame = QFrame(self.content_frame)
        self.info_bar_frame.setObjectName('inforbar_frame')
        self.info_bar_frame.setMinimumHeight(40)
        self.info_bar_frame.setMaximumHeight(40)
        self.content_layout.addWidget(self.info_bar_frame)

        app.setCentralWidget(self.bg_frame)
        
        # link btns
        self.btn_dash.clicked.connect(lambda: self.stack_pages.setCurrentWidget(self.dash_page))
        self.btn_scholars.clicked.connect(lambda: self.stack_pages.setCurrentWidget(self.scholars_page))

        # initialization
        self.stack_pages.setCurrentWidget(self.dash_page)
        self.btn_dash.setStyleSheet(stylesheet['btn_clicked'])
        self.btn_dash.change_color = False

    def user_nav_config(self) -> None:
        self.user_frame = QFrame(self.nav_frame)
        self.user_frame.setObjectName('user_frame')
        self.user_frame.setMaximumHeight(120)
        self.user_frame.setStyleSheet(stylesheet['user_frame'])
        self.nav_layout.addWidget(self.user_frame)

        self.user_layout = QVBoxLayout(self.user_frame)
        self.user_layout.setObjectName('user_layout')
        self.user_layout.setAlignment(Qt.AlignCenter)
        self.user_layout.setContentsMargins(0, 0, 0, 0)
        self.user_layout.setSpacing(0)

        self.user_avatar = UserAvatar(
            img=':/img/img/guest_user.svg', guest=True)
        self.user_avatar.setObjectName('user_avatar')
        self.user_layout.addWidget(self.user_avatar)

    def menu_nav_config(self) -> None:
        self.menu_frame = QFrame(self.nav_frame)
        self.menu_frame.setObjectName('menu_frame')
        self.menu_frame.setStyleSheet(stylesheet['menu_frame'])
        self.nav_layout.addWidget(self.menu_frame)

        self.menu_layout = QVBoxLayout(self.menu_frame)
        self.menu_layout.setAlignment(Qt.AlignTop | Qt.AlignRight)
        self.menu_layout.setSpacing(8)
        self.menu_layout.setContentsMargins(0, 20, 8, 0)

        self.btn_dash = BtnNav(text='dashboard',
                               image=':/img/img/dash_icon.svg',
                               default_style=stylesheet['btn_default'],
                               clicked_style=stylesheet['btn_clicked'],
                               hover_style=stylesheet['btn_hover'],
                               colorscheme=self.colorscheme)

        self.btn_reports = BtnNav(text='reports',
                                  image=':/img/img/reports_icon.svg',
                                  default_style=stylesheet['btn_default'],
                                  clicked_style=stylesheet['btn_clicked'],
                                  hover_style=stylesheet['btn_hover'],
                                  colorscheme=self.colorscheme)
                                

        self.btn_scholars = BtnNav(text='scholars',
                                   image=':/img/img/user_test.svg',
                                   default_style=stylesheet['btn_default'],
                                   clicked_style=stylesheet['btn_clicked'],
                                   hover_style=stylesheet['btn_hover'],
                                   colorscheme=self.colorscheme)
                                

        self.btn_inventory = BtnNav(text='inventory',
                                    image=':/img/img/inventory.svg',
                                    default_style=stylesheet['btn_default'],
                                    clicked_style=stylesheet['btn_clicked'],
                                    hover_style=stylesheet['btn_hover'],
                                    colorscheme=self.colorscheme)
                                

        list_btn = [self.btn_dash, self.btn_reports,
                    self.btn_scholars, self.btn_inventory]

        for btn in list_btn:
            self.func.set_font(btn,
                               10, ':/fonts/fonts/Montserrat-Medium.ttf',
                               bold=True)
            self.menu_layout.addWidget(btn)
            btn.clicked.connect(self.func.btn_style_applyer)

    def version_nav_config(self) -> None:
        self.version_frame = QFrame(self.nav_frame)
        self.version_frame.setObjectName('version_frame')
        self.version_frame.setMaximumHeight(80)
        self.version_frame.setStyleSheet(stylesheet['version_frame'])
        self.nav_layout.addWidget(self.version_frame)

        self.version_layout = QVBoxLayout(self.version_frame)
        self.version_layout.setObjectName('version_layout')
        self.version_layout.setContentsMargins(0, 0, 0, 0)
        self.version_layout.setSpacing(0)

        self.version_label = QLabel(self.version_frame)
        self.version_label.setObjectName('version_label')
        self.version_label.setText('VERSION 1.0.1')
        self.version_label.setStyleSheet(stylesheet['version_label'])
        self.version_label.setAlignment(Qt.AlignCenter)
        self.func.set_font(self.version_label,
                           10, ':/fonts/fonts/Montserrat-Medium.ttf',
                           bold=True)
        self.version_layout.addWidget(self.version_label)

    def header_config(self):
        self.header_frame = QFrame(self.content_frame)
        self.header_frame.setObjectName('header_frame')
        self.header_frame.setMinimumHeight(120)
        self.header_frame.setMaximumHeight(120)
        self.content_layout.addWidget(self.header_frame)

        self.header_layout = QHBoxLayout(self.header_frame)
        self.header_layout.setObjectName('header_layout')
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)

        self.title_header_config()

        self.search_header_config()

        self.icon__header_config()

    def title_header_config(self) -> None:
        self.title_frame = QFrame(self.header_frame)
        self.title_frame.setObjectName('title_frame')
        self.title_frame.setMinimumWidth(300)
        self.header_layout.addWidget(self.title_frame)

        self.title_layout = QHBoxLayout(self.title_frame)
        self.title_layout.setObjectName('title_layout')
        self.title_layout.setContentsMargins(0, 0, 0, 0)
        self.title_layout.setSpacing(0)

        self.title_label = QLabel(self.title_frame)
        self.title_label.setObjectName('title_label')
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setText('AXIE ACADEMY')
        self.func.set_font(self.title_label,
                           20, ':/fonts/fonts/Montserrat-SemiBold.ttf',
                           bold=True)

        label_pal = QPalette()
        color_gradient = QLinearGradient(self.title_label.width(), 0, 0, 0)
        color_gradient.setSpread(QGradient.PadSpread)
        color_gradient.setColorAt(0, self.color_gradient_value_1)
        color_gradient.setColorAt(1, self.color_gradient_value_2)
        brush = QBrush(color_gradient)
        label_pal.setBrush(QPalette.ColorRole.Text, brush)

        self.title_label.setPalette(label_pal)
        self.title_label.setForegroundRole(QPalette.Text)
        self.title_label.setStyleSheet(stylesheet['title_header_label'])
        self.title_layout.addWidget(self.title_label)

    def search_header_config(self) -> None:
        # main frame
        self.search_frame = QFrame(self.header_frame)
        self.search_frame.setObjectName('search_frame')
        self.search_frame.setMinimumWidth(500)
        self.header_layout.addWidget(self.search_frame)

        self.search_layout = QHBoxLayout(self.search_frame)
        self.search_layout.setObjectName('search_layout')
        self.search_layout.setContentsMargins(20, 0, 20, 0)
        self.search_layout.setSpacing(2)

        # search label
        self.search_label_config()

        # search entry
        self.search_entry_config()

    def search_label_config(self) -> None:
        self.search_label_frame = QFrame()
        self.search_label_frame.setObjectName('search_label_frame')
        self.search_label_frame.setMinimumWidth(150)
        self.search_label_frame.setMaximumWidth(150)
        self.search_label_frame.setMaximumHeight(45)
        self.search_label_frame.setStyleSheet(stylesheet['search_label_frame'])
        self.search_layout.addWidget(self.search_label_frame)
        self.func.set_drop_shadow(self.search_label_frame, blur=20)

        self.search_label_layout = QHBoxLayout(self.search_label_frame)
        self.search_label_layout.setObjectName('search_label_layout')
        self.search_label_layout.setContentsMargins(0, 0, 10, 0)
        self.search_label_layout.setSpacing(0)

        # title
        self.search_label = QLabel(self.search_label_frame)
        self.search_label.setObjectName('search_label')
        self.search_label.setText('SEARCH')
        self.search_label.setCursor(Qt.PointingHandCursor)
        self.search_label.setAlignment(Qt.AlignCenter)
        self.search_label.setStyleSheet('background-color: none')
        self.func.set_font(self.search_label,
                           13, ':/fonts/fonts/Montserrat-Medium.ttf',
                           bold=True)
        self.search_label_layout.addWidget(self.search_label)

        label_pal = QPalette()
        color_gradient = QLinearGradient(0, 0, 1, 18)
        color_gradient.setSpread(QGradient.ReflectSpread)
        color_gradient.setColorAt(0, self.color_gradient_value_1)
        color_gradient.setColorAt(1, self.color_gradient_value_2)
        brush = QBrush(color_gradient)
        label_pal.setBrush(QPalette.ColorRole.Text, brush)

        self.search_label.setPalette(label_pal)
        self.search_label.setForegroundRole(QPalette.Text)
        self.search_label.setStyleSheet(stylesheet['title_header_label'])

        # icon
        self.search_icon = QLabel()
        self.search_icon.setObjectName('search_icon')
        size = QSize(13, 13)
        self.search_icon.setMinimumSize(size)
        self.search_icon.setMaximumSize(size)

        self.painted_img = self.func.paint_image(image=':/img/img/search_arrow.svg',
                                                 color=color_gradient, size=size)

        self.search_icon.setPixmap(self.painted_img)
        self.search_icon.setScaledContents(True)
        self.search_label_layout.addWidget(self.search_icon)

    def search_entry_config(self) -> None:
        self.search_entry_frame = QFrame()
        self.search_entry_frame.setObjectName('search_entry_frame')
        self.search_entry_frame.setStyleSheet(stylesheet['search_entry_frame'])
        self.search_entry_frame.setMaximumHeight(45)
        self.search_layout.addWidget(self.search_entry_frame)
        self.func.set_drop_shadow(self.search_entry_frame, blur=20)

        self.search_entry_layout = QHBoxLayout(self.search_entry_frame)
        self.search_entry_layout.setObjectName('search_entry_layout')
        self.search_entry_layout.setContentsMargins(10, 0, 10, 0)
        self.search_entry_layout.setSpacing(0)

        self.search_entry = QLineEdit(self.search_entry_frame)
        self.search_entry.setMaximumWidth(500)
        self.search_entry.setMinimumHeight(30)
        self.search_entry.setPlaceholderText('Find here...')
        self.search_entry.setObjectName('search_entry')
        self.search_entry.setStyleSheet(stylesheet['search_entry'])
        self.func.set_font(self.search_entry,
                           10, ':/fonts/fonts/Montserrat-Medium.ttf',
                           bold=True, index=1)
        self.search_entry_layout.addWidget(self.search_entry)

        self.search_entry_btn = QToolButton(self.search_entry_frame)
        self.search_entry_btn.setObjectName('search_entry_btn')
        size = QSize(30, 30)
        self.search_entry_btn.setMinimumSize(size)
        self.search_entry_btn.setMaximumSize(size)
        self.entry_icon = self.func.paint_image(
            ':/img/img/search.svg', color=QColor(self.colorscheme['search_box']['icon']), size=size)
        self.search_entry_btn.setIcon(self.entry_icon)
        self.search_entry_btn.setSizePolicy(
            QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.search_entry_btn.setIconSize(size)
        self.search_entry_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.search_entry_layout.addWidget(self.search_entry_btn)

    def icon__header_config(self) -> None:
        self.icons_frame = QFrame(self.header_frame)
        self.icons_frame.setObjectName('icons_frame')
        self.icons_frame.setMinimumWidth(180)
        self.icons_frame.setMaximumWidth(180)
        self.header_layout.addWidget(self.icons_frame)

        self.icons_frame_layout = QHBoxLayout(self.icons_frame)
        self.icons_frame_layout.setObjectName('icons_frame_layout')
        self.icons_frame_layout.setAlignment(Qt.AlignLeft | Qt.AlignCenter)
        self.icons_frame_layout.setContentsMargins(40, 0, 0, 0)
        self.icons_frame_layout.setSpacing(20)

        color_gradient = QLinearGradient(0, 0, 1, 20)
        color_gradient.setSpread(QGradient.ReflectSpread)
        color_gradient.setColorAt(0, self.color_gradient_value_1)
        color_gradient.setColorAt(1, self.color_gradient_value_2)

        self.notification_icon = QLabel(self.icons_frame)
        self.notification_icon.setObjectName('notification_icon')
        self.notification_icon.setCursor(Qt.PointingHandCursor)
        size = QSize(25, 33)
        self.notification_icon.setMinimumSize(size)
        self.notification_icon.setMaximumSize(size)
        icon = self.func.paint_image(
            ':/img/img/notification.svg', color=color_gradient, size=size)
        self.notification_icon.setPixmap(icon)
        self.notification_icon.setScaledContents(True)
        self.icons_frame_layout.addWidget(self.notification_icon)

        self.settings_icon = QLabel(self.icons_frame)
        self.settings_icon.setObjectName('settings_icon')
        self.settings_icon.setCursor(Qt.PointingHandCursor)
        size = QSize(35, 35)
        self.settings_icon.setMinimumSize(size)
        self.settings_icon.setMaximumSize(size)
        icon = self.func.paint_image(
            ':/img/img/settings.svg', color=color_gradient, size=size)
        self.settings_icon.setPixmap(icon)
        self.settings_icon.setScaledContents(True)
        self.icons_frame_layout.addWidget(self.settings_icon)

    def pages_config(self) -> None:
        self.stack_pages = QStackedWidget(self.pages_frame)
        self.stack_pages.setObjectName('stack_pages')
        self.stack_pages.setStyleSheet(stylesheet['stack_page'])
        self.pages_layout.addWidget(self.stack_pages)

        self.dash_page = DashPage(colorscheme=self.colorscheme)
        self.dash_page_config()
        self.stack_pages.addWidget(self.dash_page)

        self.scholars_page = ScholarPage()
        self.scholars_page_config()
        self.stack_pages.addWidget(self.scholars_page)

    def dash_page_config(self):
        label_pal = QPalette()
        color_gradient = QLinearGradient(0, 0, 1, 13)
        color_gradient.setSpread(QGradient.ReflectSpread)
        color_gradient.setColorAt(0, self.color_gradient_value_1)
        color_gradient.setColorAt(1, self.color_gradient_value_2)
        brush = QBrush(color_gradient)
        label_pal.setBrush(QPalette.ColorRole.Text, brush)

        self.func.set_font(self.dash_page.analytics_title_label,
                           16, ':/fonts/fonts/Montserrat-Light.ttf',
                           bold=True, index=1)
        self.dash_page.analytics_title_label.setPalette(label_pal)
        self.dash_page.analytics_title_label.setForegroundRole(QPalette.Text)

        # scholars
        self.dash_page.scholars_widget.setStyleSheet(stylesheet['scholar_widget'])
        self.func.set_drop_shadow(
            self.dash_page.scholars_widget, blur=15, opacity=70)
        self.func.set_font(self.dash_page.scholars_widget.info_label, 10, ':/fonts/fonts/Montserrat-Medium.ttf',
                           bold=True)
        self.func.set_font(self.dash_page.scholars_widget.data_label, 24, ':/fonts/fonts/Montserrat-Light.ttf',
                           bold=False, index=1)
        self.dash_page.scholars_widget.data_label.setText('429')

        # monthly profit
        self.dash_page.m_profit_widget.setStyleSheet(stylesheet['m_profit_widget'])
        self.func.set_drop_shadow(
            self.dash_page.m_profit_widget, blur=15, opacity=70)
        self.func.set_font(self.dash_page.m_profit_widget.info_label, 10, ':/fonts/fonts/Montserrat-Medium.ttf',
                           bold=True)
        self.func.set_font(self.dash_page.m_profit_widget.data_label, 24, ':/fonts/fonts/Montserrat-Light.ttf',
                           bold=False, index=1)
        self.dash_page.m_profit_widget.data_label.setText('1.234.567')

        # axies
        self.dash_page.axies_widget.setStyleSheet(stylesheet['axies_widget'])
        self.func.set_drop_shadow(
            self.dash_page.axies_widget, blur=15, opacity=70)
        self.func.set_font(self.dash_page.axies_widget.info_label, 10, ':/fonts/fonts/Montserrat-Medium.ttf',
                           bold=True)
        self.func.set_font(self.dash_page.axies_widget.data_label, 24, ':/fonts/fonts/Montserrat-Light.ttf',
                           bold=False, index=1)
        self.dash_page.axies_widget.data_label.setText('2.114')

        self.func.set_font(self.dash_page.graph_title,
                           16, ':/fonts/fonts/Montserrat-Light.ttf',
                           bold=True, index=1)
        self.dash_page.daily_w_title.setPalette(label_pal)
        self.dash_page.daily_w_title.setForegroundRole(QPalette.Text)

        # graph
        self.dash_page.graph_title.setPalette(label_pal)
        self.dash_page.graph_title.setForegroundRole(QPalette.Text)
        self.func.set_drop_shadow(self.dash_page.graph, blur=16, opacity=40)

        # daily
        self.dash_page.daily_graph_container.setStyleSheet(stylesheet['daily_frame'])
        self.func.set_drop_shadow(self.dash_page.daily_graph_container,
                                  blur=16, opacity=40)

        self.func.set_font(self.dash_page.daily_w_title,
                           16, ':/fonts/fonts/Montserrat-Light.ttf',
                           bold=True, index=1)

        self.func.set_font(self.dash_page.daily_title,
                           11, ':/fonts/fonts/Montserrat-Light.ttf',
                           bold=True, index=1)
        self.dash_page.daily_title.setPalette(label_pal)
        self.dash_page.daily_title.setForegroundRole(QPalette.Text)

        self.dash_page.daily_label.setStyleSheet(stylesheet['daily_label'])
        self.func.set_font(self.dash_page.daily_label,
                           11, ':/fonts/fonts/Montserrat-Light.ttf',
                           bold=True, index=1)
        
        self.func.setStyleSheet(stylesheet['daily_graph'])

    def scholars_page_config(self):
        
        # bg
        self.scholars_page.setStyleSheet(stylesheet['scholars_page'])
        
        # filter btn
        self.func.set_font(self.scholars_page.filter_btn,
                           9, ':/fonts/fonts/Montserrat-Light.ttf',
                           bold=True, index=1)
        self.scholars_page.filter_btn.setStyleSheet(stylesheet['filter_btn'])
        self.func.set_drop_shadow(self.scholars_page.filter_btn, blur=10, opacity=100)
        
        # add btn
        self.func.set_font(self.scholars_page.add_btn,
                           10, ':/fonts/fonts/Montserrat-Light.ttf',
                           bold=True, index=0)
        self.func.set_drop_shadow(self.scholars_page.add_btn, blur=10, opacity=100)
        
        self.scholars_page.add_btn.setStyleSheet(stylesheet['add_btn'])
        
        # table header frame
        self.scholars_page.header_title_frame.setStyleSheet(stylesheet['table_header'])