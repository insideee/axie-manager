# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainpiOPWt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
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
        self.verticalLayout_4.setContentsMargins(5, 8, 5, 8)
        self.top_menu = QWidget(self.menu_container)
        self.top_menu.setObjectName(u"top_menu")
        self.top_menu.setMinimumSize(QSize(0, 0))
        self.top_menu.setStyleSheet(u"QPushButton {\n"
"	background-color: #1E2226;\n"
"	border-radius: 0px\n"
"	}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #E64C3C\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.top_menu)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 0)
        self.btn_toggle = QPushButton(self.top_menu)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setMinimumSize(QSize(0, 30))
        self.btn_toggle.setStyleSheet(u"QPushButton {\n"
"	background-color: #1E2226;\n"
"	}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #1E2226\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_toggle)

        self.btn_home = QPushButton(self.top_menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))

        self.verticalLayout_5.addWidget(self.btn_home)

        self.btn_profit = QPushButton(self.top_menu)
        self.btn_profit.setObjectName(u"btn_profit")
        self.btn_profit.setMinimumSize(QSize(0, 30))

        self.verticalLayout_5.addWidget(self.btn_profit)

        self.btn_students = QPushButton(self.top_menu)
        self.btn_students.setObjectName(u"btn_students")
        self.btn_students.setMinimumSize(QSize(0, 30))

        self.verticalLayout_5.addWidget(self.btn_students)

        self.btn_inventory = QPushButton(self.top_menu)
        self.btn_inventory.setObjectName(u"btn_inventory")
        self.btn_inventory.setMinimumSize(QSize(0, 30))

        self.verticalLayout_5.addWidget(self.btn_inventory)

        self.btn_mail = QPushButton(self.top_menu)
        self.btn_mail.setObjectName(u"btn_mail")
        self.btn_mail.setMinimumSize(QSize(0, 30))

        self.verticalLayout_5.addWidget(self.btn_mail)


        self.verticalLayout_4.addWidget(self.top_menu, 0, Qt.AlignTop)

        self.bottom_menu = QWidget(self.menu_container)
        self.bottom_menu.setObjectName(u"bottom_menu")
        self.bottom_menu.setMinimumSize(QSize(0, 0))
        self.bottom_menu.setMaximumSize(QSize(16777215, 120))
        self.bottom_menu.setStyleSheet(u"QPushButton {\n"
"	background-color: #1E2226;\n"
"	border-radius: 0px\n"
"	}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #1E2226\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.bottom_menu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 10)
        self.btn_settings = QPushButton(self.bottom_menu)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(0, 30))

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
        self.logo_contant.setMinimumSize(QSize(25, 25))
        self.logo_contant.setMaximumSize(QSize(25, 99999))
        self.verticalLayout_8 = QVBoxLayout(self.logo_contant)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.logo_label = QLabel(self.logo_contant)
        self.logo_label.setObjectName(u"logo_label")

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

        self.horizontalLayout_4.addWidget(self.title1_label)

        self.title2_label = QLabel(self.title_content)
        self.title2_label.setObjectName(u"title2_label")

        self.horizontalLayout_4.addWidget(self.title2_label)


        self.horizontalLayout_3.addWidget(self.title_content, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.title_window_container)

        self.btn_content = QWidget(self.top_bar)
        self.btn_content.setObjectName(u"btn_content")
        self.horizontalLayout_5 = QHBoxLayout(self.btn_content)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 10, 0)
        self.btn_minimize = QPushButton(self.btn_content)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(25, 0))
        self.btn_minimize.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_expand = QPushButton(self.btn_content)
        self.btn_expand.setObjectName(u"btn_expand")
        self.btn_expand.setMinimumSize(QSize(25, 0))
        self.btn_expand.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_5.addWidget(self.btn_expand)

        self.btn_exit = QPushButton(self.btn_content)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMinimumSize(QSize(25, 0))
        self.btn_exit.setMaximumSize(QSize(30, 16777215))

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
        self.pages_container.addWidget(self.home_page)
        self.profit_page = QWidget()
        self.profit_page.setObjectName(u"profit_page")
        self.pages_container.addWidget(self.profit_page)
        self.students_page = QWidget()
        self.students_page.setObjectName(u"students_page")
        self.pages_container.addWidget(self.students_page)
        self.inventory_page = QWidget()
        self.inventory_page.setObjectName(u"inventory_page")
        self.pages_container.addWidget(self.inventory_page)
        self.mail_page = QWidget()
        self.mail_page.setObjectName(u"mail_page")
        self.pages_container.addWidget(self.mail_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
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
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_profit.setText(QCoreApplication.translate("MainWindow", u"PROFIT", None))
        self.btn_students.setText(QCoreApplication.translate("MainWindow", u"STUDENTS", None))
        self.btn_inventory.setText(QCoreApplication.translate("MainWindow", u"INVENTORY", None))
        self.btn_mail.setText(QCoreApplication.translate("MainWindow", u"MAIL", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.logo_label.setText(QCoreApplication.translate("MainWindow", u"logo_label", None))
        self.title1_label.setText(QCoreApplication.translate("MainWindow", u"AXIE", None))
        self.title2_label.setText(QCoreApplication.translate("MainWindow", u"MANAGER", None))
        self.btn_minimize.setText(QCoreApplication.translate("MainWindow", u"MINIMIZE", None))
        self.btn_expand.setText(QCoreApplication.translate("MainWindow", u"EXPAND", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
    # retranslateUi

