# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_students_data_viewKImTvX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
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
        dataViewWidget.resize(1218, 953)
        dataViewWidget.setMinimumSize(QSize(0, 540))
        self.horizontalLayout_5 = QHBoxLayout(dataViewWidget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.leaderboardContent = QWidget(dataViewWidget)
        self.leaderboardContent.setObjectName(u"leaderboardContent")
        self.leaderboardContent.setMinimumSize(QSize(270, 0))
        self.leaderboardContent.setMaximumSize(QSize(316, 16777215))
        self.leaderboardContent.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.leaderboardContent)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.leaderboardFrame = QWidget(self.leaderboardContent)
        self.leaderboardFrame.setObjectName(u"leaderboardFrame")
        self.leaderboardFrame.setMinimumSize(QSize(0, 350))
        self.leaderboardFrame.setMaximumSize(QSize(370, 470))
        self.leaderboardFrame.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.leaderboardFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.board_bg = QWidget(self.leaderboardFrame)
        self.board_bg.setObjectName(u"board_bg")
        self.board_bg.setMinimumSize(QSize(0, 400))
        self.board_bg.setMaximumSize(QSize(16777215, 470))
        self.board_bg.setStyleSheet(u"QWidget{background-color: #47525E;\n"
"border: 1px solid #61676D;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.board_bg)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.board_header = QWidget(self.board_bg)
        self.board_header.setObjectName(u"board_header")
        self.board_header.setMinimumSize(QSize(0, 30))
        self.board_header.setMaximumSize(QSize(316, 30))
        self.board_header.setStyleSheet(u"QWidget{border: 0px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-right-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.board_header)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.labelFrame = QWidget(self.board_header)
        self.labelFrame.setObjectName(u"labelFrame")
        self.labelFrame.setMinimumSize(QSize(160, 0))
        self.verticalLayout_14 = QVBoxLayout(self.labelFrame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(6, 0, 0, 0)
        self.leaderLabel = QLabel(self.labelFrame)
        self.leaderLabel.setObjectName(u"leaderLabel")

        self.verticalLayout_14.addWidget(self.leaderLabel)


        self.horizontalLayout_7.addWidget(self.labelFrame)


        self.verticalLayout_9.addWidget(self.board_header)

        self.firstPlaceFrame = QWidget(self.board_bg)
        self.firstPlaceFrame.setObjectName(u"firstPlaceFrame")
        self.firstPlaceFrame.setMinimumSize(QSize(0, 240))
        self.firstPlaceFrame.setMaximumSize(QSize(316, 240))
        self.firstPlaceFrame.setStyleSheet(u"QWidget{border: 0px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.firstPlaceFrame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.firstPlace = QFrame(self.firstPlaceFrame)
        self.firstPlace.setObjectName(u"firstPlace")
        self.firstPlace.setFrameShape(QFrame.StyledPanel)
        self.firstPlace.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.firstPlace)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_13.addWidget(self.firstPlace)


        self.verticalLayout_9.addWidget(self.firstPlaceFrame)

        self.othersPlaceFrame = QWidget(self.board_bg)
        self.othersPlaceFrame.setObjectName(u"othersPlaceFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.othersPlaceFrame.sizePolicy().hasHeightForWidth())
        self.othersPlaceFrame.setSizePolicy(sizePolicy)
        self.othersPlaceFrame.setMinimumSize(QSize(0, 130))
        self.othersPlaceFrame.setMaximumSize(QSize(316, 200))
        self.othersPlaceFrame.setStyleSheet(u"QWidget{border: 0px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-right-radius: 10px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.othersPlaceFrame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.secondPlace = QWidget(self.othersPlaceFrame)
        self.secondPlace.setObjectName(u"secondPlace")
        self.verticalLayout_11 = QVBoxLayout(self.secondPlace)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_6.addWidget(self.secondPlace)

        self.thirdPlace = QWidget(self.othersPlaceFrame)
        self.thirdPlace.setObjectName(u"thirdPlace")
        self.verticalLayout_12 = QVBoxLayout(self.thirdPlace)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_6.addWidget(self.thirdPlace)


        self.verticalLayout_9.addWidget(self.othersPlaceFrame)


        self.verticalLayout_8.addWidget(self.board_bg)


        self.verticalLayout_3.addWidget(self.leaderboardFrame)

        self.btnFrame = QWidget(self.leaderboardContent)
        self.btnFrame.setObjectName(u"btnFrame")
        self.btnFrame.setMinimumSize(QSize(0, 0))
        self.btnFrame.setMaximumSize(QSize(16777215, 99999))
        self.verticalLayout_10 = QVBoxLayout(self.btnFrame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, -1, 20, -1)
        self.addBtn = QPushButton(self.btnFrame)
        self.addBtn.setObjectName(u"addBtn")
        self.addBtn.setStyleSheet(u"QPushButton{background-color: #47525E;\n"
"border-radius: 5px;\n"
"color:#FFFFFF}")

        self.verticalLayout_10.addWidget(self.addBtn)


        self.verticalLayout_3.addWidget(self.btnFrame)


        self.horizontalLayout_5.addWidget(self.leaderboardContent)

        self.dataFrame = QWidget(dataViewWidget)
        self.dataFrame.setObjectName(u"dataFrame")
        self.dataFrame.setMinimumSize(QSize(240, 0))
        self.dataFrame.setMaximumSize(QSize(999999, 16777215))
        self.verticalLayout = QVBoxLayout(self.dataFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.displayDataFrame = QWidget(self.dataFrame)
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
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 0)
        self.header_new = QWidget(self.displayDataFrame)
        self.header_new.setObjectName(u"header_new")
        self.header_new.setMinimumSize(QSize(0, 30))
        self.header_new.setMaximumSize(QSize(16777215, 30))
        self.header_new.setStyleSheet(u"QWidget{border: 0px;\n"
"border-bottom: 1px solid #61676D;}")
        self.horizontalLayout_11 = QHBoxLayout(self.header_new)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(2, 0, 1, 1)
        self.dataHeaderContainer = QWidget(self.header_new)
        self.dataHeaderContainer.setObjectName(u"dataHeaderContainer")
        self.dataHeaderContainer.setMinimumSize(QSize(350, 0))
        self.dataHeaderContainer.setStyleSheet(u"QWidget{border: 0px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-right-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;}")
        self.horizontalLayout_9 = QHBoxLayout(self.dataHeaderContainer)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(4, 0, 0, 1)
        self.nameLabel = QLabel(self.dataHeaderContainer)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setMinimumSize(QSize(100, 0))
        self.nameLabel.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_9.addWidget(self.nameLabel)

        self.roninLabel = QLabel(self.dataHeaderContainer)
        self.roninLabel.setObjectName(u"roninLabel")
        self.roninLabel.setMinimumSize(QSize(100, 0))
        self.roninLabel.setMaximumSize(QSize(9999999, 16777215))

        self.horizontalLayout_9.addWidget(self.roninLabel)

        self.mmrLabel = QLabel(self.dataHeaderContainer)
        self.mmrLabel.setObjectName(u"mmrLabel")
        self.mmrLabel.setMinimumSize(QSize(60, 0))
        self.mmrLabel.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_9.addWidget(self.mmrLabel)

        self.rankLabel = QLabel(self.dataHeaderContainer)
        self.rankLabel.setObjectName(u"rankLabel")
        self.rankLabel.setMinimumSize(QSize(80, 0))
        self.rankLabel.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_9.addWidget(self.rankLabel)

        self.roninLabel.raise_()
        self.nameLabel.raise_()
        self.mmrLabel.raise_()
        self.rankLabel.raise_()

        self.horizontalLayout_11.addWidget(self.dataHeaderContainer)

        self.slpDataContainer = QWidget(self.header_new)
        self.slpDataContainer.setObjectName(u"slpDataContainer")
        self.slpDataContainer.setMinimumSize(QSize(160, 0))
        self.slpDataContainer.setMaximumSize(QSize(400, 16777215))
        self.slpDataContainer.setStyleSheet(u"QWidget{border:0px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;}")
        self.horizontalLayout_10 = QHBoxLayout(self.slpDataContainer)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 1, 1)
        self.totalSlpLabel = QLabel(self.slpDataContainer)
        self.totalSlpLabel.setObjectName(u"totalSlpLabel")
        self.totalSlpLabel.setMinimumSize(QSize(80, 0))
        self.totalSlpLabel.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_10.addWidget(self.totalSlpLabel)

        self.averageLabel = QLabel(self.slpDataContainer)
        self.averageLabel.setObjectName(u"averageLabel")
        self.averageLabel.setMinimumSize(QSize(30, 0))
        self.averageLabel.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_10.addWidget(self.averageLabel)

        self.slpGoalLabel = QLabel(self.slpDataContainer)
        self.slpGoalLabel.setObjectName(u"slpGoalLabel")
        self.slpGoalLabel.setMinimumSize(QSize(30, 0))
        self.slpGoalLabel.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_10.addWidget(self.slpGoalLabel)

        self.slpTodayLabel = QLabel(self.slpDataContainer)
        self.slpTodayLabel.setObjectName(u"slpTodayLabel")
        self.slpTodayLabel.setMinimumSize(QSize(30, 0))
        self.slpTodayLabel.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_10.addWidget(self.slpTodayLabel)


        self.horizontalLayout_11.addWidget(self.slpDataContainer)


        self.verticalLayout_2.addWidget(self.header_new)

        self.dataContainer = QWidget(self.displayDataFrame)
        self.dataContainer.setObjectName(u"dataContainer")
        self.dataContainer.setMinimumSize(QSize(0, 0))
        self.dataContainer.setStyleSheet(u"")
        self.layoutDataWidgets = QVBoxLayout(self.dataContainer)
        self.layoutDataWidgets.setSpacing(0)
        self.layoutDataWidgets.setObjectName(u"layoutDataWidgets")
        self.layoutDataWidgets.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.dataContainer, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.displayDataFrame)

        self.bottomFrame = QWidget(self.dataFrame)
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


        self.horizontalLayout_5.addWidget(self.dataFrame)


        self.retranslateUi(dataViewWidget)

        QMetaObject.connectSlotsByName(dataViewWidget)
    # setupUi

    def retranslateUi(self, dataViewWidget):
        dataViewWidget.setWindowTitle(QCoreApplication.translate("dataViewWidget", u"Form", None))
        self.leaderLabel.setText(QCoreApplication.translate("dataViewWidget", u"Leaderboard", None))
        self.addBtn.setText(QCoreApplication.translate("dataViewWidget", u"add", None))
        self.nameLabel.setText(QCoreApplication.translate("dataViewWidget", u"Name", None))
        self.roninLabel.setText(QCoreApplication.translate("dataViewWidget", u"Ronin", None))
        self.mmrLabel.setText(QCoreApplication.translate("dataViewWidget", u"MMR", None))
        self.rankLabel.setText(QCoreApplication.translate("dataViewWidget", u"Rank", None))
        self.totalSlpLabel.setText(QCoreApplication.translate("dataViewWidget", u"Total SLP", None))
        self.averageLabel.setText(QCoreApplication.translate("dataViewWidget", u"avg SLP", None))
        self.slpGoalLabel.setText(QCoreApplication.translate("dataViewWidget", u"SLP Goal", None))
        self.slpTodayLabel.setText(QCoreApplication.translate("dataViewWidget", u"SLP Today", None))
        self.leftBtn.setText("")
        self.indiceLabel.setText("")
        self.rigthBtn.setText("")
    # retranslateUi

