from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import(QApplication, QMainWindow, QMessageBox)
import sys
from PyQt5.QtWidgets import *
from Database import *
from Registration import *
from AdminWindow import *
from Scheduling import *

class Ui_Login(QMainWindow):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(365, 326)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setStyleSheet("background-color: #240046;")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 30, 171, 20))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 16px;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 70, 71, 17))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.username_le = QtWidgets.QLineEdit(self.centralwidget)
        self.username_le.setGeometry(QtCore.QRect(70, 94, 260, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 153, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 153, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 153, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.username_le.setPalette(palette)
        self.username_le.setStyleSheet("font-color: #fff;\n"
"border: 2px solid;\n"
"border-radius: 5px;\n"
"border-color: #fff;\n"
"font-size: 12px;")
        self.username_le.setObjectName("username_le")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 130, 67, 17))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.password_le = QtWidgets.QLineEdit(self.centralwidget)
        self.password_le.setGeometry(QtCore.QRect(70, 154, 260, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 153, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 153, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 0, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 153, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.password_le.setPalette(palette)
        self.password_le.setStyleSheet("font-color: #fff;\n"
"border: 2px solid;\n"
"border-radius: 5px;\n"
"border-color: #fff;\n"
"font-size: 12px;")
        self.password_le.setObjectName("password_le")
        self.login_pb = QtWidgets.QPushButton(self.centralwidget)
        self.login_pb.setGeometry(QtCore.QRect(240, 220, 89, 25))
        self.login_pb.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.login_pb.setObjectName("login_pb")
        self.registration_pb = QtWidgets.QPushButton(self.centralwidget)
        self.registration_pb.setGeometry(QtCore.QRect(70, 220, 141, 25))
        self.registration_pb.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.registration_pb.setObjectName("registration_pb")
        self.fpassword_pb = QtWidgets.QPushButton(self.centralwidget)
        self.fpassword_pb.setGeometry(QtCore.QRect(30, 270, 131, 25))
        self.fpassword_pb.setStyleSheet("background-color: #240046;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.fpassword_pb.setObjectName("fpassword_pb")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

        self.login_pb.clicked.connect(self.verify)
        self.registration_pb.clicked.connect(self.show_registration_window)
#        self.fpassword_pb.clicked.connect(self.fpassword_window)

        self.password_le.setEchoMode(QLineEdit.Password)

    def verify(self):
        db = sqlite_db('db_files.db')
        username = (self.username_le.text(),)
        password = self.password_le.text()

        username_tuple_list = db.queries('''SELECT Username FROM Users ''')
        username_list = [''.join(i) for i in username_tuple_list]
        print(username_list, type(username_list))

        if self.username_le.text() in username_list:         

                password_query = '''SELECT Password FROM Users WHERE Username=?'''
                true_password_list = db.check(password_query,username)
                true_password_tuple = true_password_list[0]
                true_password = str(true_password_tuple[0])


                if self.username_le.text()=='devgvieira' and password==true_password:
                        self.admin_window = Ui_AdminWindow()
                        self.admin_window.show()
                        self.close()

                elif password==true_password:
                        self.scheduling_window = Ui_Scheduling()
                        self.scheduling_window.show()
                        self.close()

                else:
                        QMessageBox.warning(QMessageBox(), "Login Problem", "Incorrect password")

        else:
                QMessageBox.warning(QMessageBox(), "Login Problem", "Incorrect username or password")

    def show_registration_window(self):
        self.registration_window = Ui_Registration()
        self.registration_window.show()
        self.close()

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "Login to your account"))
        self.label_3.setText(_translate("Login", "Username"))
        self.username_le.setPlaceholderText(_translate("Login", "Insert your username (not email)"))
        self.label_4.setText(_translate("Login", "Password"))
        self.password_le.setPlaceholderText(_translate("Login", "Insert your password"))
        self.login_pb.setText(_translate("Login", "Login"))
        self.registration_pb.setText(_translate("Login", "Create Account"))
        self.fpassword_pb.setText(_translate("Login", "Forgot Password"))

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
                
app = QApplication(sys.argv)
window = Ui_Login()
window.show()
app.exec()