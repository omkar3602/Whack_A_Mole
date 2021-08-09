import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import threading
from functools import wraps
from DBhelper import Database

def delay(delay=0.):
    """
    Decorator delaying the execution of a function for a while.
    """

    def wrap(f):
        @wraps(f)
        def delayed(*args, **kwargs):
            timer = threading.Timer(delay, f, args=args, kwargs=kwargs)
            timer.start()

        return delayed

    return wrap


class Timer():
    toClearTimer = False

    def setTimeout(self, fn, time):
        isInvokationCancelled = False

        @delay(time)
        def some_fn():
            if self.toClearTimer is False:
                fn()
            else:
                print('Invokation is cleared!')

        some_fn()
        return isInvokationCancelled

    def setClearTimer(self):
        self.toClearTimer = True


class Profile_frame(QDialog):
    def __init__(self, username):
        super().__init__()
        self.username1 = username
        loadUi(r"C:\Whack_A_Mole\ui_files\profile_frame.ui", self)
        self.setWindowTitle("Profile")
        self.setFixedSize(800, 800)
        self.username = username
        self.f_chusername.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\n QPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_chusername.clicked.connect(self.gotoUsername)

        self.f_chpassword.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\n QPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_chpassword.clicked.connect(self.gotoPassword)

        self.f_back.setStyleSheet(
            "QPushButton{font: 75 italic 14pt \"Georgia\"; background:white; border-radius:5px; color:black;}")
        self.f_back.clicked.connect(self.gotoSettings)

    def gotoUsername(self):
        from username_settings import chusername_frame
        s_q = str(self.f_scque.currentText())
        s_a = str(self.f_scans.text())
        if s_q != "" and s_a != "":
            """self.change_username = chusername_frame(username)
            self.change_username.show()
            self.close()"""
            mydatabase = Database()
            result = mydatabase.Query_fetchone("SELECT security_question, security_answer FROM users WHERE username = %s", (str(self.username1),))
            print(self.username1)
            print(result)
            if result[0] == s_q and result[1] == s_a:
                print("change username")
                self.change_username = chusername_frame(self.username1)
                self.change_username.show()
                self.close()
            else:
                print("else result")
                self.f_response.setText("Security Question and answer did not match")
        else:
            if s_q == "" and s_a == "":
                self.f_response.setText("Please fill all the credentials")
            elif s_a == "":
                self.f_response.setText("Please enter Security Answer")
            elif s_q == "":
                self.f_response.setText("Please enter Security Question")
            print("text not filled")
            self.f_chusername.setEnabled(False)
            timer = Timer()
            timer.setTimeout(self.enableme1, 0.2)

    def enableme1(self):
        self.f_chusername.setEnabled(True)

    def gotoPassword(self):
        from password_settings import chpassword_frame
        s_q = str(self.f_scque.currentText())
        s_a = str(self.f_scans.text())
        if s_q != "" and s_a != "":
            mydatabase = Database()
            result = mydatabase.Query_fetchone(
                "SELECT security_question, security_answer FROM users WHERE username = %s", (str(self.username1),))
            print(self.username1)
            print(result)
            if result[0] == s_q and result[1] == s_a:
                print("change password")
                self.change_password = chpassword_frame(self.username1)
                self.change_password.show()
                self.close()
            else:
                print("else result")
                self.f_response.setText("Security Question and answer did not match")
        else:
            if s_q == "" and s_a == "":
                self.f_response.setText("Please fill all the credentials")
            elif s_a == "":
                self.f_response.setText("Please enter Security Answer")
            elif s_q == "":
                self.f_response.setText("Please enter Security Question")
            print("text not filled")
            self.f_chpassword.setEnabled(False)
            timer = Timer()
            timer.setTimeout(self.enableme2, 0.2)

    def enableme2(self):
        self.f_chpassword.setEnabled(True)

    def gotoSettings(self):
        from settings import Settings_frame
        self.settings = Settings_frame(self.username1)
        self.settings.show()
        self.close()
