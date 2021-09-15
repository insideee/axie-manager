# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_loadingJlMakO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import src.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 250)
        self.bg = QWidget(MainWindow)
        self.bg.setObjectName(u"bg")
        self.bg.setStyleSheet(u"background-color: rgb(48, 56, 64);\n"
"border-radius: 10px")
        self.verticalLayout = QVBoxLayout(self.bg)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QWidget(self.bg)
        self.container.setObjectName(u"container")
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_container = QWidget(self.container)
        self.title_container.setObjectName(u"title_container")
        self.horizontalLayout = QHBoxLayout(self.title_container)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_1 = QLabel(self.title_container)
        self.title_1.setObjectName(u"title_1")
        self.title_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.title_1)

        self.title_2 = QLabel(self.title_container)
        self.title_2.setObjectName(u"title_2")

        self.horizontalLayout.addWidget(self.title_2)


        self.verticalLayout_2.addWidget(self.title_container, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.progress_container = QWidget(self.container)
        self.progress_container.setObjectName(u"progress_container")
        self.verticalLayout_3 = QVBoxLayout(self.progress_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, -1, -1, -1)
        self.info_label = QLabel(self.progress_container)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_3.addWidget(self.info_label)

        self.progress = QProgressBar(self.progress_container)
        self.progress.setObjectName(u"progress")
        self.progress.setMinimumSize(QSize(500, 30))
        self.progress.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(115, 115, 115);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(230, 76, 60)\n"
"}")
        self.progress.setValue(10)

        self.verticalLayout_3.addWidget(self.progress)


        self.verticalLayout_2.addWidget(self.progress_container, 0, Qt.AlignHCenter)

        self.widget_3 = QWidget(self.container)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.container)

        MainWindow.setCentralWidget(self.bg)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_1.setText(QCoreApplication.translate("MainWindow", u"AXIE", None))
        self.title_2.setText(QCoreApplication.translate("MainWindow", u"MANAGER", None))
        self.info_label.setText(QCoreApplication.translate("MainWindow", u"text", None))
    # retranslateUi

