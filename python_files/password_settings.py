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


def pass_val(pass1, pass2):
    print(pass1, pass2)
    pass_length = len(pass2)
    sp_count = 0
    cap_count = 0
    num_count = 0
    for j in str(pass2):
        if 'A' <= j <= 'Z':
            cap_count += 1
        elif "0" <= j <= "9":
            num_count += 1
        elif j == '@' or j == '#' or j == '$' or j == '^' or j == '&' or j == '*' or j == '%' or j == '~' or j == '`' or j == '!':
            sp_count += 1
    if not (pass_length < 8) and cap_count != 0 and num_count != 0 and sp_count != 0:
        print("True")
        return True
    else:
        print("False")
        return False


class chpassword_frame(QDialog):
    def __init__(self, username):
        super().__init__()
        self.username1 = username
        print(self.username1)
        loadUi(r"C:\Whack_A_Mole\ui_files\chpassword_frame.ui",self)
        self.setWindowTitle("Password")
        self.setFixedSize(800,800)
        self.f_back.clicked.connect(self.gotoprofile)
        self.f_passchange.clicked.connect(self.change_password)
        self.f_passchange.setEnabled(True)

    def change_password(self):
        print("changing password")
        current_password = str(self.f_cu_password.text())
        new_password = str(self.f_new_password.text())
        mydatabase = Database()
        result = mydatabase.Query_fetchone("SELECT password FROM users WHERE username = %s", (str(self.username1),))
        if current_password != "" and new_password != "" and current_password == str(result[0]):
            if current_password != new_password:
                if pass_val(current_password, new_password):
                    mydatabase = Database()
                    mydatabase.Query_update("UPDATE users SET password = %s WHERE username = %s",
                                            (str(new_password), str(self.username1)))
                    from settings import Settings_frame
                    self.w = Settings_frame(self.username1)
                    self.w.show()
                    self.close()
                else:
                    print("Enter valid data")
            else:
                self.f_response.setText("Current and new password should not be same")
        else:
            if current_password == "" and new_password == "":
                self.f_response.setText("Please fill all the credentials")
            elif current_password == "":
                self.f_response.setText("Please enter Current password")
            elif new_password == "":
                self.f_response.setText("Please enter New password")
            elif current_password != str(result[0]):
                self.f_response.setText("Current password is wrong")
            print("text not filled")
            self.f_passchange.setEnabled(False)
            timer = Timer()
            timer.setTimeout(self.enableme1, 0.2)

    def enableme1(self):
        self.f_passchange.setEnabled(True)

    def gotoprofile(self):
        from profile_settings import Profile_frame
        self.settings=Profile_frame(self.username1)
        self.settings.show()
        self.close()
