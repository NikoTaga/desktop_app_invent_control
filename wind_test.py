# Импорт модулей
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QFileDialog
from PyQt5 import uic, QtSql


class CatalogMainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        uic.loadUi('test_ui.ui', self)
        self.pushButton.clicked.connect(self.on_click)
        self.pushButton_4.clicked.connect(self.save_record)
        self.pushButton_3.clicked.connect(self.del_record)
        self.pushButton_2.clicked.connect(self.add_record)
        self.comboBox.activated.connect(self.select_table)

    def on_click(self):
        self.db_path = QFileDialog.getOpenFileName(parent=self, caption='Выберите файл БД', filter='*.db3 *.sqlite3')[0]
        self.textEdit.setText(self.db_path)
        self.db_connect()

    def db_connect(self):
        self.conn = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.conn.setDatabaseName(self.db_path)
        if self.conn.open():
            self.creat_combo_items(self.conn.tables(type=1))
            self.table_model = QtSql.QSqlTableModel(parent=self)
            self.table_model.setEditStrategy(2)
            self.select_table()
            self.tableView.setModel(self.table_model)

    def del_record(self):
        self.table_model.removeRow(self.tableView.currentIndex().row())
        self.table_model.select()

    def add_record(self):
        self.table_model.insertRow(self.table_model.rowCount())

    def save_record(self):
        self.table_model.submitAll()

    def select_table(self):
        self.table_model.setTable(self.comboBox.currentText())
        self.table_model.select()

    def creat_combo_items(self, tables):
        self.comboBox.clear()
        for i in tables:
            self.comboBox.addItem(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    CMW = CatalogMainWindow()
    CMW.show()
    sys.exit(app.exec_())
