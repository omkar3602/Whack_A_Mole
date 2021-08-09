import sys

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from Main_menu import *
from DBhelper import Database
import threading
from functools import wraps
import gc

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


def name_val(name):
    print(name)
    if 1 < len(name) <= 20:
        return True
    else:
        return False


def email_val(email):
    import re

    regex = '^[a-z0-9]+[\.]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        mydatabase = Database()
        result = mydatabase.Query_fetchall("SELECT email FROM users WHERE email = %s", (str(email),))
        if result == []:
            return True
        return False
    else:
        return False


def pass_val(pass1, pass2):
    print(pass1, pass2)
    pass_length = len(pass1)
    sp_count = 0
    cap_count = 0
    num_count = 0
    for j in str(pass1):
        if 'A' <= j <= 'Z':
            cap_count += 1
        elif "0" <= j <= "9":
            num_count += 1
        elif j == '@' or j == '#' or j == '$' or j == '^' or j == '&' or j == '*' or j == '%' or j == '~' or j == '`' or j == '!':
            sp_count += 1
    if pass1 != pass2:
        return "100"
    if not (pass_length < 8) and cap_count != 0 and num_count != 0 and sp_count != 0 and pass1 == pass2:
        print("True")
        return True
    else:
        print("False")
        return False


def security_ques_val(security_ques, answer):
    print(security_ques)
    print(answer)
    if str(security_ques) != "" and str(answer) != "":
        return True
    else:
        return False


def insert_data(name, uname, email, pass1, security_ques, answer):
    print("Inserting")
    mydatabase = Database()
    print(mydatabase.Query_insert(
        "INSERT INTO users (username, name, email, password, security_question, security_answer, total_score, highscore) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (uname, name, email, pass1, security_ques, answer, '0', '0')), "record inserted.")
    print(mydatabase.Query_insert(
        "INSERT INTO levels_and_skins (username, e1, e2, e3, m1,m2,m3,h1,h2,h3,s1,s2,s3,s4,s5,s6,s7,s8,s9) VALUES (%s, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)",
        (uname,)), "record inserted.")


class Signup(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(r"C:\Whack_A_Mole\ui_files\Signuppage.ui", self)
        self.setFixedSize(800, 800)
        self.setWindowTitle("Signup page")
        self.f_goto_login.clicked.connect(self.gotoLogin)
        self.f_create_account.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_create_account.clicked.connect(self.create_acc)
        self.f_security_ques.setCurrentIndex(0)

    def create_acc(self):
        name = self.f_name.text()
        uname = self.f_uname.text()
        email = self.f_email.text()
        pass1 = self.f_pass1.text()
        pass2 = self.f_pass2.text()
        security_ques = self.f_security_ques.currentText()
        answer = self.f_answer.text()

        if uname == "":
            self.f_responseerror.setText("")
        elif not uname_val(uname):
            self.f_responseerror.setStyleSheet("color:red;\nfont: 10pt 'Meiryo UI';")
            self.f_responseerror.setText("Username unavailable")
        else:
            self.f_responseerror.setStyleSheet("color:green;\nfont: 10pt 'Meiryo UI';")
            self.f_responseerror.setText("Username available")

        if email == "":
            self.f_responseerror_2.setText("")
        elif email_val(email):
            self.f_responseerror_2.setStyleSheet("color:green;\nfont: 10pt 'Meiryo UI';")
            self.f_responseerror_2.setText("Email available")
        elif not email_val(uname):
            self.f_responseerror_2.setStyleSheet("color:red;\nfont: 10pt 'Meiryo UI';")
            self.f_responseerror_2.setText("Email unavailable")

        if pass_val(pass1, pass2) == "100":
            self.f_responseerror2.setText("Both the passwords does not match")
        else:
            self.f_responseerror2.setText("")

        if name != "" and uname != "" and email != "" and pass1 != "" and pass2 != "" and security_ques != "" and answer != "":
            if name_val(name) and uname_val(uname) and email_val(email) and pass_val(pass1,
                                                                                     pass2) and security_ques_val(
                    security_ques,
                    answer):
                insert_data(name, uname, email, pass1, security_ques, answer)
                self.main_menu = Main_menu(uname)
                self.main_menu.show()
                self.close()
            else:
                print("Enter valid data")
        else:
            self.f_responseerror1.setText("Please fill all the credentials")
            self.f_create_account.setEnabled(False)
            timer = Timer()
            timer.setTimeout(self.enableme, 0.2)

    def enableme(self):
        self.f_create_account.setEnabled(True)

    def gotoLogin(self):
        self.log = Login()
        self.log.show()
        self.close()


def login_val(username, password):
    print("Checking")
    mydatabase = Database()
    result = mydatabase.Query_fetchone(f"SELECT username FROM users WHERE username = %s", (str(username),))
    if not (result is None):
        result = mydatabase.Query_fetchone(f"SELECT password FROM users WHERE username = %s", (str(username),))
        if password == str(result[0]):
            print("True")
            return True
        else:
            print("False")
            return False
    else:
        return False


class Login(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(r"C:\Whack_A_Mole\ui_files\Loginpage.ui", self)
        self.setFixedSize(800, 800)
        self.setWindowTitle("Login page")
        self.f_login.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_login.clicked.connect(self.login)
        self.f_goto_signup.clicked.connect(self.gotoSignup)
        self.f_forgot_pass.clicked.connect(self.gotoforgotpassword)
        self.f_login.setEnabled(True)

    def login(self):
        username = str(self.f_username.text())
        password = str(self.f_password.text())
        self.f_responseerror.setText("")
        if username != "" and password != "":
            if login_val(username, password):
                print("Going to main menu")
                self.main_menu = Main_menu(username)
                self.main_menu.show()
                self.close()
            else:
                self.f_responseerror.setText("Username and password did not match")
        else:
            if username == "" and password == "":
                self.f_responseerror.setText("Please enter the credentials")
            elif username == "":
                self.f_responseerror.setText("Please enter the username")
            elif password == "":
                self.f_responseerror.setText("Please enter the password")
            self.f_login.setEnabled(False)
            timer = Timer()
            timer.setTimeout(self.enableme, 0.2)

    def enableme(self):
        self.f_login.setEnabled(True)

    def gotoSignup(self):
        self.sign = Signup()
        self.sign.show()
        self.close()

    def gotoforgotpassword(self):
        self.forgot_pass = Forgotpassword()
        global id_
        id_ = id(self.forgot_pass)
        self.forgot_pass.show()
        self.close()


def forgot_pass_val(username):
    print("Checking")
    mydatabase = Database()
    result = mydatabase.Query_fetchone("SELECT username FROM users WHERE username = %s", (str(username),))
    if not (result is None):
        return True
    else:
        return False


class Forgotpassword(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(r"C:\Whack_A_Mole\ui_files\Forgotpassword_sec_check.ui", self)
        self.setFixedSize(800, 800)
        self.setWindowTitle("Forgot Password page")
        self.f_goback.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_goback.clicked.connect(self.gotologin)
        self.f_continue.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_continue.clicked.connect(self.continueto_sec_check)

    def gotologin(self):
        self.log = Login()
        self.log.show()
        self.close()

    def continueto_sec_check(self):
        username = str(self.f_username.text())
        if username != "":
            result = forgot_pass_val(username)
            if result:
                mydatabase = Database()
                security_question = mydatabase.Query_fetchone(
                    "SELECT security_question, security_answer, password FROM users WHERE username = %s",
                    (str(username),))
                self.w = Forgotpassword_sec_check(security_question[0], security_question[1], security_question[2],
                                                  username)
                self.w.show()
                self.close()
            else:
                self.f_responseerror.setText("Username does not exists")
        else:
            self.f_responseerror.setText("Please enter the username")
            self.f_continue.setEnabled(False)
            timer = Timer()
            timer.setTimeout(self.enableme, 0.2)

    def enableme(self):
        self.f_continue.setEnabled(True)


class Forgotpassword_sec_check(QDialog):
    def __init__(self, s_q, s_a, password, username):
        super().__init__()
        loadUi(r"C:\Whack_A_Mole\ui_files\Forgotpassword.ui", self)
        self.username1 = username
        self.security_question = s_q
        self.security_answer = s_a
        self.password = password
        self.label_3.setText(str(self.security_question))
        self.setFixedSize(800, 800)
        self.setWindowTitle("Forgot Password page")
        self.f_getpass.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_getpass.clicked.connect(self.getpassword)
        self.f_gotologin.clicked.connect(self.gotologin)
        self.f_gotologin.setStyleSheet(
            "QPushButton{font: 16pt \"Arial Rounded MT Bold\";\npadding:15px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")

    def gotologin(self):
        self.w = Login()
        self.w.show()
        self.close()

    def getpassword(self):
        security_ans_cu = str(self.f_answer.text())
        email_id = str(self.f_emailid.text())
        if security_ans_cu != "" and email_id != "":
            mydatabase = Database()
            result = mydatabase.Query_fetchone("SELECT email FROM users WHERE username = %s", (str(self.username1),))
            if security_ans_cu == self.security_answer and email_id == result[0]:
                try:
                    self.send_email(email_id, self.username1)
                    self.w = Response_Pass("Email sent to you successfully", 200)
                    self.w.show()
                    self.close()
                except:
                    self.w = Response_Pass("An Error occurred while sending email", 404)
                    self.w.show()
                    self.close()
            else:
                self.w = Response_Pass("Incorrect Username or Email ID", 403)
                self.w.show()
                self.close()
        else:
            self.f_responseerror.setText("Please enter the Security answer")
            self.f_getpass.setEnabled(False)
            timer = Timer()
            timer.setTimeout(self.enableme, 0.2)

    def send_email(self, email_id, username):
        import smtplib
        from email.message import EmailMessage
        mydatabase = Database()
        password = mydatabase.Query_fetchone("SELECT password FROM users WHERE username = %s", (str(username),))[0]
        print(password)
        msg = EmailMessage()
        msg['Subject'] = 'Whack A Mole Game'
        msg['From'] = 'Whack A Mole Team'
        msg['To'] = email_id
        msg.set_content("Hello, your password is " + "'" + password + "'" + ".")
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("gamewhackamole@gmail.com", "whackamole@123")
        server.send_message(msg)
        server.quit()

    def enableme(self):
        self.f_getpass.setEnabled(True)


class Response_Pass(QDialog):
    def __init__(self, text, status):
        super().__init__()
        loadUi(r"C:\Whack_A_Mole\ui_files\responsePass.ui", self)
        self.setFixedSize(500, 300)
        self.setWindowTitle("Response")
        self.f_ok.setStyleSheet(
            "QPushButton{font: 15pt \"Arial Rounded MT Bold\";\npadding:5px;\nbackground-color:green;\ncolor:white;\nborder-radius:20px;}\nQPushButton:hover{\nborder:1px solid white;\nbackground-color:#03C227;}")
        self.f_answer.setText(str(text))
        if status == 200:
            self.f_ok.clicked.connect(self.gotologin)
        elif status == 400:
            self.f_ok.clicked.connect(self.gotoforgotpassword)
        else:
            self.f_ok.clicked.connect(self.gotoforgotpassword)

    def gotologin(self):
        self.log = Login()
        self.log.show()
        self.close()
        global id_
        for obj in gc.get_objects():
            if id(obj) == id_:
                obj.close()

    def gotoforgotpassword(self):
        self.fp = Forgotpassword()
        self.fp.show()
        self.close()
        global id_
        for obj in gc.get_objects():
            if id(obj) == id_:
                obj.close()
