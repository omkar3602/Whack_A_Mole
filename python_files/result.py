import sys
from PyQt5.QtWidgets import QButtonGroup, QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from DBhelper import Database

class Result(QDialog):
    def __init__(self, username):
        super().__init__()
        loadUi(r"C:\Whack_A_Mole\ui_files\result.ui", self)
        self.setFixedSize(800, 800)
        self.setWindowTitle("Result")
        self.username1 = str(username)
        self.f_playagain.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_playagain.clicked.connect(self.goto_playagain)

        self.f_next.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_next.clicked.connect(self.goto_level_skin)

        self.f_mainmenu.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_mainmenu.clicked.connect(self.goto_mainmenu)

        self.f_quit.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_quit.clicked.connect(self.goto_quit)

        from gameframe import score
        self.now_score = score
        self.f_score.setText(str(score))
        mydatabase = Database()
        mydatabase.Query_insert(
            "INSERT INTO highscores (username, score, date, time) VALUES (%s, %s, date(sysdate()), time(sysdate()))",
            (str(self.username1), int(score)))
        result = mydatabase.Query_fetchone("SELECT total_score, highscore FROM users WHERE username = %s", (str(self.username1),))
        self.total_score, self.highscore = int(result[0]), int(result[1])
        print(self.total_score)
        addon = int(self.now_score) + int(self.total_score)
        
        if self.highscore <= int(self.now_score):
            self.f_highscore.setText(str(self.now_score))
            mydatabase.Query_update("UPDATE users SET total_score = %s, highscore = %s WHERE username = %s", (str(addon), str(self.now_score), str(self.username1)))
        else:
            self.f_highscore.setText(str(self.highscore))
            mydatabase.Query_update("UPDATE users SET total_score = %s WHERE username = %s", (str(addon), str(self.username1)))
        self.f_tot_score.setText(str(addon))
        self.now_score = int(self.now_score) + self.total_score
        self.level_and_skin_update()

    def goto_playagain(self):
        from gameframe import GameFrame
        self.z = GameFrame(self.username1)
        self.z.show()
        self.close()

    def goto_level_skin(self):
        from level_and_skin import level_skin
        self.level_window=level_skin(self.username1)
        self.level_window.show()
        self.close()

    def goto_mainmenu(self):
        from Main_menu import Main_menu
        self.w=Main_menu(self.username1)
        self.w.show()
        self.close()

    def goto_quit(self):
        from Main_menu import popwindow
        self.a_window = popwindow()
        self.a_window.show()

    def level_and_skin_update(self):
        mydatabase = Database()
        if int(self.now_score) >= 50:
            mydatabase.Query_update("UPDATE levels_and_skins SET e2 = %s, s2 = %s WHERE username = %s",
                                    (1, 1, str(self.username1)))
        if int(self.now_score) >= 100:
            mydatabase.Query_update("UPDATE levels_and_skins SET e3 = %s, s3 = %s WHERE username = %s",
                                    (1, 1, str(self.username1)))
        if int(self.now_score) >= 150:
            mydatabase.Query_update("UPDATE levels_and_skins SET m1 = %s, s4 = %s WHERE username = %s",
                                    (1, 1, str(self.username1)))
        if int(self.now_score) >= 200:
            mydatabase.Query_update("UPDATE levels_and_skins SET m2 = %s, s5 = %s WHERE username = %s",
                                    (1, 1, str(self.username1)))
        if int(self.now_score) >= 250:
            mydatabase.Query_update("UPDATE levels_and_skins SET m3 = %s, s6 = %s WHERE username = %s",
                                    (1, 1, str(self.username1)))
        if int(self.now_score) >= 300:
            mydatabase.Query_update("UPDATE levels_and_skins SET h1 = %s, s7 = %s WHERE username = %s",
                                    (1, 1, str(self.username1)))
        if int(self.now_score) >= 350:
            mydatabase.Query_update("UPDATE levels_and_skins SET h2 = %s, s8 = %s WHERE username = %s",
                                    (1, 1, str(self.username1)))
        if int(self.now_score) >= 400:
            mydatabase.Query_update("UPDATE levels_and_skins SET h3 = %s, s9 = %s WHERE username = %s",
                                    (1, 1, str(self.username1)))
