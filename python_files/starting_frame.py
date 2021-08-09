"""

##########  Whac A Mole Game  ##########
# Tools used Python (for back-end), PyQt5 (for front-end), QT Designer (GUI designer), MySQL(for database)
# Packages and modules :- PyQt5, mysql.connector, random, sys, gc.
# 13 Python Files
# 20 .ui files
# 1707 Lines of code
# 21 Classes with total 86 methods
# 12 Functions
########################################

# Creators
Students from Vishwakarma Institute of Technology [ DESH ]
1] M 40 Omkar Mudkanna 
2] M 41 Omkar Jahagirdar 
3] M 42 Onkar Pardeshi [ Assistant Group Leader ]
4] M 43 Abhishek Otari [ Group Leader ]
5] M 44 Sakshi Ozarde 
6] M 45 Aditya Pachore 

"""

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt


class Startwindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(r"C:\Whack_A_Mole\ui_files\startwindow.ui", self)
        self.setFixedSize(800, 800)
        self.setWindowTitle("Whack A Mole Game")

    def mousePressEvent(self, click):
        from login_signup_forgot_pass import Login
        if click.button() == Qt.LeftButton:
            self.w = Login()
            self.w.show()
            self.close()


app = QApplication(sys.argv)
window = Startwindow()
window.show()
sys.exit(app.exec_())
