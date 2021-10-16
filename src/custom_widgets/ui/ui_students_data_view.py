# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_students_data_viewMeVbgb.ui'
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

class Ui_dataViewWidget(object):
    def setupUi(self, dataViewWidget):
        if not dataViewWidget.objectName():
            dataViewWidget.setObjectName(u"dataViewWidget")
        dataViewWidget.resize(891, 540)
        dataViewWidget.setMinimumSize(QSize(0, 540))
        self.verticalLayout = QVBoxLayout(dataViewWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.displayDataFrame = QWidget(dataViewWidget)
        self.displayDataFrame.setObjectName(u"displayDataFrame")
        self.displayDataFrame.setMinimumSize(QSize(0, 0))
        self.displayDataFrame.setStyleSheet(u"QWidget{background-color: #47525E;\n"
"border: 1px solid #61676D;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.displayDataFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.displayDataFrame)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 30))
        self.header.setMaximumSize(QSize(16777215, 30))
        self.header.setStyleSheet(u"QLabel{border: 0px}\n"
"QWidget{\n"
"border-top-left-radius: 10px;\n"
"border-bottom-right-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;}")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.dataHeaderContainer = QWidget(self.header)
        self.dataHeaderContainer.setObjectName(u"dataHeaderContainer")
        self.dataHeaderContainer.setMinimumSize(QSize(695, 0))
        self.dataHeaderContainer.setStyleSheet(u"QWidget{border: 0px;\n"
"border-radius:0px}")
        self.horizontalLayout_2 = QHBoxLayout(self.dataHeaderContainer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 0, 1, 0)
        self.nameLabel = QLabel(self.dataHeaderContainer)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setMinimumSize(QSize(223, 0))
        self.nameLabel.setMaximumSize(QSize(223, 16777215))

        self.horizontalLayout_2.addWidget(self.nameLabel)

        self.roninLabel = QLabel(self.dataHeaderContainer)
        self.roninLabel.setObjectName(u"roninLabel")
        self.roninLabel.setMinimumSize(QSize(260, 0))
        self.roninLabel.setMaximumSize(QSize(9999999, 16777215))

        self.horizontalLayout_2.addWidget(self.roninLabel)

        self.emailLabel = QLabel(self.dataHeaderContainer)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setMinimumSize(QSize(186, 0))
        self.emailLabel.setMaximumSize(QSize(186, 16777215))

        self.horizontalLayout_2.addWidget(self.emailLabel)


        self.horizontalLayout.addWidget(self.dataHeaderContainer, 0, Qt.AlignVCenter)

        self.slpHeaderDataContainer = QWidget(self.header)
        self.slpHeaderDataContainer.setObjectName(u"slpHeaderDataContainer")
        self.slpHeaderDataContainer.setMaximumSize(QSize(190, 16777215))
        self.slpHeaderDataContainer.setStyleSheet(u"QWidget{border: 0px;\n"
"border-radius:0px}")
        self.horizontalLayout_3 = QHBoxLayout(self.slpHeaderDataContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 1, 0)
        self.slpGoalLabel = QLabel(self.slpHeaderDataContainer)
        self.slpGoalLabel.setObjectName(u"slpGoalLabel")
        self.slpGoalLabel.setMinimumSize(QSize(95, 0))
        self.slpGoalLabel.setMaximumSize(QSize(95, 16777215))

        self.horizontalLayout_3.addWidget(self.slpGoalLabel)

        self.slpTodayLabel = QLabel(self.slpHeaderDataContainer)
        self.slpTodayLabel.setObjectName(u"slpTodayLabel")
        self.slpTodayLabel.setMinimumSize(QSize(94, 0))
        self.slpTodayLabel.setMaximumSize(QSize(94, 16777215))
        self.slpTodayLabel.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.slpTodayLabel)


        self.horizontalLayout.addWidget(self.slpHeaderDataContainer, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.header)

        self.dataContainer = QWidget(self.displayDataFrame)
        self.dataContainer.setObjectName(u"dataContainer")
        self.dataContainer.setMinimumSize(QSize(0, 0))
        self.dataContainer.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.dataContainer)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.dataContainer, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.displayDataFrame)

        self.bottomFrame = QWidget(dataViewWidget)
        self.bottomFrame.setObjectName(u"bottomFrame")
        self.bottomFrame.setMinimumSize(QSize(0, 30))
        self.bottomFrame.setMaximumSize(QSize(16777215, 30))
        self.verticalLayout_4 = QVBoxLayout(self.bottomFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnContainer = QWidget(self.bottomFrame)
        self.btnContainer.setObjectName(u"btnContainer")
        self.btnContainer.setMinimumSize(QSize(80, 0))
        self.btnContainer.setMaximumSize(QSize(80, 16777215))
        self.btnContainer.setStyleSheet(u"QToolButton{\n"
"background-color: #47525E;\n"
"border: 1px solid #61676D\n"
"}\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.btnContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.leftBtnFrame = QWidget(self.btnContainer)
        self.leftBtnFrame.setObjectName(u"leftBtnFrame")
        self.verticalLayout_5 = QVBoxLayout(self.leftBtnFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.leftBtn = QToolButton(self.leftBtnFrame)
        self.leftBtn.setObjectName(u"leftBtn")
        self.leftBtn.setMinimumSize(QSize(20, 20))
        self.leftBtn.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/images/img/left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.leftBtn.setIcon(icon)
        self.leftBtn.setIconSize(QSize(15, 15))
        self.leftBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout_5.addWidget(self.leftBtn, 0, Qt.AlignVCenter)


        self.horizontalLayout_4.addWidget(self.leftBtnFrame)

        self.indiceFrame = QWidget(self.btnContainer)
        self.indiceFrame.setObjectName(u"indiceFrame")
        self.verticalLayout_7 = QVBoxLayout(self.indiceFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.indiceLabel = QLabel(self.indiceFrame)
        self.indiceLabel.setObjectName(u"indiceLabel")

        self.verticalLayout_7.addWidget(self.indiceLabel)


        self.horizontalLayout_4.addWidget(self.indiceFrame)

        self.rightBtnFrame = QWidget(self.btnContainer)
        self.rightBtnFrame.setObjectName(u"rightBtnFrame")
        self.verticalLayout_6 = QVBoxLayout(self.rightBtnFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.rigthBtn = QToolButton(self.rightBtnFrame)
        self.rigthBtn.setObjectName(u"rigthBtn")
        self.rigthBtn.setMinimumSize(QSize(20, 20))
        self.rigthBtn.setMaximumSize(QSize(20, 20))
        icon1 = QIcon()
        icon1.addFile(u":/images/img/right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rigthBtn.setIcon(icon1)

        self.verticalLayout_6.addWidget(self.rigthBtn, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout_4.addWidget(self.rightBtnFrame)


        self.verticalLayout_4.addWidget(self.btnContainer, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.bottomFrame)


        self.retranslateUi(dataViewWidget)

        QMetaObject.connectSlotsByName(dataViewWidget)
    # setupUi

    def retranslateUi(self, dataViewWidget):
        dataViewWidget.setWindowTitle(QCoreApplication.translate("dataViewWidget", u"Form", None))
        self.nameLabel.setText(QCoreApplication.translate("dataViewWidget", u"Name", None))
        self.roninLabel.setText(QCoreApplication.translate("dataViewWidget", u"Ronin", None))
        self.emailLabel.setText(QCoreApplication.translate("dataViewWidget", u"Email", None))
        self.slpGoalLabel.setText(QCoreApplication.translate("dataViewWidget", u"SLP Goal", None))
        self.slpTodayLabel.setText(QCoreApplication.translate("dataViewWidget", u"SLP Today", None))
        self.leftBtn.setText("")
        self.indiceLabel.setText("")
        self.rigthBtn.setText("")
    # retranslateUi

