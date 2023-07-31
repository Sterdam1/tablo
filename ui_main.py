# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(502, 900)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spred:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(200,0,100,1),  stop:1 rgba(81,0,255,1));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_team_1 = QLabel(self.centralwidget)
        self.label_team_1.setObjectName(u"label_team_1")
        self.label_team_1.setGeometry(QRect(70, 200, 111, 41))
        font = QFont()
        font.setFamilies([u"Source Code Pro Semibold"])
        font.setPointSize(18)
        font.setBold(True)
        self.label_team_1.setFont(font)
        self.label_team_1.setStyleSheet(u"border-radius: 10px;\n"
"background:rgba(40,230,255,0.42);\n"
"border: 2px solid rgba(40,230,255, 0.60);\n"
"")
        self.label_team_1.setTextFormat(Qt.MarkdownText)
        self.label_team_1.setAlignment(Qt.AlignCenter)
        self.label_team_2 = QLabel(self.centralwidget)
        self.label_team_2.setObjectName(u"label_team_2")
        self.label_team_2.setGeometry(QRect(320, 200, 111, 41))
        self.label_team_2.setFont(font)
        self.label_team_2.setStyleSheet(u"border-radius: 10px;\n"
"background:rgba(255,0,0,0.42);\n"
"border: 2px solid rgba(255,0,0,0.42);")
        self.label_team_2.setTextFormat(Qt.MarkdownText)
        self.label_team_2.setAlignment(Qt.AlignCenter)
        self.btn_team1 = QPushButton(self.centralwidget)
        self.btn_team1.setObjectName(u"btn_team1")
        self.btn_team1.setGeometry(QRect(70, 260, 111, 111))
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro Semibold"])
        font1.setPointSize(25)
        font1.setBold(True)
        self.btn_team1.setFont(font1)
        self.btn_team1.setStyleSheet(u"border-radius: 10px;\n"
"background:rgba(40,230,255,0.42);\n"
"border: 2px solid rgba(40,230,255, 0.60);")
        self.btn_team2 = QPushButton(self.centralwidget)
        self.btn_team2.setObjectName(u"btn_team2")
        self.btn_team2.setGeometry(QRect(320, 260, 111, 111))
        font2 = QFont()
        font2.setFamilies([u"Source Code Pro Semibold"])
        font2.setPointSize(25)
        self.btn_team2.setFont(font2)
        self.btn_team2.setStyleSheet(u"border-radius: 10px;\n"
"background:rgba(255,0,0,0.42);\n"
"border: 2px solid rgba(255,0,0,0.42);")
        self.btn_sets1 = QPushButton(self.centralwidget)
        self.btn_sets1.setObjectName(u"btn_sets1")
        self.btn_sets1.setGeometry(QRect(200, 200, 41, 41))
        self.btn_sets1.setFont(font1)
        self.btn_sets1.setStyleSheet(u"border-radius: 10px;\n"
"background:rgba(40,230,255,0.42);\n"
"border: 2px solid rgba(40,230,255, 0.60);")
        self.btn_sets2 = QPushButton(self.centralwidget)
        self.btn_sets2.setObjectName(u"btn_sets2")
        self.btn_sets2.setGeometry(QRect(260, 200, 41, 41))
        self.btn_sets2.setFont(font1)
        self.btn_sets2.setStyleSheet(u"border-radius: 10px;\n"
"background:rgba(255,0,0,0.42);\n"
"border: 2px solid rgba(255,0,0,0.42);")
        self.btn_reset = QPushButton(self.centralwidget)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setGeometry(QRect(370, 30, 101, 61))
        font3 = QFont()
        font3.setFamilies([u"Source Code Pro Semibold"])
        font3.setPointSize(15)
        font3.setBold(True)
        self.btn_reset.setFont(font3)
        self.btn_reset.setStyleSheet(u"border-radius: 10px;\n"
"background:rgba(255,0,0,0.42);\n"
"border: 2px solid rgba(255,0,0,0.42);")
        self.btn_undo = QPushButton(self.centralwidget)
        self.btn_undo.setObjectName(u"btn_undo")
        self.btn_undo.setGeometry(QRect(30, 30, 101, 61))
        self.btn_undo.setFont(font3)
        self.btn_undo.setStyleSheet(u"border-radius: 10px;\n"
"background:rgba(40,230,255,0.42);\n"
"border: 2px solid rgba(40,230,255, 0.60);\n"
"")     
        font4 = QFont()
        font4.setFamilies([u"Source Code Pro Semibold"])
        font4.setPointSize(10)
        font4.setBold(True)
        
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setFont(font4)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(170, 30, 161, 61))
        self.comboBox.setFont(font3)
        self.comboBox.setMaxVisibleItems(2)
        self.comboBox.setInsertPolicy(QComboBox.InsertAtTop)
        self.comboBox.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.comboBox.setStyleSheet(u"background: rgba(160,0,180, 0.42);\n"
"border: 2px solid rgba(200, 0, 180, 0.6);\n"
"border-radius: 5px 5px 5px 5px;\n"
"padding: 10px; combobox-popup: 0;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Volleyball score", None))
        self.label_team_1.setText(QCoreApplication.translate("MainWindow", u"Team 1", None))
        self.label_team_2.setText(QCoreApplication.translate("MainWindow", u"Team 2", None))
        self.btn_team1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_team2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_sets1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_sets2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_undo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
    # retranslateUi

