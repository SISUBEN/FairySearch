# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)
from .assets import resources_rc

class Ui_Profile(object):
    def setupUi(self, Profile, username, uid):
        if not Profile.objectName():
            Profile.setObjectName(u"Profile")
        Profile.resize(1053, 601)
        Profile.setMinimumSize(QSize(1053, 601))
        Profile.setStyleSheet(u"QWidget#Profile {\n"
"	background-image: url(:/images/images/profile.png);\n"
"	background-size:cover;\n"
"}")
        self.link_like_btn = QPushButton(Profile)
        self.changeAvatar.setObjectName(u"link_like_btn")
        self.link_like_btn.setStyleSheet(u"QPushButton#link_like_btn {\n"
        "	color: #1a0dab;\n"
        "	color: white;\n"
        "	background-color:transparent;\n"
        "}\n"
        "QPushButton#link_like_btn:pressed {\n"
        "	color: #681DA8;\n"
        "	background-color:transparent;\n"
        "}\n"
        "QPushButton#link_like_btn:hover {\n"
        "	text-decoration: underline;\n"
        "	background-color:transparent;\n"
        "}")
        
        self.username = QLabel(Profile)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(140, 410, 151, 41))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.username.setFont(font)
        self.username.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"\n"
"}")
        self.uid = QLabel(Profile)
        self.uid.setObjectName(u"uid")
        self.uid.setGeometry(QRect(80, 480, 211, 31))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.uid.setFont(font1)
        self.uid.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"\n"
"}")
        self.username_3 = QLabel(Profile)
        self.username_3.setObjectName(u"username_3")
        self.username_3.setGeometry(QRect(360, 70, 151, 41))
        self.username_3.setFont(font)
        self.username_3.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"\n"
"}")
        self.changeAvatar = QPushButton(Profile)
        self.changeAvatar.setObjectName(u"changeAvatar")
        self.changeAvatar.setGeometry(QRect(80, 410, 41, 41))
        self.changeAvatar.setStyleSheet(u"QPushButton {\n"
"	background: transparent\n"
"}")
        self.tableWidget = QTableWidget(Profile)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(365, 121, 601, 401))

        self.retranslateUi(Profile, username, uid)

        QMetaObject.connectSlotsByName(Profile)
    # setupUi

    def retranslateUi(self, Profile, username, uid):
        Profile.setWindowTitle(QCoreApplication.translate("Profile", u"Profile", None))
        self.username.setText(QCoreApplication.translate("Profile", f"{username}", None))
        self.uid.setText(QCoreApplication.translate("Profile", f"UID: {uid}", None))
        self.username_3.setText(QCoreApplication.translate("Profile", u"\u641c\u7d22\u5386\u53f2\uff1a", None))
        self.changeAvatar.setText("")
    # retranslateUi

