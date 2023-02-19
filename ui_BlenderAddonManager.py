# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BlenderAddonManager.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTabWidget,
    QTableView, QVBoxLayout, QWidget)

class Ui_BlenderAddonManager(object):
    def setupUi(self, BlenderAddonManager):
        if not BlenderAddonManager.objectName():
            BlenderAddonManager.setObjectName(u"BlenderAddonManager")
        BlenderAddonManager.resize(1211, 905)
        self.verticalLayout = QVBoxLayout(BlenderAddonManager)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_9 = QFrame(BlenderAddonManager)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_9)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.tabWidget_3 = QTabWidget(self.frame_9)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_20 = QWidget()
        self.tab_20.setObjectName(u"tab_20")
        self.verticalLayout_293 = QVBoxLayout(self.tab_20)
        self.verticalLayout_293.setObjectName(u"verticalLayout_293")
        self.frame_13 = QFrame(self.tab_20)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_13)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_2 = QLabel(self.frame_13)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)

        self.verticalLayout_43.addWidget(self.label_2)

        self.tableView_git = QTableView(self.frame_13)
        self.tableView_git.setObjectName(u"tableView_git")
        self.tableView_git.setSortingEnabled(True)
        self.tableView_git.horizontalHeader().setDefaultSectionSize(200)
        self.tableView_git.horizontalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_43.addWidget(self.tableView_git)

        self.frame_1195 = QFrame(self.frame_13)
        self.frame_1195.setObjectName(u"frame_1195")
        self.frame_1195.setFrameShape(QFrame.StyledPanel)
        self.frame_1195.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_662 = QHBoxLayout(self.frame_1195)
        self.horizontalLayout_662.setObjectName(u"horizontalLayout_662")
        self.horizontalLayout_662.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_pull_gitaddon_selected = QPushButton(self.frame_1195)
        self.pushButton_pull_gitaddon_selected.setObjectName(u"pushButton_pull_gitaddon_selected")
        self.pushButton_pull_gitaddon_selected.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_662.addWidget(self.pushButton_pull_gitaddon_selected)

        self.pushButton_pull_gitaddons = QPushButton(self.frame_1195)
        self.pushButton_pull_gitaddons.setObjectName(u"pushButton_pull_gitaddons")
        self.pushButton_pull_gitaddons.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_662.addWidget(self.pushButton_pull_gitaddons)


        self.verticalLayout_43.addWidget(self.frame_1195)


        self.verticalLayout_293.addWidget(self.frame_13)

        self.tabWidget_3.addTab(self.tab_20, "")
        self.tab_21 = QWidget()
        self.tab_21.setObjectName(u"tab_21")
        self.verticalLayout_294 = QVBoxLayout(self.tab_21)
        self.verticalLayout_294.setObjectName(u"verticalLayout_294")
        self.frame_38 = QFrame(self.tab_21)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_38)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_3 = QLabel(self.frame_38)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_45.addWidget(self.label_3)

        self.tableView_init = QTableView(self.frame_38)
        self.tableView_init.setObjectName(u"tableView_init")
        self.tableView_init.setSortingEnabled(True)
        self.tableView_init.horizontalHeader().setDefaultSectionSize(200)
        self.tableView_init.horizontalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_45.addWidget(self.tableView_init)


        self.verticalLayout_294.addWidget(self.frame_38)

        self.tabWidget_3.addTab(self.tab_21, "")
        self.tab_22 = QWidget()
        self.tab_22.setObjectName(u"tab_22")
        self.verticalLayout_295 = QVBoxLayout(self.tab_22)
        self.verticalLayout_295.setObjectName(u"verticalLayout_295")
        self.frame_37 = QFrame(self.tab_22)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_37)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_4 = QLabel(self.frame_37)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_44.addWidget(self.label_4)

        self.tableView_py = QTableView(self.frame_37)
        self.tableView_py.setObjectName(u"tableView_py")
        self.tableView_py.setSortingEnabled(True)
        self.tableView_py.horizontalHeader().setDefaultSectionSize(200)
        self.tableView_py.horizontalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_44.addWidget(self.tableView_py)


        self.verticalLayout_295.addWidget(self.frame_37)

        self.tabWidget_3.addTab(self.tab_22, "")
        self.tab_126 = QWidget()
        self.tab_126.setObjectName(u"tab_126")
        self.horizontalLayout_663 = QHBoxLayout(self.tab_126)
        self.horizontalLayout_663.setObjectName(u"horizontalLayout_663")
        self.frame_1196 = QFrame(self.tab_126)
        self.frame_1196.setObjectName(u"frame_1196")
        self.frame_1196.setFrameShape(QFrame.StyledPanel)
        self.frame_1196.setFrameShadow(QFrame.Raised)
        self.verticalLayout_741 = QVBoxLayout(self.frame_1196)
        self.verticalLayout_741.setObjectName(u"verticalLayout_741")
        self.label_22 = QLabel(self.frame_1196)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.verticalLayout_741.addWidget(self.label_22)

        self.tableView_bak = QTableView(self.frame_1196)
        self.tableView_bak.setObjectName(u"tableView_bak")
        self.tableView_bak.setSortingEnabled(True)
        self.tableView_bak.horizontalHeader().setDefaultSectionSize(200)
        self.tableView_bak.horizontalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_741.addWidget(self.tableView_bak)


        self.horizontalLayout_663.addWidget(self.frame_1196)

        self.tabWidget_3.addTab(self.tab_126, "")

        self.verticalLayout_41.addWidget(self.tabWidget_3)

        self.frame_91 = QFrame(self.frame_9)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 4px;\n"
"	color : white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:rgb(99, 60, 245);\n"
"}")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.pushButton_search_addons = QPushButton(self.frame_91)
        self.pushButton_search_addons.setObjectName(u"pushButton_search_addons")
        self.pushButton_search_addons.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_78.addWidget(self.pushButton_search_addons)

        self.pushButton_move_unused_addons = QPushButton(self.frame_91)
        self.pushButton_move_unused_addons.setObjectName(u"pushButton_move_unused_addons")
        self.pushButton_move_unused_addons.setMinimumSize(QSize(0, 30))
        self.pushButton_move_unused_addons.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(227, 90, 90);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(104, 24, 242);\n"
"}")

        self.horizontalLayout_78.addWidget(self.pushButton_move_unused_addons)


        self.verticalLayout_41.addWidget(self.frame_91)


        self.verticalLayout.addWidget(self.frame_9)


        self.retranslateUi(BlenderAddonManager)

        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(BlenderAddonManager)
    # setupUi

    def retranslateUi(self, BlenderAddonManager):
        BlenderAddonManager.setWindowTitle(QCoreApplication.translate("BlenderAddonManager", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("BlenderAddonManager", u"Git Addon", None))
        self.pushButton_pull_gitaddon_selected.setText(QCoreApplication.translate("BlenderAddonManager", u"Pull Selected Git Addon", None))
        self.pushButton_pull_gitaddons.setText(QCoreApplication.translate("BlenderAddonManager", u"Pull Git Addons", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_20), QCoreApplication.translate("BlenderAddonManager", u"Git", None))
        self.label_3.setText(QCoreApplication.translate("BlenderAddonManager", u"Folder Addon", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_21), QCoreApplication.translate("BlenderAddonManager", u"Folder", None))
        self.label_4.setText(QCoreApplication.translate("BlenderAddonManager", u"Py Addon", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_22), QCoreApplication.translate("BlenderAddonManager", u"Py", None))
        self.label_22.setText(QCoreApplication.translate("BlenderAddonManager", u"Py Addon", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_126), QCoreApplication.translate("BlenderAddonManager", u"Bak", None))
        self.pushButton_search_addons.setText(QCoreApplication.translate("BlenderAddonManager", u"Search Addons", None))
        self.pushButton_move_unused_addons.setText(QCoreApplication.translate("BlenderAddonManager", u"Move Unused Addons", None))
    # retranslateUi

