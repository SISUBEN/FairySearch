# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(340, 212)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 130, 151, 41))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 141, 41))
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 141, 51))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 20, 141, 21))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(160, 70, 141, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Login", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Password:", None))
    # retranslateUi

