# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc
import resources_rc
import resources_rc
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1096, 857)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 16777215))
        Form.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        Form.setAcceptDrops(False)
        Form.setStyleSheet(u"QWidget#Form {\n"
"	background-image: url(:/images/images/background.png);\n"
"    width:100%;\n"
"    height:100%;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(256, 256))
        self.label_3.setStyleSheet(u"background-image: url(:/icons/icons/hdd.ico) no-repeat center center;\n"
"")

        self.horizontalLayout_5.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 120))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(40)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: white;")
        self.label_4.setTextFormat(Qt.TextFormat.RichText)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 10, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_7)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: white;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.username = QLineEdit(self.groupBox)
        self.username.setObjectName(u"username")
        self.username.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(13, 13, 13);\n"
"    /*color: rgb(41, 41, 41);*/\n"
"	color: white;\n"
"    border: 3px solid #262626;\n"
"    height: 50px;\n"
"    width: 500px;\n"
"    border-radius: 25px;\n"
"	padding: 0 10%;\n"
"}\n"
"QLineEdit::placeholderText {\n"
"    font-size: 16px;\n"
"}")

        self.horizontalLayout.addWidget(self.username)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: white;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.password = QLineEdit(self.groupBox)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(526, 0))
        self.password.setMaximumSize(QSize(500, 16777215))
        self.password.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(13, 13, 13);\n"
"    /*color: rgb(41, 41, 41);*/\n"
"	color: white;\n"
"    border: 3px solid #262626;\n"
"    height: 50px;\n"
"    width: 500px;\n"
"    border-radius: 25px;\n"
"	padding: 0 10%;\n"
"}\n"
"QLineEdit::placeholderText {\n"
"    font-size: 16px;\n"
"}")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_2.addWidget(self.password)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.login_btn = QPushButton(self.groupBox)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(0, 0))
        self.login_btn.setMaximumSize(QSize(100, 50))
        font2 = QFont()
        font2.setPointSize(12)
        self.login_btn.setFont(font2)
        self.login_btn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.login_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.register_2 = QPushButton(self.groupBox)
        self.register_2.setObjectName(u"register_2")
        self.register_2.setMaximumSize(QSize(16777215, 16777215))
        self.register_2.setFont(font1)
        self.register_2.setStyleSheet(u"QPushButton#register_2 {\n"
"	color: #1a0dab;\n"
"	color: white;\n"
"	background-color:transparent;\n"
"}\n"
"QPushButton#register_2:pressed {\n"
"	color: #681DA8;\n"
"	background-color:transparent;\n"
"}\n"
"QPushButton#register_2:hover {\n"
"	text-decoration: underline;\n"
"	background-color:transparent;\n"
"}")

        self.horizontalLayout_4.addWidget(self.register_2)

        self.forget_password = QPushButton(self.groupBox)
        self.forget_password.setObjectName(u"forget_password")
        self.forget_password.setMaximumSize(QSize(16777215, 16777215))
        self.forget_password.setFont(font1)
        self.forget_password.setStyleSheet(u"QPushButton#forget_password {\n"
"	color: #1a0dab;\n"
"	color: white;\n"
"	background-color:transparent;\n"
"}\n"
"QPushButton#forget_password:pressed {\n"
"	color: #681DA8;\n"
"	background-color:transparent;\n"
"}\n"
"QPushButton#forget_password:hover {\n"
"	text-decoration: underline;\n"
"	background-color:transparent;\n"
"}")

        self.horizontalLayout_4.addWidget(self.forget_password)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Login", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6b22\u8fce\u8bbf\u95eeH.D.D System", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d\uff1a", None))
        self.username.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6    \u7801\uff1a", None))
        self.password.setInputMask("")
        self.password.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"\u767b\u5165", None))
        self.register_2.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.forget_password.setText(QCoreApplication.translate("Form", u"\u5fd8\u8bb0\u5bc6\u7801", None))
    # retranslateUi

