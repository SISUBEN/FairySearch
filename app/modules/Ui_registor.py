# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registor.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from ..assets import resources_rc

class Ui_Registor(object):
    def setupUi(self, Registor):
        if not Registor.objectName():
            Registor.setObjectName(u"Registor")
        Registor.resize(1388, 879)
        Registor.setMinimumSize(QSize(1388, 879))
        Registor.setMaximumSize(QSize(1388, 879))
        Registor.setStyleSheet(u"QWidget#Registor {\n"
"	background-image: url(:/images/images/reg.png);\n"
"    background-position: center;\n"
"    background-size: contain;\n"
"}")
        self.layoutWidget = QWidget(Registor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(440, 430, 508, 261))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.username = QLineEdit(self.layoutWidget)
        self.username.setObjectName(u"username")
        self.username.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(13, 13, 13);\n"
"    /* color: rgb(41, 41, 41); */\n"
"	color: white;\n"
"    border: 3px solid #262626;\n"
"    height: 50px;\n"
"    width: 500px;\n"
"    border-radius: 25px;\n"
"}\n"
"QLineEdit::placeholderText {\n"
"    font-size: 16px;\n"
"}")

        self.verticalLayout.addWidget(self.username)

        self.password_2 = QLineEdit(self.layoutWidget)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(13, 13, 13);\n"
"    /*color: rgb(41, 41, 41);*/\n"
"	color: white;\n"
"    border: 3px solid #262626;\n"
"    height: 50px;\n"
"    width: 500px;\n"
"    border-radius: 25px;\n"
"}\n"
"QLineEdit::placeholderText {\n"
"    font-size: 16px;\n"
"}")

        self.verticalLayout.addWidget(self.password_2)

        self.password = QLineEdit(self.layoutWidget)
        self.password.setObjectName(u"password")
        self.password.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(13, 13, 13);\n"
"    /*color: rgb(41, 41, 41);*/\n"
"	color: white;\n"
"    border: 3px solid #262626;\n"
"    height: 50px;\n"
"    width: 500px;\n"
"    border-radius: 25px;\n"
"}\n"
"QLineEdit::placeholderText {\n"
"    font-size: 16px;\n"
"}")

        self.verticalLayout.addWidget(self.password)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.register_btn = QPushButton(self.layoutWidget)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setMinimumSize(QSize(271, 71))
        self.register_btn.setMaximumSize(QSize(271, 71))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.register_btn.setFont(font)
        self.register_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 3px solid #262626;\n"
"    height: 50px;\n"
"    width: 500px;\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6c100;\n"
"    color: black;\n"
"    border: 5px solid #a6c100;\n"
"}")
        self.register_btn.setCheckable(False)
        self.register_btn.setAutoRepeat(False)

        self.horizontalLayout_2.addWidget(self.register_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Registor)

        QMetaObject.connectSlotsByName(Registor)
    # setupUi

    def retranslateUi(self, Registor):
        Registor.setWindowTitle(QCoreApplication.translate("Registor", u"Form", None))
        self.username.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("Registor", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d", None))
        self.password_2.setText("")
        self.password_2.setPlaceholderText(QCoreApplication.translate("Registor", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("Registor", u"\u8bf7\u518d\u6b21\u8f93\u5165\u5bc6\u7801", None))
        self.register_btn.setText(QCoreApplication.translate("Registor", u"\u6ce8\u518c", None))
    # retranslateUi

