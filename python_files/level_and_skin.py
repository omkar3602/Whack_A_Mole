import sys
from PyQt5.QtWidgets import QButtonGroup, QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from gameframe import *
from DBhelper import Database

level = "PRE"
skin = "PRE"
Totalscore = 0


class level_skin(QDialog):
    def __init__(self, username):
        super().__init__()
        loadUi(r"C:\Whack_A_Mole\ui_files\level_and_skin2.ui", self)
        self.username1 = str(username)
        global level,skin
        level = "PRE"
        skin = "PRE"
        mydb = Database()
        result = mydb.Query_fetchone("select * from levels_and_skins where username=%s;", (str(self.username1),))
        self.result = list(result[1:])
        self.setFixedSize(800, 800)
        self.setWindowTitle("Level and skin page")
        self.f_play.setStyleSheet(
            "QPushButton{font: 15pt \"Arial Rounded MT Bold\";\npadding:5px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_play.clicked.connect(self.playgame)
        self.group1 = QButtonGroup()
        self.group2 = QButtonGroup()
        self.group1.addButton(self.e_level1)
        self.group1.addButton(self.e_level2)
        self.group1.addButton(self.e_level3)
        self.group1.addButton(self.m_level1)
        self.group1.addButton(self.m_level2)
        self.group1.addButton(self.m_level3)
        self.group1.addButton(self.h_level1)
        self.group1.addButton(self.h_level2)
        self.group1.addButton(self.h_level3)

        self.group2.addButton(self.skin_1)
        self.group2.addButton(self.skin_2)
        self.group2.addButton(self.skin_3)
        self.group2.addButton(self.skin_4)
        self.group2.addButton(self.skin_5)
        self.group2.addButton(self.skin_6)
        self.group2.addButton(self.skin_7)
        self.group2.addButton(self.skin_8)
        self.group2.addButton(self.skin_9)

        self.f_back.clicked.connect(self.goto_main_menu)
        self.e_level1.toggled.connect(self.e_lev_1)
        self.e_level2.toggled.connect(self.e_lev_2)
        self.e_level3.toggled.connect(self.e_lev_3)
        self.m_level1.toggled.connect(self.m_lev_1)
        self.m_level2.toggled.connect(self.m_lev_2)
        self.m_level3.toggled.connect(self.m_lev_3)
        self.h_level1.toggled.connect(self.h_lev_1)
        self.h_level2.toggled.connect(self.h_lev_2)
        self.h_level3.toggled.connect(self.h_lev_3)

        self.skin_1.toggled.connect(self.s_1)
        self.skin_2.toggled.connect(self.s_2)
        self.skin_3.toggled.connect(self.s_3)
        self.skin_4.toggled.connect(self.s_4)
        self.skin_5.toggled.connect(self.s_5)
        self.skin_6.toggled.connect(self.s_6)
        self.skin_7.toggled.connect(self.s_7)
        self.skin_8.toggled.connect(self.s_8)
        self.skin_9.toggled.connect(self.s_9)

        if self.result[1] == 1 and self.result[10] == 1:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../Whack_A_Mole/Images and icon/unlocked.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            self.e_level2.setIcon(icon)
            self.s2_label.setText("Unlocked")
        if self.result[2] == 1 and self.result[11] == 1:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../Whack_A_Mole/Images and icon/unlocked.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            self.e_level3.setIcon(icon)
            self.s3_label.setText("Unlocked")
        if self.result[3] == 1 and self.result[12] == 1:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../Whack_A_Mole/Images and icon/unlocked.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            self.m_level1.setIcon(icon)
            self.s4_label.setText("Unlocked")
        if self.result[4] == 1 and self.result[13] == 1:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../Whack_A_Mole/Images and icon/unlocked.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            self.m_level2.setIcon(icon)
            self.s5_label.setText("Unlocked")
        if self.result[5] == 1 and self.result[14] == 1:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../Whack_A_Mole/Images and icon/unlocked.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            self.m_level3.setIcon(icon)
            self.s6_label.setText("Unlocked")
        if self.result[6] == 1 and self.result[15] == 1:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../Whack_A_Mole/Images and icon/unlocked.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            self.h_level1.setIcon(icon)
            self.s7_label.setText("Unlocked")
        if self.result[7] == 1 and self.result[16] == 1:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../Whack_A_Mole/Images and icon/unlocked.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            self.h_level2.setIcon(icon)
            self.s8_label.setText("Unlocked")
        if self.result[8] == 1 and self.result[17] == 1:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../Whack_A_Mole/Images and icon/unlocked.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            self.h_level3.setIcon(icon)
            self.s9_label.setText("Unlocked")

    def e_lev_1(self):
        global level
        level = 'e1'

    def e_lev_2(self):
        global level
        if self.e_level2.isChecked() and self.result[1] == 1:
            level = 'e2'
        elif self.e_level2.isChecked() and self.result[1] == 0:
            level = "ERROR"
            self.l_pop = level_popup()
            self.l_pop.show()

    def e_lev_3(self):
        global level
        if self.e_level3.isChecked() and self.result[2] == 1:
            level = 'e3'
        elif self.e_level3.isChecked() and self.result[2] == 0:
            level = "ERROR"
            self.l_pop = level_popup()
            self.l_pop.show()

    def m_lev_1(self):
        global level
        if self.m_level1.isChecked() and self.result[3] == 1:
            level = 'm1'
        elif self.m_level1.isChecked() and self.result[3] == 0:
            level = "ERROR"
            self.l_pop = level_popup()
            self.l_pop.show()

    def m_lev_2(self):
        global level
        if self.m_level2.isChecked() and self.result[4] == 1:
            level = 'm2'
        elif self.m_level2.isChecked() and self.result[4] == 0:
            level = "ERROR"
            self.l_pop = level_popup()
            self.l_pop.show()

    def m_lev_3(self):
        global level
        if self.m_level3.isChecked() and self.result[5] == 1:
            level = 'm3'
        elif self.m_level3.isChecked() and self.result[5] == 0:
            level = "ERROR"
            self.l_pop = level_popup()
            self.l_pop.show()

    def h_lev_1(self):
        global level
        if self.h_level1.isChecked() and self.result[6] == 1:
            level = 'h1'
        elif self.h_level1.isChecked() and self.result[6] == 0:
            level = "ERROR"
            self.l_pop = level_popup()
            self.l_pop.show()

    def h_lev_2(self):
        global level
        if self.h_level2.isChecked() and self.result[7] == 1:
            level = 'h2'
        elif self.h_level2.isChecked() and self.result[7] == 0:
            level = "ERROR"
            self.l_pop = level_popup()
            self.l_pop.show()

    def h_lev_3(self):
        global level
        if self.h_level3.isChecked() and self.result[8] == 1:
            level = 'h3'
        elif self.h_level3.isChecked() and self.result[8] == 0:
            level = "ERROR"
            self.l_pop = level_popup()
            self.l_pop.show()

    def s_1(self):
        global skin
        skin = '1'

    def s_2(self):
        global skin
        if self.skin_2.isChecked() and self.result[10] == 1:
            skin = '2'
        elif self.skin_2.isChecked() and self.result[10] == 0:
            skin = "ERROR"
            self.l_pop = skin_popup()
            self.l_pop.show()

    def s_3(self):
        global skin
        if self.skin_3.isChecked() and self.result[11] == 1:
            skin = '3'
        elif self.skin_3.isChecked() and self.result[11] == 0:
            skin = "ERROR"
            self.l_pop = skin_popup()
            self.l_pop.show()

    def s_4(self):
        global skin
        if self.skin_4.isChecked() and self.result[12] == 1:
            skin = '4'
        elif self.skin_4.isChecked() and self.result[12] == 0:
            skin = "ERROR"
            self.l_pop = skin_popup()
            self.l_pop.show()

    def s_5(self):
        global skin
        if self.skin_5.isChecked() and self.result[13] == 1:
            skin = '5'
        elif self.skin_5.isChecked() and self.result[13] == 0:
            skin = "ERROR"
            self.l_pop = skin_popup()
            self.l_pop.show()

    def s_6(self):
        global skin
        if self.skin_6.isChecked() and self.result[14] == 1:
            skin = '6'
        elif self.skin_6.isChecked() and self.result[14] == 0:
            skin = "ERROR"
            self.l_pop = skin_popup()
            self.l_pop.show()

    def s_7(self):
        global skin
        if self.skin_7.isChecked() and self.result[15] == 1:
            skin = '7'
        elif self.skin_7.isChecked() and self.result[15] == 0:
            skin = "ERROR"
            self.l_pop = skin_popup()
            self.l_pop.show()

    def s_8(self):
        global skin
        if self.skin_8.isChecked() and self.result[16] == 1:
            skin = '8'
        elif self.skin_8.isChecked() and self.result[16] == 0:
            skin = "ERROR"
            self.l_pop = skin_popup()
            self.l_pop.show()

    def s_9(self):
        global skin
        if self.skin_9.isChecked() and self.result[17] == 1:
            skin = '9'
        elif self.skin_9.isChecked() and self.result[17] == 0:
            skin = "ERROR"
            self.l_pop = skin_popup()
            self.l_pop.show()

    def playgame(self):
        global skin
        global level
        if (skin not in ["ERROR", "PRE"]) and (level not in ["ERROR", "PRE"]):
            self.z = GameFrame(self.username1)
            self.z.show()
            self.close()
        elif (skin == "ERROR") and (level == "ERROR"):
            self.f_play_game_err.setText(f"Level and Skin is Locked")
        elif skin == "ERROR":
            self.f_play_game_err.setText(f"Skin is Locked")
        elif level == "ERROR":
            self.f_play_game_err.setText(f"Level is Locked")
        elif (skin == "PRE") and (level == "PRE"):
            self.f_play_game_err.setText(f"Please Select Level and Skin")
        elif skin == "PRE":
            self.f_play_game_err.setText(f"Please Select Skin")
        else:
            self.f_play_game_err.setText(f"Please Select Level")

    def goto_main_menu(self):
        from Main_menu import Main_menu
        self.w = Main_menu(self.username1)
        self.w.show()
        self.close()


class level_popup(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(r"C:\Whack_A_Mole\ui_files\level_popupwindow.ui", self)
        self.setWindowTitle("Alert")
        self.setFixedSize(500, 200)
        self.f_ok_level.setStyleSheet(
            "QPushButton{font: 15pt \"Arial Rounded MT Bold\";\npadding:5px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_ok_level.clicked.connect(self.OK)

    def OK(self):
        self.close()


class skin_popup(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(r"C:\Whack_A_Mole\ui_files\skin_popupwindow.ui", self)
        self.setWindowTitle("Alert")
        self.setFixedSize(500, 200)
        self.f_ok_skin.setStyleSheet(
            "QPushButton{font: 15pt \"Arial Rounded MT Bold\";\npadding:5px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_ok_skin.clicked.connect(self.OK)

    def OK(self):
        self.close()
