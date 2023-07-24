import sqlite3
from sqlite3 import Error
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QMessageBox
import sqlite3
from sqlite3 import Error
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
)

# SQLite connection and queries
class sqlite_db:

    # Initializing the connection procedure
    def __init__(self, database):
        self.conn = None
        self.cursor = None

        # Opening the connection
        if database:
            self.open(database)

    # Opening the connection
    def open(self, database):
        try:
            self.conn = sqlite3.connect(database)
            self.cursor = self.conn.cursor()
            print("Successfully Connected to SQLite.")

        except sqlite3.Error as error:
            print("Failed to create table.", error) 

    def queries(self, query):
        cursor = self.cursor
        cursor.execute(query)
        self.conn.commit()
        return cursor.fetchall()

    def insert(self,query,tuple):
         cursor = self.cursor
         cursor.execute(query,tuple)
         self.conn.commit()

    def check(self, query, tuple):
         cursor = self.cursor
         cursor.execute(query,tuple)
         return cursor.fetchall()

    def delete(self, query, tuple):
         cursor = self.cursor
         cursor.execute(query,tuple)
         self.conn.commit()

    def update(self, query, tuple):
         cursor = self.cursor
         cursor.execute(query,tuple)
         self.conn.commit()         
    
# SQLite connection to PyQt
def qt_connection():
        con = QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName('db_files.db')

        if not con.open():
                QMessageBox.critical(
                None,
                "QTableView Example - Error!",
                "Database Error: %s" % con.lastError().databaseText(),
                )      
                return False
        return True
