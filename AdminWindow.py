from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import(QApplication, QMainWindow)
import sys
from PyQt5.QtWidgets import *
from Database import *
from Scheduling import *
from Entry_deletion import *
from Update_Scheduling import *

class Ui_AdminWindow(QMainWindow):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(750, 533)
        AdminWindow.setStyleSheet("background-color: #240046;")
        self.centralwidget = QtWidgets.QWidget(AdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scheduling_tb = QtWidgets.QTableWidget(self.centralwidget)
        self.scheduling_tb.setGeometry(QtCore.QRect(0, 0, 550, 500))
        self.scheduling_tb.setObjectName("scheduling_tb")
        self.scheduling_tb.setStyleSheet("font-color: #fff;\n"
"border: 2px solid;\n"
"border-radius: 5px;\n"
"border-color: #fff;\n"
"font-size: 12px;\n"
"background-color: #fff;\n")
        self.add_pb = QtWidgets.QPushButton(self.centralwidget)
        self.add_pb.setGeometry(QtCore.QRect(575, 20, 151, 25))
        self.add_pb.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.add_pb.setObjectName("add_pb")
        self.update_pb = QtWidgets.QPushButton(self.centralwidget)
        self.update_pb.setGeometry(QtCore.QRect(575, 60, 151, 25))
        self.update_pb.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.update_pb.setObjectName("update_pb")
        self.delete_pb = QtWidgets.QPushButton(self.centralwidget)
        self.delete_pb.setGeometry(QtCore.QRect(575, 100, 151, 25))
        self.delete_pb.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.delete_pb.setObjectName("delete_pb")
        self.refresh_pb = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_pb.setGeometry(QtCore.QRect(575, 140, 151, 25))
        self.refresh_pb.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.refresh_pb.setObjectName("refresh_pb")
        AdminWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AdminWindow)
        self.statusbar.setObjectName("statusbar")
        AdminWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

        self.view = self.scheduling_tb
        self.view.setColumnCount(7)
        self.view.setHorizontalHeaderLabels(["ID","Responsible Adult", "Student Name", "Date", "Time", "Subject", "Hours of Class"])
        
        if not qt_connection():
            qt_connection()

        # Selecting all entries in the table
        query = QSqlQuery("SELECT id, Responsible_Adult, Student_Name, date, time, subject, hours_of_class FROM Scheduling")

        # Adding new items to the table when necessary
        while query.next():
            rows = self.view.rowCount()
            self.view.setRowCount(rows + 1)
            columns = (0,1,2,3,4,5,6)
            i=0

            while i in columns:
                self.view.setItem(rows, i, QTableWidgetItem((str(query.value(i)))))
                i = i + 1

        # Setting the window and table display
        self.view.resizeColumnsToContents()
        self.view.show()

        self.add_pb.clicked.connect(self.show_scheduling_window)
        self.update_pb.clicked.connect(self.update_scheduling_window)
        self.delete_pb.clicked.connect(self.entry_deletion_window)
        self.refresh_pb.clicked.connect(self.refresh)

    def show_scheduling_window(self):
        self.scheduling_window = Ui_Scheduling()
        self.scheduling_window.show()

    def update_scheduling_window(self):
        self.update_scheduling_window = Ui_Update_Scheduling()
        self.update_scheduling_window.show()

    def entry_deletion_window(self):
        self.entry_deletion_window = Ui_Entry_deletion()
        self.entry_deletion_window.show()
    
    def refresh(self):
        self.view.setRowCount(0)

        query = QSqlQuery("SELECT id, Responsible_Adult, Student_Name, date, time, subject, hours_of_class FROM Scheduling")

        while query.next():
            rows = self.view.rowCount()
            self.view.setRowCount(rows + 1)
            columns = (0,1,2,3,4,5,6)
            i=0

            while i in columns:
                self.view.setItem(rows, i, QTableWidgetItem((str(query.value(i)))))
                i = i + 1

        self.view.show()

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "AdminWindow"))
        self.add_pb.setText(_translate("AdminWindow", "Add"))
        self.update_pb.setText(_translate("AdminWindow", "Update"))
        self.delete_pb.setText(_translate("AdminWindow", "Delete"))
        self.refresh_pb.setText(_translate("AdminWindow", "Refresh"))

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
