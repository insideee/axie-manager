# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainLRfNft.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

try:
        import resources.resources_rc
except ModuleNotFoundError:
        import src.resources.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1201, 680)
        MainWindow.setMinimumSize(QSize(1200, 680))
        MainWindow.setStyleSheet(u"border: 0px solid;")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.bg = QWidget(MainWindow)
        self.bg.setObjectName(u"bg")
        self.bg.setMinimumSize(QSize(0, 0))
        self.bg.setStyleSheet(u"background-color:  #303840;\n"
"border-radius: 10px;")
        self.verticalLayout = QVBoxLayout(self.bg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QWidget(self.bg)
        self.container.setObjectName(u"container")
        self.horizontalLayout = QHBoxLayout(self.container)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_container = QWidget(self.container)
        self.menu_container.setObjectName(u"menu_container")
        self.menu_container.setMinimumSize(QSize(52, 0))
        self.menu_container.setMaximumSize(QSize(52, 16777215))
        self.menu_container.setStyleSheet(u"QWidget{\n"
"background-color: #1E2226;\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QToolButton {\n"
"	background-color: #1E2226;\n"
"	border-radius: 0px;\n"
"	padding-left: 15px;\n"
"	margin-right: 0px;\n"
"	color: #ffffff\n"
"	}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.menu_container)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 8, 0, 0)
        self.btn_toggle = QToolButton(self.menu_container)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setMinimumSize(QSize(0, 30))
        self.btn_toggle.setStyleSheet(u"QToolButton {\n"
"	background-color: #1E2226;\n"
"	padding-left: 3px\n"
"	}\n"
"\n"
"QToolButton:hover {\n"
"	background-color: #1E2226\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/img/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)

        self.verticalLayout_4.addWidget(self.btn_toggle)

        self.btn_home = QToolButton(self.menu_container)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(140, 30))
        self.btn_home.setFocusPolicy(Qt.NoFocus)
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"QToolButton{\n"
"background-color: #303840;\n"
"border-left: 2px solid  #E64C3C;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/images/img/home_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon1)
        self.btn_home.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.btn_home.setAutoRaise(False)

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_profit = QToolButton(self.menu_container)
        self.btn_profit.setObjectName(u"btn_profit")
        sizePolicy1.setHeightForWidth(self.btn_profit.sizePolicy().hasHeightForWidth())
        self.btn_profit.setSizePolicy(sizePolicy1)
        self.btn_profit.setMinimumSize(QSize(140, 30))
        icon2 = QIcon()
        icon2.addFile(u":/images/img/profit_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_profit.setIcon(icon2)
        self.btn_profit.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_4.addWidget(self.btn_profit)

        self.btn_students = QToolButton(self.menu_container)
        self.btn_students.setObjectName(u"btn_students")
        sizePolicy1.setHeightForWidth(self.btn_students.sizePolicy().hasHeightForWidth())
        self.btn_students.setSizePolicy(sizePolicy1)
        self.btn_students.setMinimumSize(QSize(140, 30))
        icon3 = QIcon()
        icon3.addFile(u":/images/img/user_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_students.setIcon(icon3)
        self.btn_students.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_4.addWidget(self.btn_students)

        self.btn_inventory = QToolButton(self.menu_container)
        self.btn_inventory.setObjectName(u"btn_inventory")
        sizePolicy1.setHeightForWidth(self.btn_inventory.sizePolicy().hasHeightForWidth())
        self.btn_inventory.setSizePolicy(sizePolicy1)
        self.btn_inventory.setMinimumSize(QSize(140, 30))
        icon4 = QIcon()
        icon4.addFile(u":/images/img/inventory_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_inventory.setIcon(icon4)
        self.btn_inventory.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_4.addWidget(self.btn_inventory)

        self.btn_mail = QToolButton(self.menu_container)
        self.btn_mail.setObjectName(u"btn_mail")
        sizePolicy1.setHeightForWidth(self.btn_mail.sizePolicy().hasHeightForWidth())
        self.btn_mail.setSizePolicy(sizePolicy1)
        self.btn_mail.setMinimumSize(QSize(140, 30))
        self.btn_mail.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/images/img/mail_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_mail.setIcon(icon5)
        self.btn_mail.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_4.addWidget(self.btn_mail)

        self.bottom_menu = QWidget(self.menu_container)
        self.bottom_menu.setObjectName(u"bottom_menu")
        self.bottom_menu.setMinimumSize(QSize(0, 0))
        self.bottom_menu.setMaximumSize(QSize(16777215, 120))
        self.bottom_menu.setStyleSheet(u"QToolButton {\n"
"	background-color: #1E2226;\n"
"	border-radius: 0px;\n"
"	padding-left: 15px;\n"
"	}")
        self.verticalLayout_6 = QVBoxLayout(self.bottom_menu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 10)
        self.btn_settings = QToolButton(self.bottom_menu)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(140, 30))
        icon6 = QIcon()
        icon6.addFile(u":/images/img/config_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon6)
        self.btn_settings.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_6.addWidget(self.btn_settings)


        self.verticalLayout_4.addWidget(self.bottom_menu, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.menu_container)

        self.right_container = QWidget(self.container)
        self.right_container.setObjectName(u"right_container")
        self.verticalLayout_2 = QVBoxLayout(self.right_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_bar_container = QWidget(self.right_container)
        self.top_bar_container.setObjectName(u"top_bar_container")
        self.top_bar_container.setMinimumSize(QSize(0, 45))
        self.top_bar_container.setMaximumSize(QSize(16777215, 45))
        self.verticalLayout_7 = QVBoxLayout(self.top_bar_container)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.top_bar = QWidget(self.top_bar_container)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setStyleSheet(u"background-color: #47525E;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;")
        self.horizontalLayout_2 = QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_window_container = QWidget(self.top_bar)
        self.title_window_container.setObjectName(u"title_window_container")
        self.title_window_container.setMinimumSize(QSize(0, 0))
        self.title_window_container.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.title_window_container)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.logo_contant = QWidget(self.title_window_container)
        self.logo_contant.setObjectName(u"logo_contant")
        sizePolicy1.setHeightForWidth(self.logo_contant.sizePolicy().hasHeightForWidth())
        self.logo_contant.setSizePolicy(sizePolicy1)
        self.logo_contant.setMinimumSize(QSize(25, 25))
        self.logo_contant.setMaximumSize(QSize(25, 99999))
        self.verticalLayout_8 = QVBoxLayout(self.logo_contant)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.logo_label = QLabel(self.logo_contant)
        self.logo_label.setObjectName(u"logo_label")
        sizePolicy1.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy1)
        self.logo_label.setMinimumSize(QSize(25, 25))
        self.logo_label.setMaximumSize(QSize(25, 25))
        self.logo_label.setPixmap(QPixmap(u":/images/img/mizer_logo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setMargin(2)

        self.verticalLayout_8.addWidget(self.logo_label)


        self.horizontalLayout_3.addWidget(self.logo_contant, 0, Qt.AlignVCenter)

        self.title_content = QWidget(self.title_window_container)
        self.title_content.setObjectName(u"title_content")
        self.horizontalLayout_4 = QHBoxLayout(self.title_content)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.title1_label = QLabel(self.title_content)
        self.title1_label.setObjectName(u"title1_label")
        self.title1_label.setOpenExternalLinks(True)

        self.horizontalLayout_4.addWidget(self.title1_label)

        self.title2_label = QLabel(self.title_content)
        self.title2_label.setObjectName(u"title2_label")

        self.horizontalLayout_4.addWidget(self.title2_label)


        self.horizontalLayout_3.addWidget(self.title_content, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.title_window_container)

        self.btn_content = QWidget(self.top_bar)
        self.btn_content.setObjectName(u"btn_content")
        self.horizontalLayout_5 = QHBoxLayout(self.btn_content)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 10, 0)
        self.btn_minimize = QToolButton(self.btn_content)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(25, 0))
        self.btn_minimize.setMaximumSize(QSize(30, 16777215))
        icon7 = QIcon()
        icon7.addFile(u":/images/img/minimize_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon7)
        self.btn_minimize.setIconSize(QSize(10, 10))

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_expand = QToolButton(self.btn_content)
        self.btn_expand.setObjectName(u"btn_expand")
        self.btn_expand.setMinimumSize(QSize(25, 0))
        self.btn_expand.setMaximumSize(QSize(30, 16777215))
        icon8 = QIcon()
        icon8.addFile(u":/images/img/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_expand.setIcon(icon8)
        self.btn_expand.setIconSize(QSize(10, 10))

        self.horizontalLayout_5.addWidget(self.btn_expand)

        self.btn_exit = QToolButton(self.btn_content)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(25, 0))
        self.btn_exit.setMaximumSize(QSize(30, 16777215))
        icon9 = QIcon()
        icon9.addFile(u":/images/img/close_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit.setIcon(icon9)
        self.btn_exit.setIconSize(QSize(10, 10))

        self.horizontalLayout_5.addWidget(self.btn_exit)


        self.horizontalLayout_2.addWidget(self.btn_content, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_7.addWidget(self.top_bar)


        self.verticalLayout_2.addWidget(self.top_bar_container)

        self.content_container = QWidget(self.right_container)
        self.content_container.setObjectName(u"content_container")
        self.verticalLayout_3 = QVBoxLayout(self.content_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pages_container = QStackedWidget(self.content_container)
        self.pages_container.setObjectName(u"pages_container")
        self.pages_container.setStyleSheet(u"border-radius: 0px")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_9 = QVBoxLayout(self.home_page)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.home_container = QWidget(self.home_page)
        self.home_container.setObjectName(u"home_container")
        self.verticalLayout_11 = QVBoxLayout(self.home_container)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 50, 0, 0)
        self.widgets_home = QWidget(self.home_container)
        self.widgets_home.setObjectName(u"widgets_home")
        self.widgets_home.setMinimumSize(QSize(0, 191))
        self.widgets_home.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.widgets_home)
        self.horizontalLayout_6.setSpacing(90)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(60, 25, 60, 25)
        self.students_widget = QWidget(self.widgets_home)
        self.students_widget.setObjectName(u"students_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.students_widget.sizePolicy().hasHeightForWidth())
        self.students_widget.setSizePolicy(sizePolicy2)
        self.students_widget.setMinimumSize(QSize(283, 141))
        self.students_widget.setMaximumSize(QSize(339, 169))
        self.students_widget.setStyleSheet(u"background-color: #47525E;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;")
        self.verticalLayout_12 = QVBoxLayout(self.students_widget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 2, -1, -1)
        self.top_bar_students = QWidget(self.students_widget)
        self.top_bar_students.setObjectName(u"top_bar_students")
        self.horizontalLayout_7 = QHBoxLayout(self.top_bar_students)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, -1, 0)
        self.icon_students_container = QWidget(self.top_bar_students)
        self.icon_students_container.setObjectName(u"icon_students_container")
        self.icon_students_container.setMaximumSize(QSize(15, 15))
        self.verticalLayout_13 = QVBoxLayout(self.icon_students_container)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.icon_students = QLabel(self.icon_students_container)
        self.icon_students.setObjectName(u"icon_students")
        self.icon_students.setPixmap(QPixmap(u":/images/img/user_icon.png"))
        self.icon_students.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.icon_students, 0, Qt.AlignVCenter)


        self.horizontalLayout_7.addWidget(self.icon_students_container, 0, Qt.AlignVCenter)

        self.title_students_container = QWidget(self.top_bar_students)
        self.title_students_container.setObjectName(u"title_students_container")
        self.verticalLayout_14 = QVBoxLayout(self.title_students_container)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.title_students = QLabel(self.title_students_container)
        self.title_students.setObjectName(u"title_students")

        self.verticalLayout_14.addWidget(self.title_students)


        self.horizontalLayout_7.addWidget(self.title_students_container, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_12.addWidget(self.top_bar_students)

        self.data_students = QWidget(self.students_widget)
        self.data_students.setObjectName(u"data_students")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.data_students.sizePolicy().hasHeightForWidth())
        self.data_students.setSizePolicy(sizePolicy3)
        self.data_students.setMinimumSize(QSize(0, 68))
        self.verticalLayout_15 = QVBoxLayout(self.data_students)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(3, 3, 3, 3)
        self.data_label_students = QLabel(self.data_students)
        self.data_label_students.setObjectName(u"data_label_students")
        self.data_label_students.setLayoutDirection(Qt.LeftToRight)
        self.data_label_students.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.data_label_students)


        self.verticalLayout_12.addWidget(self.data_students)

        self.btn_stundents = QWidget(self.students_widget)
        self.btn_stundents.setObjectName(u"btn_stundents")
        self.btn_stundents.setMinimumSize(QSize(0, 20))
        self.verticalLayout_16 = QVBoxLayout(self.btn_stundents)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.goto_students_btn = QToolButton(self.btn_stundents)
        self.goto_students_btn.setObjectName(u"goto_students_btn")
        self.goto_students_btn.setMinimumSize(QSize(15, 15))
        self.goto_students_btn.setMaximumSize(QSize(20, 20))
        icon10 = QIcon()
        icon10.addFile(u":/images/img/goto-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.goto_students_btn.setIcon(icon10)
        self.goto_students_btn.setIconSize(QSize(15, 15))

        self.verticalLayout_16.addWidget(self.goto_students_btn)


        self.verticalLayout_12.addWidget(self.btn_stundents, 0, Qt.AlignRight)


        self.horizontalLayout_6.addWidget(self.students_widget)

        self.profit_widget = QWidget(self.widgets_home)
        self.profit_widget.setObjectName(u"profit_widget")
        sizePolicy2.setHeightForWidth(self.profit_widget.sizePolicy().hasHeightForWidth())
        self.profit_widget.setSizePolicy(sizePolicy2)
        self.profit_widget.setMinimumSize(QSize(283, 141))
        self.profit_widget.setMaximumSize(QSize(339, 169))
        self.profit_widget.setStyleSheet(u"background-color: #47525E;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;")
        self.verticalLayout_26 = QVBoxLayout(self.profit_widget)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(-1, 2, -1, -1)
        self.top_bar_profit = QWidget(self.profit_widget)
        self.top_bar_profit.setObjectName(u"top_bar_profit")
        self.horizontalLayout_9 = QHBoxLayout(self.top_bar_profit)
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, -1, 0)
        self.icon_profit_container = QWidget(self.top_bar_profit)
        self.icon_profit_container.setObjectName(u"icon_profit_container")
        self.icon_profit_container.setMaximumSize(QSize(15, 15))
        self.verticalLayout_23 = QVBoxLayout(self.icon_profit_container)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.icon_profit = QLabel(self.icon_profit_container)
        self.icon_profit.setObjectName(u"icon_profit")
        self.icon_profit.setPixmap(QPixmap(u":/images/img/profit_icon2.png"))
        self.icon_profit.setScaledContents(True)

        self.verticalLayout_23.addWidget(self.icon_profit, 0, Qt.AlignVCenter)


        self.horizontalLayout_9.addWidget(self.icon_profit_container, 0, Qt.AlignVCenter)

        self.title_profit_container = QWidget(self.top_bar_profit)
        self.title_profit_container.setObjectName(u"title_profit_container")
        self.verticalLayout_24 = QVBoxLayout(self.title_profit_container)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.title_profit = QLabel(self.title_profit_container)
        self.title_profit.setObjectName(u"title_profit")

        self.verticalLayout_24.addWidget(self.title_profit)


        self.horizontalLayout_9.addWidget(self.title_profit_container, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_26.addWidget(self.top_bar_profit)

        self.data_profit = QWidget(self.profit_widget)
        self.data_profit.setObjectName(u"data_profit")
        sizePolicy3.setHeightForWidth(self.data_profit.sizePolicy().hasHeightForWidth())
        self.data_profit.setSizePolicy(sizePolicy3)
        self.data_profit.setMinimumSize(QSize(0, 68))
        self.verticalLayout_22 = QVBoxLayout(self.data_profit)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(3, 3, 3, 3)
        self.data_label_profit = QLabel(self.data_profit)
        self.data_label_profit.setObjectName(u"data_label_profit")
        self.data_label_profit.setLayoutDirection(Qt.LeftToRight)
        self.data_label_profit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_22.addWidget(self.data_label_profit)


        self.verticalLayout_26.addWidget(self.data_profit)

        self.btn_profit_container = QWidget(self.profit_widget)
        self.btn_profit_container.setObjectName(u"btn_profit_container")
        self.btn_profit_container.setMinimumSize(QSize(0, 20))
        self.verticalLayout_25 = QVBoxLayout(self.btn_profit_container)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.goto_profit_btn = QToolButton(self.btn_profit_container)
        self.goto_profit_btn.setObjectName(u"goto_profit_btn")
        self.goto_profit_btn.setMinimumSize(QSize(15, 15))
        self.goto_profit_btn.setMaximumSize(QSize(20, 20))
        self.goto_profit_btn.setIcon(icon10)
        self.goto_profit_btn.setIconSize(QSize(15, 15))

        self.verticalLayout_25.addWidget(self.goto_profit_btn)


        self.verticalLayout_26.addWidget(self.btn_profit_container, 0, Qt.AlignRight)


        self.horizontalLayout_6.addWidget(self.profit_widget)

        self.axies_widget = QWidget(self.widgets_home)
        self.axies_widget.setObjectName(u"axies_widget")
        sizePolicy2.setHeightForWidth(self.axies_widget.sizePolicy().hasHeightForWidth())
        self.axies_widget.setSizePolicy(sizePolicy2)
        self.axies_widget.setMinimumSize(QSize(283, 141))
        self.axies_widget.setMaximumSize(QSize(339, 169))
        self.axies_widget.setStyleSheet(u"background-color: #47525E;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;")
        self.verticalLayout_21 = QVBoxLayout(self.axies_widget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, 2, -1, -1)
        self.top_bar_axies = QWidget(self.axies_widget)
        self.top_bar_axies.setObjectName(u"top_bar_axies")
        self.horizontalLayout_8 = QHBoxLayout(self.top_bar_axies)
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, -1, 0)
        self.icon_axies_container = QWidget(self.top_bar_axies)
        self.icon_axies_container.setObjectName(u"icon_axies_container")
        self.icon_axies_container.setMaximumSize(QSize(15, 15))
        self.verticalLayout_18 = QVBoxLayout(self.icon_axies_container)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.icon_axies = QLabel(self.icon_axies_container)
        self.icon_axies.setObjectName(u"icon_axies")
        self.icon_axies.setPixmap(QPixmap(u":/images/img/inventory_icon.png"))
        self.icon_axies.setScaledContents(True)

        self.verticalLayout_18.addWidget(self.icon_axies, 0, Qt.AlignVCenter)


        self.horizontalLayout_8.addWidget(self.icon_axies_container, 0, Qt.AlignVCenter)

        self.title_axies_container = QWidget(self.top_bar_axies)
        self.title_axies_container.setObjectName(u"title_axies_container")
        self.verticalLayout_19 = QVBoxLayout(self.title_axies_container)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.title_axies = QLabel(self.title_axies_container)
        self.title_axies.setObjectName(u"title_axies")

        self.verticalLayout_19.addWidget(self.title_axies)


        self.horizontalLayout_8.addWidget(self.title_axies_container, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_21.addWidget(self.top_bar_axies)

        self.data_axies = QWidget(self.axies_widget)
        self.data_axies.setObjectName(u"data_axies")
        sizePolicy3.setHeightForWidth(self.data_axies.sizePolicy().hasHeightForWidth())
        self.data_axies.setSizePolicy(sizePolicy3)
        self.data_axies.setMinimumSize(QSize(0, 68))
        self.verticalLayout_17 = QVBoxLayout(self.data_axies)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(3, 3, 3, 3)
        self.data_label_axies = QLabel(self.data_axies)
        self.data_label_axies.setObjectName(u"data_label_axies")
        self.data_label_axies.setLayoutDirection(Qt.LeftToRight)
        self.data_label_axies.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_17.addWidget(self.data_label_axies)


        self.verticalLayout_21.addWidget(self.data_axies)

        self.btn_axies = QWidget(self.axies_widget)
        self.btn_axies.setObjectName(u"btn_axies")
        self.btn_axies.setMinimumSize(QSize(0, 20))
        self.verticalLayout_20 = QVBoxLayout(self.btn_axies)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.goto_axies_btn = QToolButton(self.btn_axies)
        self.goto_axies_btn.setObjectName(u"goto_axies_btn")
        self.goto_axies_btn.setMinimumSize(QSize(15, 15))
        self.goto_axies_btn.setMaximumSize(QSize(20, 20))
        self.goto_axies_btn.setIcon(icon10)
        self.goto_axies_btn.setIconSize(QSize(15, 15))

        self.verticalLayout_20.addWidget(self.goto_axies_btn)


        self.verticalLayout_21.addWidget(self.btn_axies, 0, Qt.AlignRight)


        self.horizontalLayout_6.addWidget(self.axies_widget)


        self.verticalLayout_11.addWidget(self.widgets_home)

        self.graphics_home = QWidget(self.home_container)
        self.graphics_home.setObjectName(u"graphics_home")
        self.graphics_home.setMinimumSize(QSize(0, 200))
        self.graphics_home.setStyleSheet(u"")
        self.graphics_layout = QHBoxLayout(self.graphics_home)
        self.graphics_layout.setSpacing(180)
        self.graphics_layout.setObjectName(u"graphics_layout")
        self.graphics_layout.setContentsMargins(95, 25, 95, 25)

        self.verticalLayout_11.addWidget(self.graphics_home)

        self.information_home = QWidget(self.home_container)
        self.information_home.setObjectName(u"information_home")
        self.information_home.setMinimumSize(QSize(0, 150))
        self.information_home.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.information_home)


        self.verticalLayout_9.addWidget(self.home_container)

        self.pages_container.addWidget(self.home_page)
        self.profit_page = QWidget()
        self.profit_page.setObjectName(u"profit_page")
        self.verticalLayout_10 = QVBoxLayout(self.profit_page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.profit_page)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_10.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pages_container.addWidget(self.profit_page)
        self.students_page = QWidget()
        self.students_page.setObjectName(u"students_page")
        self.verticalLayout_27 = QVBoxLayout(self.students_page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_3 = QLabel(self.students_page)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_27.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pages_container.addWidget(self.students_page)
        self.inventory_page = QWidget()
        self.inventory_page.setObjectName(u"inventory_page")
        self.verticalLayout_28 = QVBoxLayout(self.inventory_page)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_4 = QLabel(self.inventory_page)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_28.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pages_container.addWidget(self.inventory_page)
        self.mail_page = QWidget()
        self.mail_page.setObjectName(u"mail_page")
        self.verticalLayout_29 = QVBoxLayout(self.mail_page)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_5 = QLabel(self.mail_page)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_29.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pages_container.addWidget(self.mail_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayout_30 = QVBoxLayout(self.settings_page)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_6 = QLabel(self.settings_page)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_30.addWidget(self.label_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pages_container.addWidget(self.settings_page)

        self.verticalLayout_3.addWidget(self.pages_container)


        self.verticalLayout_2.addWidget(self.content_container)


        self.horizontalLayout.addWidget(self.right_container)


        self.verticalLayout.addWidget(self.container)

        MainWindow.setCentralWidget(self.bg)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"TOGGLE", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"      Home", None))
        self.btn_profit.setText(QCoreApplication.translate("MainWindow", u"      Profit", None))
        self.btn_students.setText(QCoreApplication.translate("MainWindow", u"      Students", None))
        self.btn_inventory.setText(QCoreApplication.translate("MainWindow", u"      Inventory", None))
        self.btn_mail.setText(QCoreApplication.translate("MainWindow", u"      Mail", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"     Settings", None))
        self.logo_label.setText("")
        self.title1_label.setText(QCoreApplication.translate("MainWindow", u"AXIE", None))
        self.title2_label.setText(QCoreApplication.translate("MainWindow", u"MANAGER", None))
        self.btn_minimize.setText(QCoreApplication.translate("MainWindow", u"MINIMIZE", None))
        self.btn_expand.setText(QCoreApplication.translate("MainWindow", u"EXPAND", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.icon_students.setText("")
        self.title_students.setText(QCoreApplication.translate("MainWindow", u"STUDENTS", None))
        self.data_label_students.setText(QCoreApplication.translate("MainWindow", u"999", None))
        self.goto_students_btn.setText("")
        self.icon_profit.setText("")
        self.title_profit.setText(QCoreApplication.translate("MainWindow", u"MONTHLY PROFIT", None))
        self.data_label_profit.setText(QCoreApplication.translate("MainWindow", u"999", None))
        self.goto_profit_btn.setText("")
        self.icon_axies.setText("")
        self.title_axies.setText(QCoreApplication.translate("MainWindow", u"AXIES", None))
        self.data_label_axies.setText(QCoreApplication.translate("MainWindow", u"999", None))
        self.goto_axies_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"profit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"students", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"inventory", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"mail", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"settings", None))
    # retranslateUi

