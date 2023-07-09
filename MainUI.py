# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLineEdit, QListView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTreeView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(514, 469)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 9, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.buttonGroupFrame = QFrame(self.centralwidget)
        self.buttonGroupFrame.setObjectName(u"buttonGroupFrame")
        self.verticalLayout_3 = QVBoxLayout(self.buttonGroupFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 8, 0, 8)
        self.allButton = QPushButton(self.buttonGroupFrame)
        self.allButton.setObjectName(u"allButton")

        self.verticalLayout_3.addWidget(self.allButton)

        self.shareButton = QPushButton(self.buttonGroupFrame)
        self.shareButton.setObjectName(u"shareButton")

        self.verticalLayout_3.addWidget(self.shareButton)


        self.verticalLayout.addWidget(self.buttonGroupFrame)

        self.treeFrame = QFrame(self.centralwidget)
        self.treeFrame.setObjectName(u"treeFrame")
        self.verticalLayout_2 = QVBoxLayout(self.treeFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 1, 8, 1)
        self.treeView = QTreeView(self.treeFrame)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setUniformRowHeights(True)
        self.treeView.setAnimated(True)
        self.treeView.header().setVisible(False)

        self.verticalLayout_2.addWidget(self.treeView)

        self.homeButton = QPushButton(self.treeFrame)
        self.homeButton.setObjectName(u"homeButton")

        self.verticalLayout_2.addWidget(self.homeButton)


        self.verticalLayout.addWidget(self.treeFrame)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setMovement(QListView.Static)
        self.listView.setResizeMode(QListView.Adjust)
        self.listView.setSpacing(-1)
        self.listView.setViewMode(QListView.IconMode)
        self.listView.setUniformItemSizes(True)
        self.listView.setWordWrap(True)
        self.listView.setItemAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.listView)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 4)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.hrefInput = QFrame(self.centralwidget)
        self.hrefInput.setObjectName(u"hrefInput")
        self.topLayout = QHBoxLayout(self.hrefInput)
        self.topLayout.setObjectName(u"topLayout")
        self.topLayout.setContentsMargins(-1, 1, -1, -1)
        self.pathInput = QLineEdit(self.hrefInput)
        self.pathInput.setObjectName(u"pathInput")

        self.topLayout.addWidget(self.pathInput)

        self.searchInput = QLineEdit(self.hrefInput)
        self.searchInput.setObjectName(u"searchInput")

        self.topLayout.addWidget(self.searchInput)

        self.searchButton = QPushButton(self.hrefInput)
        self.searchButton.setObjectName(u"searchButton")

        self.topLayout.addWidget(self.searchButton)

        self.topLayout.setStretch(0, 2)
        self.topLayout.setStretch(1, 1)

        self.gridLayout.addWidget(self.hrefInput, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 514, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.allButton.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.shareButton.setText(QCoreApplication.translate("MainWindow", u"Shared", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pathInput.setText("")
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
    # retranslateUi

