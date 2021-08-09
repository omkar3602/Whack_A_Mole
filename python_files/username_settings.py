import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from DBhelper import Database

import threading
from functools import wraps

id_ = int()


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


def uname_val(uname):
    print(uname)
    mydatabase = Database()
    result = mydatabase.Query_fetchall(f"SELECT * FROM users WHERE username = %s", (str(uname),))
    if result == [] and 1 < len(uname) <= 20:
        return True
    else:
        return False


class chusername_frame(QDialog):
    def __init__(self, username):
        super().__init__()
        self.username1 = username
        loadUi(r"C:\Whack_A_Mole\ui_files\chusername_frame.ui", self)
        self.setWindowTitle("Username")
        self.setFixedSize(800, 800)
        self.f_back.clicked.connect(self.gotoprofile)
        self.f_userchange.clicked.connect(self.change_username)
        self.f_userchange.setStyleSheet("QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:5px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")

    def change_username(self):
        print("changing username")
        current_username = str(self.f_cu_username.text())
        new_username = str(self.f_new_username.text())
        if current_username != "" and new_username != "" and current_username == str(self.username1):
            if current_username != new_username:
                if uname_val(new_username):
                    mydatabase = Database()
                    mydatabase.Query_update("UPDATE users SET username = %s WHERE username = %s",
                                            (str(new_username), str(self.username1)))
                    from settings import Settings_frame
                    self.w = Settings_frame(str(new_username))
                    self.w.show()
                    self.close()
                else:
                    print("Enter valid data")
            else:
                self.f_response.setText("Current and new username should not be same")
        else:
            if current_username == "" and new_username == "":
                self.f_response.setText("Please fill all the credentials")
            elif current_username == "":
                self.f_response.setText("Please enter Current username")
            elif new_username == "":
                self.f_response.setText("Please enter New username")
            elif current_username != str(self.username1):
                self.f_response.setText("Current username is wrong")

            print("text not filled")
            self.f_userchange.setEnabled(False)
            timer = Timer()
            timer.setTimeout(self.enableme1, 0.2)

    def enableme1(self):
        self.f_userchange.setEnabled(True)

    def gotoprofile(self):
        from profile_settings import Profile_frame
        self.settings = Profile_frame(self.username1)
        self.settings.show()
        self.close()
