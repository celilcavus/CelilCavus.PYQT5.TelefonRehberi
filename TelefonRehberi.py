# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 441)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.txtAd = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAd.setObjectName("txtAd")
        self.verticalLayout.addWidget(self.txtAd)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.txtSoyad = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSoyad.setObjectName("txtSoyad")
        self.verticalLayout.addWidget(self.txtSoyad)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.txtTelNo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTelNo.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txtTelNo.setInputMask("")
        self.txtTelNo.setObjectName("txtTelNo")
        self.verticalLayout.addWidget(self.txtTelNo)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnEkle = QtWidgets.QPushButton(self.centralwidget)
        self.btnEkle.setObjectName("btnEkle")
        self.horizontalLayout_2.addWidget(self.btnEkle)
        self.btnSil = QtWidgets.QPushButton(self.centralwidget)
        self.btnSil.setObjectName("btnSil")
        self.horizontalLayout_2.addWidget(self.btnSil)
        self.btnGuncelle = QtWidgets.QPushButton(self.centralwidget)
        self.btnGuncelle.setObjectName("btnGuncelle")
        self.horizontalLayout_2.addWidget(self.btnGuncelle)
        self.btnYenile = QtWidgets.QPushButton(self.centralwidget)
        self.btnYenile.setObjectName("btnYenile")
        self.horizontalLayout_2.addWidget(self.btnYenile)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableView.setLineWidth(0)
        self.tableView.setGridStyle(QtCore.Qt.NoPen)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Ad"))
        self.label_2.setText(_translate("MainWindow", "Soyad"))
        self.label.setText(_translate("MainWindow", "Telefon no"))
        self.btnEkle.setText(_translate("MainWindow", "Ekle"))
        self.btnSil.setText(_translate("MainWindow", "Sil"))
        self.btnGuncelle.setText(_translate("MainWindow", "Guncelle"))
        self.btnYenile.setText(_translate("MainWindow", "Listele"))
