# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designhAtcCO.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 500)
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/res/main.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"\n"
"QTextEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"	font: 700 12pt \"Hack\";\n"
"}\n"
"QPushButton:hover {\n"
"    border-color: #090;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 4px solid #090;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:checked {\n"
"	color: white;\n"
"	background-color: #090;\n"
"	border: 2px solid black;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #090;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background-color: gray;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: black;\n"
"    width: 16px;\n"
"    border-radius:8px;\n"
"    margin-top: -5px;\n"
"    margin-bottom: -5px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    background-color: transparent;\n"
"    height: 7px;\n"
"}\n"
"QLabel {\n"
"	font: 500 11pt \"Ubuntu\";\n"
"}\n"
"QSpinBox {\n"
"    border: 2px solid gray;\n"
"   "
                        " border-radius: 5px;\n"
"    background: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border-color: #009900;\n"
"}")
        MainWindow.setIconSize(QSize(32, 32))
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        icon1 = QIcon()
        icon1.addFile(u":/icons/res/about.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionabout.setIcon(icon1)
        font1 = QFont()
        font1.setFamilies([u"Hack NF"])
        self.actionabout.setFont(font1)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon2 = QIcon()
        icon2.addFile(u":/icons/res/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setFont(font1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Original_text = QVBoxLayout()
        self.Original_text.setObjectName(u"Original_text")
        self.input_text_lbl = QLabel(self.centralwidget)
        self.input_text_lbl.setObjectName(u"input_text_lbl")

        self.Original_text.addWidget(self.input_text_lbl)

        self.chars_label = QLabel(self.centralwidget)
        self.chars_label.setObjectName(u"chars_label")

        self.Original_text.addWidget(self.chars_label)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        font2 = QFont()
        font2.setFamilies([u"Fira Code Medium"])
        font2.setPointSize(10)
        self.textEdit.setFont(font2)
        self.textEdit.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.textEdit.setFrameShape(QFrame.StyledPanel)
        self.textEdit.setFrameShadow(QFrame.Sunken)
        self.textEdit.setLineWidth(1)

        self.Original_text.addWidget(self.textEdit)


        self.verticalLayout.addLayout(self.Original_text)

        self.Decrypte_text = QVBoxLayout()
        self.Decrypte_text.setObjectName(u"Decrypte_text")
        self.outpu_text_lbl = QLabel(self.centralwidget)
        self.outpu_text_lbl.setObjectName(u"outpu_text_lbl")

        self.Decrypte_text.addWidget(self.outpu_text_lbl)

        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setFont(font2)
        self.textEdit_2.setReadOnly(True)

        self.Decrypte_text.addWidget(self.textEdit_2)


        self.verticalLayout.addLayout(self.Decrypte_text)

        self.Buttons = QHBoxLayout()
        self.Buttons.setObjectName(u"Buttons")
        self.decrypt_btn = QPushButton(self.centralwidget)
        self.decrypt_btn.setObjectName(u"decrypt_btn")
        self.decrypt_btn.setMinimumSize(QSize(0, 80))
        self.decrypt_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/res/lock_open_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.decrypt_btn.setIcon(icon3)
        self.decrypt_btn.setIconSize(QSize(32, 32))
        self.decrypt_btn.setCheckable(True)
        self.decrypt_btn.setChecked(True)

        self.Buttons.addWidget(self.decrypt_btn)

        self.encrypt_btn = QPushButton(self.centralwidget)
        self.encrypt_btn.setObjectName(u"encrypt_btn")
        self.encrypt_btn.setMinimumSize(QSize(0, 80))
        self.encrypt_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/res/lock_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.encrypt_btn.setIcon(icon4)
        self.encrypt_btn.setIconSize(QSize(32, 32))
        self.encrypt_btn.setCheckable(True)

        self.Buttons.addWidget(self.encrypt_btn)

        self.brute_btn = QPushButton(self.centralwidget)
        self.brute_btn.setObjectName(u"brute_btn")
        self.brute_btn.setMinimumSize(QSize(0, 80))
        self.brute_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        iconThemeName = u"zoom-in"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u":/icons/res/swap_horizontal_circle_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.brute_btn.setIcon(icon5)
        self.brute_btn.setIconSize(QSize(32, 32))

        self.Buttons.addWidget(self.brute_btn)

        self.open_btn = QPushButton(self.centralwidget)
        self.open_btn.setObjectName(u"open_btn")
        self.open_btn.setMinimumSize(QSize(0, 60))
        self.open_btn.setMaximumSize(QSize(80, 16777215))
        self.open_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/res/open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_btn.setIcon(icon6)
        self.open_btn.setIconSize(QSize(32, 32))

        self.Buttons.addWidget(self.open_btn)

        self.copy_btn = QPushButton(self.centralwidget)
        self.copy_btn.setObjectName(u"copy_btn")
        self.copy_btn.setMinimumSize(QSize(0, 60))
        self.copy_btn.setMaximumSize(QSize(80, 16777215))
        self.copy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/res/copy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.copy_btn.setIcon(icon7)
        self.copy_btn.setIconSize(QSize(32, 32))

        self.Buttons.addWidget(self.copy_btn)

        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(0, 60))
        self.save_btn.setMaximumSize(QSize(80, 16777215))
        self.save_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/res/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_btn.setIcon(icon8)
        self.save_btn.setIconSize(QSize(32, 32))

        self.Buttons.addWidget(self.save_btn)


        self.verticalLayout.addLayout(self.Buttons)

        self.ShiftKey = QHBoxLayout()
        self.ShiftKey.setObjectName(u"ShiftKey")
        self.key_lbl = QLabel(self.centralwidget)
        self.key_lbl.setObjectName(u"key_lbl")
        self.key_lbl.setEnabled(True)
        font3 = QFont()
        font3.setFamilies([u"Ubuntu"])
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        self.key_lbl.setFont(font3)
        self.key_lbl.setAlignment(Qt.AlignCenter)

        self.ShiftKey.addWidget(self.key_lbl)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider.setMinimum(-50)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setPageStep(5)
        self.horizontalSlider.setValue(13)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider.setTickInterval(0)

        self.ShiftKey.addWidget(self.horizontalSlider)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(100, 50))
        font4 = QFont()
        font4.setFamilies([u"Hack NF"])
        font4.setPointSize(18)
        font4.setBold(True)
        self.spinBox.setFont(font4)
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox.setAccelerated(False)
        self.spinBox.setMinimum(-50)
        self.spinBox.setMaximum(50)
        self.spinBox.setValue(13)

        self.ShiftKey.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.ShiftKey)

        self.Author = QHBoxLayout()
        self.Author.setObjectName(u"Author")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 15))
        self.label.setFont(font3)
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setOpenExternalLinks(True)

        self.Author.addWidget(self.label)


        self.verticalLayout.addLayout(self.Author)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 850, 20))
        self.menuBar.setFont(font1)
        self.menuBar.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuAbout = QMenu(self.menuBar)
        self.menuAbout.setObjectName(u"menuAbout")
        font5 = QFont()
        font5.setFamilies([u"Hack NF"])
        font5.setPointSize(9)
        self.menuAbout.setFont(font5)
        self.menuAbout.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuAbout.setTearOffEnabled(False)
        self.menuAbout.setSeparatorsCollapsible(False)
        self.menuAbout.setToolTipsVisible(False)
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setFont(font1)
        self.menuFile.setCursor(QCursor(Qt.PointingHandCursor))
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.menuAbout.addAction(self.actionabout)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Caesar cipher: encode and decode", None))
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(QCoreApplication.translate("MainWindow", u"Easter egg here!", None))
#endif // QT_CONFIG(whatsthis)
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"about", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.input_text_lbl.setText(QCoreApplication.translate("MainWindow", u"Original text", None))
        self.chars_label.setText(QCoreApplication.translate("MainWindow", u"Characters:", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Fira Code Medium'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Uryyb grnz!</p></body></html>", None))
        self.outpu_text_lbl.setText(QCoreApplication.translate("MainWindow", u"Encrypted/Decrypted text", None))
        self.decrypt_btn.setText(QCoreApplication.translate("MainWindow", u"DECRYPT", None))
        self.encrypt_btn.setText(QCoreApplication.translate("MainWindow", u"ENCRYPT", None))
        self.brute_btn.setText(QCoreApplication.translate("MainWindow", u"BRUTEFORCE", None))
#if QT_CONFIG(tooltip)
        self.open_btn.setToolTip(QCoreApplication.translate("MainWindow", u"File open", None))
#endif // QT_CONFIG(tooltip)
        self.open_btn.setText("")
#if QT_CONFIG(tooltip)
        self.copy_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Copy to clipboard", None))
#endif // QT_CONFIG(tooltip)
        self.copy_btn.setText("")
#if QT_CONFIG(tooltip)
        self.save_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Save to a file", None))
#endif // QT_CONFIG(tooltip)
        self.save_btn.setText("")
        self.key_lbl.setText(QCoreApplication.translate("MainWindow", u"Shift key (positive or negative integer):", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Author: [Exited3n](https://t.me/exited3n)", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

