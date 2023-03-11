# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\phorn\Documents\Code\anikator\gui\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 279)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainTab = QtWidgets.QTabWidget(self.centralwidget)
        self.mainTab.setGeometry(QtCore.QRect(-10, 0, 741, 241))
        self.mainTab.setObjectName("mainTab")
        self.intro_tab = QtWidgets.QWidget()
        self.intro_tab.setEnabled(True)
        self.intro_tab.setFocusPolicy(QtCore.Qt.NoFocus)
        self.intro_tab.setObjectName("intro_tab")
        self.intro_label = QtWidgets.QLabel(self.intro_tab)
        self.intro_label.setGeometry(QtCore.QRect(30, 40, 711, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.intro_label.setFont(font)
        self.intro_label.setObjectName("intro_label")
        self.intro_button_continue = QtWidgets.QPushButton(self.intro_tab)
        self.intro_button_continue.setGeometry(QtCore.QRect(620, 90, 93, 28))
        self.intro_button_continue.setObjectName("intro_button_continue")
        self.mainTab.addTab(self.intro_tab, "")
        self.questions_tab = QtWidgets.QWidget()
        self.questions_tab.setObjectName("questions_tab")
        self.no_button = QtWidgets.QPushButton(self.questions_tab)
        self.no_button.setGeometry(QtCore.QRect(290, 20, 31, 28))
        self.no_button.setObjectName("no_button")
        self.candidates_label = QtWidgets.QLabel(self.questions_tab)
        self.candidates_label.setGeometry(QtCore.QRect(450, 0, 71, 16))
        self.candidates_label.setObjectName("candidates_label")
        self.output_label = QtWidgets.QLabel(self.questions_tab)
        self.output_label.setGeometry(QtCore.QRect(20, 15, 221, 31))
        self.output_label.setFrameShape(QtWidgets.QFrame.Box)
        self.output_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_label.setObjectName("output_label")
        self.yes_button = QtWidgets.QPushButton(self.questions_tab)
        self.yes_button.setGeometry(QtCore.QRect(250, 20, 31, 28))
        self.yes_button.setObjectName("yes_button")
        self.candidates = QtWidgets.QLineEdit(self.questions_tab)
        self.candidates.setGeometry(QtCore.QRect(430, 20, 113, 22))
        self.candidates.setObjectName("candidates")
        self.mainTab.addTab(self.questions_tab, "")
        self.guessed_tab = QtWidgets.QWidget()
        self.guessed_tab.setObjectName("guessed_tab")
        self.mainTab.addTab(self.guessed_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 26))
        self.menubar.setObjectName("menubar")
        self.menuAnikator = QtWidgets.QMenu(self.menubar)
        self.menuAnikator.setObjectName("menuAnikator")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAnikator.menuAction())

        self.retranslateUi(MainWindow)
        self.mainTab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Anikator Window"))
        self.intro_label.setText(_translate("MainWindow", "Piensa en un animal, e intentaré adivinarlo. Pulsar el boton para continuar."))
        self.intro_button_continue.setText(_translate("MainWindow", "Continuar"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.intro_tab), _translate("MainWindow", "Tab 1"))
        self.no_button.setText(_translate("MainWindow", "No"))
        self.candidates_label.setText(_translate("MainWindow", "Candidates"))
        self.output_label.setText(_translate("MainWindow", "---"))
        self.yes_button.setText(_translate("MainWindow", "Si"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.questions_tab), _translate("MainWindow", "Tab 2"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.guessed_tab), _translate("MainWindow", "Página"))
        self.menuAnikator.setTitle(_translate("MainWindow", "Anikator"))
