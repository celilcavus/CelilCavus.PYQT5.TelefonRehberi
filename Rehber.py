from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QTableView, QMainWindow
import sys
from TelefonRehberi import Ui_MainWindow



class TelApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnEkle.clicked.connect(self.ekle)

    def ekle(self):
        sender = self.sender().text()
        if (sender == "Ekle"):
            name = self.ui.txtAd.text()
            Surname = self.ui.txtSoyad.text()
            TelNo = self.ui.txtTelNo.text()

            self.ui.tableView = QTableView(self)
            self.ui.tableView.model = QStandardItemModel()
            list = [
                [name, Surname, TelNo]
            ]

            for i in list:
                self.ui.tableView.model.appendRow(
                    [QStandardItem(str(val)) for val in i])

            self.ui.tableView.setModel(self.ui.tableView.model)
            self.setCentralWidget(self.ui.tableView)



def AppShow():
    app = QtWidgets.QApplication(sys.argv)
    win = TelApp()
    win.show()
    sys.exit(app.exec_())


AppShow()