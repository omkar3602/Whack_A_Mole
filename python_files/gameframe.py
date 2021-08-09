import sys, random
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from PyQt5 import QtGui

score = 0
t = 30
countdown_time = 3
start = False
mouseflag = cursorflag = 0

levels={
    'e1':1050,
    'e2':950,
    'e3':850,
    'm1':750,
    'm2':650,
    'm3':550,
    'h1':450,
    'h2':350,
    'h3':250,
}

def reset():
    global score, t, countdown_time, start, mouseflag, cursorflag
    score = 0
    t = 30
    countdown_time = 3
    start = False
    mouseflag = cursorflag = 0


class GameFrame(QDialog):
    def __init__(self, username):
        global start, countdown_time
        super().__init__()
        loadUi(r"C:\Whack_A_Mole\ui_files\gameframe.ui", self)
        reset()
        self.setFixedSize(800, 800)
        self.setWindowTitle("Game page")
        self.username1 = str(username)
        self.f_mole.clicked.connect(self.updatescore)
        self.f_score.setText(str(score))
        self.f_label.setVisible(False)
        self.f_score.setVisible(False)
        self.f_label_2.setVisible(False)
        self.f_timer.setVisible(False)
        self.f_mole.setVisible(False)
        self.f_mole.setEnabled(False)
        self.f_continue.setVisible(False)
        self.f_continue.setEnabled(False)
        self.f_continue.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_continue.clicked.connect(self.Result)
        self.countdown_timer = QTimer(self)
        self.countdown_timer.timeout.connect(self.countdown)
        self.countdown_timer.start(1000)
        self.f_biglabel1.setText("GAME BEGINS IN...")

    def showTime(self):
        global start, t
        if start:
            t -= 1
            if t == 0:
                start = False
                self.f_timer.setText(str(0))
            self.f_timer.setText(str(t))
        else:
            global cursorflag, mouseflag
            cursorflag, mouseflag = 1, 0
            self.f_mole.setVisible(False)
            self.f_mole.setEnabled(False)
            self.f_continue.setVisible(True)
            self.f_continue.setEnabled(True)
            self.f_biglabel1.setVisible(True)
            self.setCursor(QtGui.QCursor(Qt.ArrowCursor))
            self.f_biglabel1.setStyleSheet("font-size: 100px;color: white;")
            self.f_biglabel1.setText("TIME UP")

    def updatescore(self):
        global score
        score += 1
        self.f_score.setText(str(score))
        from level_and_skin import skin
        cursor_pix = QtGui.QPixmap(f"C:\\Whack_A_Mole\\Mallet images\\"+ skin +"r.png")
        cursor_scaled_pix = cursor_pix.scaled(QSize(60, 60))
        current_cursor = QtGui.QCursor(cursor_scaled_pix, 8, 20)
        self.setCursor(current_cursor)

        self.cursor_timer = QTimer(self)
        self.cursor_timer.timeout.connect(self.change_cursor)
        self.cursor_timer.start(200)

    def change_cursor(self):
        global cursorflag
        if cursorflag == 0:
            from level_and_skin import skin
            cursor_pix = QtGui.QPixmap(f"C:\\Whack_A_Mole\\Mallet images\\"+ skin +".png")
            cursor_scaled_pix = cursor_pix.scaled(QSize(60, 60))
            current_cursor = QtGui.QCursor(cursor_scaled_pix, 8, 20)
            self.setCursor(current_cursor)

    def change_location(self):
        if start:
            x, y = random.randrange(100, 700), random.randrange(100, 700)
            self.f_mole.move(x, y)

    def countdown(self):
        global countdown_time, start
        self.f_biglabel2.setText(str(countdown_time))
        countdown_time -= 1
        if countdown_time == -1:
            global mouseflag
            mouseflag = 1
            self.f_biglabel1.setVisible(False)
            self.f_biglabel2.setVisible(False)
            self.f_label.setVisible(True)
            self.f_score.setVisible(True)
            self.f_label_2.setVisible(True)
            self.f_timer.setVisible(True)
            self.f_mole.setVisible(True)
            self.f_mole.setEnabled(True)
            from level_and_skin import skin
            cursor_pix = QtGui.QPixmap(f"C:\\Whack_A_Mole\\Mallet images\\"+ skin +".png")
            cursor_scaled_pix = cursor_pix.scaled(QSize(60, 60))
            current_cursor = QtGui.QCursor(cursor_scaled_pix, 8, 20)
            self.setCursor(current_cursor)
            start = True
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.showTime)
            self.timer.start(1000)
            self.location_timer = QTimer(self)
            self.location_timer.timeout.connect(self.change_location)
            from level_and_skin import level
            self.location_timer.start(levels[level])

    def mousePressEvent(self, click):
        if click.button() == Qt.LeftButton and mouseflag == 1:
            from level_and_skin import skin
            cursor_pix = QtGui.QPixmap(f"C:\\Whack_A_Mole\\Mallet images\\"+ skin +"r.png")
            cursor_scaled_pix = cursor_pix.scaled(QSize(60, 60))
            current_cursor = QtGui.QCursor(cursor_scaled_pix, 8, 20)
            self.setCursor(current_cursor)

    def mouseReleaseEvent(self, click):
        if click.button() == Qt.LeftButton and mouseflag == 1:
            from level_and_skin import skin
            cursor_pix = QtGui.QPixmap(f"C:\\Whack_A_Mole\\Mallet images\\"+ skin +".png")
            cursor_scaled_pix = cursor_pix.scaled(QSize(60, 60))
            current_cursor = QtGui.QCursor(cursor_scaled_pix, 8, 20)
            self.setCursor(current_cursor)

    def Result(self):
        from result import Result
        self.countdown_timer.stop()
        self.timer.stop()
        self.location_timer.stop()
        self.r_window = Result(self.username1)
        self.r_window.show()
        self.close()
