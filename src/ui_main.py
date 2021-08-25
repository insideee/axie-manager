# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainUKImVn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1201, 680)
        MainWindow.setMinimumSize(QSize(1200, 680))
        MainWindow.setStyleSheet(u"border: 0px solid;")
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
        self.menu_container.setStyleSheet(u"background-color: #1E2226;\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 0px;")
        self.verticalLayout_4 = QVBoxLayout(self.menu_container)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 8, 5, 8)
        self.top_menu = QWidget(self.menu_container)
        self.top_menu.setObjectName(u"top_menu")
        self.top_menu.setMinimumSize(QSize(0, 0))
        self.top_menu.setStyleSheet(u"QToolButton {\n"
"	background-color: #1E2226;\n"
"	border-radius: 0px;\n"
"	margin-left: 15px;\n"
"	}\n"
"\n"
"QToolButton:hover {\n"
"	\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.top_menu)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 0)
        self.btn_toggle = QToolButton(self.top_menu)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setMinimumSize(QSize(0, 30))
        self.btn_toggle.setStyleSheet(u"QToolButton {\n"
"	background-color: #1E2226;\n"
"	margin-left: 3px\n"
"	}\n"
"\n"
"QToolButton:hover {\n"
"	background-color: #1E2226\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/img/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)

        self.verticalLayout_5.addWidget(self.btn_toggle)

        self.btn_home = QToolButton(self.top_menu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(140, 30))
        self.btn_home.setFocusPolicy(Qt.NoFocus)
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/images/img/home_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon1)
        self.btn_home.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.btn_home.setAutoRaise(False)

        self.verticalLayout_5.addWidget(self.btn_home)

        self.btn_profit = QToolButton(self.top_menu)
        self.btn_profit.setObjectName(u"btn_profit")
        sizePolicy1.setHeightForWidth(self.btn_profit.sizePolicy().hasHeightForWidth())
        self.btn_profit.setSizePolicy(sizePolicy1)
        self.btn_profit.setMinimumSize(QSize(140, 30))
        icon2 = QIcon()
        icon2.addFile(u":/images/img/profit_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_profit.setIcon(icon2)
        self.btn_profit.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_5.addWidget(self.btn_profit)

        self.btn_students = QToolButton(self.top_menu)
        self.btn_students.setObjectName(u"btn_students")
        sizePolicy1.setHeightForWidth(self.btn_students.sizePolicy().hasHeightForWidth())
        self.btn_students.setSizePolicy(sizePolicy1)
        self.btn_students.setMinimumSize(QSize(140, 30))
        icon3 = QIcon()
        icon3.addFile(u":/images/img/user_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_students.setIcon(icon3)
        self.btn_students.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_5.addWidget(self.btn_students)

        self.btn_inventory = QToolButton(self.top_menu)
        self.btn_inventory.setObjectName(u"btn_inventory")
        sizePolicy1.setHeightForWidth(self.btn_inventory.sizePolicy().hasHeightForWidth())
        self.btn_inventory.setSizePolicy(sizePolicy1)
        self.btn_inventory.setMinimumSize(QSize(140, 30))
        icon4 = QIcon()
        icon4.addFile(u":/images/img/inventory_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_inventory.setIcon(icon4)
        self.btn_inventory.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_5.addWidget(self.btn_inventory)

        self.btn_mail = QToolButton(self.top_menu)
        self.btn_mail.setObjectName(u"btn_mail")
        sizePolicy1.setHeightForWidth(self.btn_mail.sizePolicy().hasHeightForWidth())
        self.btn_mail.setSizePolicy(sizePolicy1)
        self.btn_mail.setMinimumSize(QSize(140, 30))
        icon5 = QIcon()
        icon5.addFile(u":/images/img/mail_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_mail.setIcon(icon5)
        self.btn_mail.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_5.addWidget(self.btn_mail)

        self.btn_home.raise_()
        self.btn_toggle.raise_()
        self.btn_profit.raise_()
        self.btn_students.raise_()
        self.btn_inventory.raise_()
        self.btn_mail.raise_()

        self.verticalLayout_4.addWidget(self.top_menu, 0, Qt.AlignTop)

        self.bottom_menu = QWidget(self.menu_container)
        self.bottom_menu.setObjectName(u"bottom_menu")
        self.bottom_menu.setMinimumSize(QSize(0, 0))
        self.bottom_menu.setMaximumSize(QSize(16777215, 120))
        self.bottom_menu.setStyleSheet(u"QToolButton {\n"
"	background-color: #1E2226;\n"
"	border-radius: 0px;\n"
"	margin-left: 15px;\n"
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
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.label = QLabel(self.home_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 190, 58, 18))
        self.pages_container.addWidget(self.home_page)
        self.profit_page = QWidget()
        self.profit_page.setObjectName(u"profit_page")
        self.label_2 = QLabel(self.profit_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 240, 58, 18))
        self.pages_container.addWidget(self.profit_page)
        self.students_page = QWidget()
        self.students_page.setObjectName(u"students_page")
        self.label_3 = QLabel(self.students_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 270, 58, 18))
        self.pages_container.addWidget(self.students_page)
        self.inventory_page = QWidget()
        self.inventory_page.setObjectName(u"inventory_page")
        self.label_4 = QLabel(self.inventory_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 250, 58, 18))
        self.pages_container.addWidget(self.inventory_page)
        self.mail_page = QWidget()
        self.mail_page.setObjectName(u"mail_page")
        self.label_5 = QLabel(self.mail_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(130, 170, 58, 18))
        self.pages_container.addWidget(self.mail_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.label_6 = QLabel(self.settings_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(140, 160, 58, 18))
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
        self.btn_mail.setText(QCoreApplication.translate("MainWindow", u"     Mail", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"     Settings", None))
        self.logo_label.setText("")
        self.title1_label.setText(QCoreApplication.translate("MainWindow", u"AXIE", None))
        self.title2_label.setText(QCoreApplication.translate("MainWindow", u"MANAGER", None))
        self.btn_minimize.setText(QCoreApplication.translate("MainWindow", u"MINIMIZE", None))
        self.btn_expand.setText(QCoreApplication.translate("MainWindow", u"EXPAND", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"profit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"students", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"inventory", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"mail", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"settings", None))
    # retranslateUi

