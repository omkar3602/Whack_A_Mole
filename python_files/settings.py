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


class Settings_frame(QDialog):
    def __init__(self, username):
        super().__init__()
        self.username1 = str(username)
        loadUi(r"C:\Whack_A_Mole\ui_files\settings_frame.ui", self)
        self.setWindowTitle("Settings")
        self.setFixedSize(800, 800)
        self.username = username
        self.f_profile.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_profile.clicked.connect(self.gotoProfile)

        self.f_resetacc.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_resetacc.clicked.connect(self.reset_account)

        self.f_logout.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_logout.clicked.connect(self.gotologin)

        self.f_back.clicked.connect(self.gotomainmenu)

    def gotoProfile(self):
        from profile_settings import Profile_frame
        self.profile_window = Profile_frame(self.username1)
        self.profile_window.show()
        self.close()

    def gotomainmenu(self):
        from Main_menu import Main_menu
        self.main_window = Main_menu(self.username1)
        self.main_window.show()
        self.close()

    def reset_account(self):
        self.reset_window = Reset_Account(self.username1)
        self.reset_window.show()
        self.close()
    
    def gotologin(self):
        from login_signup_forgot_pass import Login
        self.logout = Login()
        self.logout.show()
        self.close()

class Reset_Account(QDialog):
    def __init__(self, username):
        super().__init__()
        loadUi(r"C:\Whack_A_Mole\ui_files\popup_resetaccount.ui", self)
        self.setWindowTitle("Alert")
        self.setFixedSize(500, 200)
        self.username1 = username
        self.f_popup_yes.setStyleSheet(
            "QPushButton{font: 12pt \"Arial Rounded MT Bold\";\npadding:5px;\nbackground-color:green;\ncolor:white;\nborder-radius:10px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")

        self.f_popup_no.setStyleSheet(
            "QPushButton{font: 12pt \"Arial Rounded MT Bold\";\npadding:5px;\nbackground-color:green;\ncolor:white;\nborder-radius:10px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_popup_yes.clicked.connect(self.resetmyacc)
        self.f_popup_no.clicked.connect(self.closepopup)
    
    def resetmyacc(self):
        mydatabase = Database()
        mydatabase.Query_update("UPDATE levels_and_skins SET e2=0,e3=0,m1=0,m2=0,m3=0,h1=0,h2=0,h3=0,s2=0,s3=0,s4=0,s5=0,s6=0,s7=0,s8=0,s9=0 WHERE username = %s", (str(self.username1),))
        mydatabase.Query_update("DELETE FROM highscores WHERE username = %s", (str(self.username1),))
        mydatabase.Query_update("UPDATE users SET total_score = '0', highscore = '0' WHERE username = %s", (str(self.username1),))
        self.closepopup()
    
    def closepopup(self):
        self.w = Settings_frame(self.username1)
        self.w.show()
        self.close()