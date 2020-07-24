from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import resources_rc
from backend import *
from os import path 

vcc = ""
user_email = ""
user_data = list()
dummy_user = list()

def Success_Message(code):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setWindowTitle(" ")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    msg.setWindowIcon(icon)
    if not code:
        msg.setText("Verification Code Has Been Sent To Your Email Address")
    elif code == 1:
        msg.setText("Account Has Been Registered Successfully.")
    elif code == 2:
        msg.setText("Please Be Patient While We Create Your Account. Time Depends On Your Internet Speed.")
    elif code == 3:
        msg.setText("Login Successfull")
    elif code == 4:
        msg.setText("Password Reset Successfull")
    elif code == 5:
        msg.setText("Name Has Been Changed Successfully")
    elif code == 6:
        msg.setText("Email Has Been Changed Successfully")
    elif code == 7:
        msg.setText("Username Has Been Changed Successfully")
    elif code == 8:
        msg.setText("Password Has Been Changed Successfully")
    elif code == 9:
        msg.setText("You Have Not Made Any Transactions Yet.")
    elif code == 10:
        msg.setText("Working On Your Transaction")
    elif code == 11:
        msg.setText("Amount Has Been Deposited To Your Account Balance Successfully.")
    elif code == 12:
        msg.setText("Amount Has Been Withdrawed From Your Account Balance Successfully.")
    elif code == 13:
        msg.setText("Amount Has Been Transferred From Your Account Successfully.")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()


def Error_Message(code):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setWindowTitle(" ")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    msg.setWindowIcon(icon)
    if not code:
        msg.setText("Invalid Email Address")
    elif code == 1:
        msg.setText("The Email Is Already In Use.")
    elif code == 2:
        msg.setText("You Are Not Connected To The Internet.")
    elif code == 3:
        msg.setText("Invalid Name")
    elif code == 4:
        msg.setText("Invalid Username")
    elif code == 5:
        msg.setText("The Username Is Already In Use.")
    elif code == 6:
        msg.setText("Invalid Password")
    elif code == 7:
        msg.setText("The Confirmation Password Did Not Match With The Orginal Password.")
    elif code == 8:
        msg.setText("Wrong Verification Code")
    elif code ==9:
        msg.setText("You Didn't Agree To The Terms And Conditions Yet.")
    elif code == 10:
        msg.setText("Enter Your Correct Email Address In The Username/Email Field")
    elif code == 11:
        msg.setText("Invalid Login Credentials")
    elif code == 12:
        msg.setText("Invalid Amount")
    elif code == 13:
        msg.setText("Insufficient Balance")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()


class Ui_TransferMoney(object):
    def setupUi(self, TransferMoney):
        global user_data
        TransferMoney.setObjectName("TransferMoney")
        TransferMoney.resize(600, 600)
        TransferMoney.setMinimumSize(QtCore.QSize(600, 600))
        TransferMoney.setMaximumSize(QtCore.QSize(600, 600))
        TransferMoney.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TransferMoney.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(TransferMoney)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Back_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Back_Button.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.Back_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_Button.setIcon(icon1)
        self.Back_Button.setObjectName("Back_Button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 10, 120, 120))
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/send.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        
        self.Show_Users = QtWidgets.QListWidget(self.centralwidget)
        self.Show_Users.setGeometry(QtCore.QRect(20, 150, 551, 271))
        self.Show_Users.setObjectName("Show_Users")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 440, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(21)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Available_Users = QtWidgets.QComboBox(self.centralwidget)
        self.Available_Users.setGeometry(QtCore.QRect(190, 440, 211, 31))
        self.Available_Users.setEditable(True)
        self.Available_Users.setObjectName("Available_Users")
        to_show = Retreive_All_Users_Names()
        to_show.remove(user_data[1])
        for ts in to_show:
            self.Show_Users.addItem(ts)
            self.Available_Users.addItem(ts)
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 490, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(21)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Amount = QtWidgets.QLineEdit(self.centralwidget)
        self.Amount.setGeometry(QtCore.QRect(190, 490, 211, 31))
        self.Amount.setObjectName("Amount")
        self.Amount.setValidator(QtGui.QIntValidator())
        self.Transfer_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Transfer_Button.setGeometry(QtCore.QRect(210, 540, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(21)
        self.Transfer_Button.setFont(font)
        self.Transfer_Button.setObjectName("Transfer_Button")
        TransferMoney.setCentralWidget(self.centralwidget)

        self.retranslateUi(TransferMoney)
        QtCore.QMetaObject.connectSlotsByName(TransferMoney)
        self.Back_Button.clicked.connect(self.Take_To_Payments)
        self.Transfer_Button.clicked.connect(self.Make_The_Transfer)

    def Make_The_Transfer(self):
        global user_data
        to_show1 = Retreive_All_Users_Names()
        to_show1.remove(user_data[1])
        try:
            if not Internet_Available():
                raise No_Internet
            if "," in self.Amount.text() or "-" in self.Amount.text() or self.Amount.text() == "":
                raise Invalid_Amount
            if int(self.Amount.text()) > int(user_data[3]):
                raise Insufficient_Balance
            if self.Available_Users.currentText() == "" or self.Available_Users.currentText() == user_data[1]:
                raise Invalid_Username
            if self.Available_Users.currentText() not in to_show1:
                raise Invalid_Username
        except No_Internet:
            Error_Message(2)
        except Invalid_Amount:
            Error_Message(12)
        except Insufficient_Balance:
            Error_Message(13)
        except Invalid_Username:
            Error_Message(4)
        else:
            Success_Message(10)
            data_user = Retrieve_Users_Data(self.Available_Users.currentText())
            amount = int(self.Amount.text())
            user_data[4] = str(int(user_data[4]) + 1)
            user_data[3] = str(int(user_data[3]) - amount)
            data_user[4] = str(int(data_user[4]) + 1)
            data_user[3] = str(int(data_user[3]) + amount)
            Modify_Content_In_File(user_data)
            Modify_Content_In_File(data_user)
            Write_To_Passbook(2, Get_User_Position(user_data[1]), str(amount), user_data[3], data_user[1])
            Write_To_Passbook(3, Get_User_Position(data_user[1]), str(amount), data_user[3], user_data[1])
            Transactional_Email(2, user_data, str(amount), data_user[1])
            Transactional_Email(3, data_user, str(amount), user_data[1])
            Success_Message(13)
            Payments.show()
            TransferMoney.hide()

    def Take_To_Payments(self):
        Payments.show()
        TransferMoney.hide()

    def retranslateUi(self, TransferMoney):
        _translate = QtCore.QCoreApplication.translate
        global user_data
        TransferMoney.setWindowTitle(_translate("TransferMoney", "Transfer Money"))
        self.Back_Button.setToolTip(_translate("TransferMoney", "<html><head/><body><p><span style=\" font-weight:600;\">Back To Payments</span></p></body></html>"))
        self.Show_Users.setToolTip(_translate("TransferMoney", "<html><head/><body><p><span style=\" font-weight:600;\">Available Users</span></p></body></html>"))
        self.label_3.setText(_translate("TransferMoney", "<html><head/><body><p><span style=\" color:#ffffff;\">Select User</span></p></body></html>"))
        self.Available_Users.setToolTip(_translate("TransferMoney", "<html><head/><body><p><span style=\" font-weight:600;\">Available Users</span></p></body></html>"))
        self.label_4.setText(_translate("TransferMoney", "<html><head/><body><p><span style=\" color:#ffffff;\">Amount</span></p></body></html>"))
        self.Amount.setToolTip(_translate("TransferMoney", "<html><head/><body><p><span style=\" font-weight:600;\">Amount To Transfer : Balance : {} Rs</span></p></body></html>".format(user_data[3])))
        self.Transfer_Button.setToolTip(_translate("TransferMoney", "<html><head/><body><p><span style=\" font-weight:600;\">Transfer Amount</span></p></body></html>"))
        self.Transfer_Button.setText(_translate("TransferMoney", "Transfer"))


class Ui_Passbook(object):
    def setupUi(self, Passbook):
        global user_data
        Passbook.setObjectName("Passbook")
        Passbook.resize(600, 400)
        Passbook.setMinimumSize(QtCore.QSize(600, 400))
        Passbook.setMaximumSize(QtCore.QSize(600, 400))
        Passbook.setBaseSize(QtCore.QSize(600, 600))
        Passbook.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Passbook.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Passbook)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Back_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Back_Button.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.Back_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_Button.setIcon(icon1)
        self.Back_Button.setObjectName("Back_Button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 180, 90))
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/passbook.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 120, 561, 241))
        self.listWidget.setObjectName("listWidget")
        file_loc = "C:\\Projects\\Python\\Banking2\\{}.txt".format(Get_User_Position(user_data[1]))
        if not path.exists(file_loc):
            self.listWidget.addItem("You Have Not Made Any Transactions Yet.")
            Success_Message(9)
        else:
            file = open(file_loc)
            for line in file.readlines():
                self.listWidget.addItem(line.rstrip())
            file.close()
        self.Balance = QtWidgets.QLineEdit(self.centralwidget)
        self.Balance.setGeometry(QtCore.QRect(430, 370, 151, 21))
        self.Balance.setObjectName("Balance")
        self.Balance.setText(user_data[3] + " Rs")
        self.Balance.setReadOnly(True)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 360, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        Passbook.setCentralWidget(self.centralwidget)

        self.retranslateUi(Passbook)
        QtCore.QMetaObject.connectSlotsByName(Passbook)
        self.Back_Button.clicked.connect(self.Back_To_Payments)

    def Back_To_Payments(self):
        Payments.show()
        Passbook.hide()

    def retranslateUi(self, Passbook):
        _translate = QtCore.QCoreApplication.translate
        Passbook.setWindowTitle(_translate("Passbook", "Passbook"))
        self.Back_Button.setToolTip(_translate("Passbook", "<html><head/><body><p><span style=\" font-weight:600;\">Back To Payments</span></p></body></html>"))
        self.Balance.setToolTip(_translate("Passbook", "<html><head/><body><p><span style=\" font-weight:600;\">Account Balance</span></p></body></html>"))
        self.label_3.setText(_translate("Passbook", "<html><head/><body><p><span style=\" color:#ffffff;\">Account Balance</span></p></body></html>"))


class Ui_Withdraw(object):
    def setupUi(self, Withdraw):
        global user_data
        Withdraw.setObjectName("Withdraw")
        Withdraw.resize(500, 300)
        Withdraw.setMaximumSize(QtCore.QSize(500, 300))
        Withdraw.setBaseSize(QtCore.QSize(500, 300))
        Withdraw.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Withdraw.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Withdraw)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 500, 300))
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 42, 42))
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Back_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Back_Button.setGeometry(QtCore.QRect(0, 0, 42, 42))
        self.Back_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_Button.setIcon(icon1)
        self.Back_Button.setObjectName("Back_Button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 84, 84))
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/minus.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(21)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(21)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Balance = QtWidgets.QLineEdit(self.centralwidget)
        self.Balance.setGeometry(QtCore.QRect(260, 120, 221, 31))
        self.Balance.setObjectName("Balance")
        self.Balance.setText(user_data[3] + " Rs")
        self.Balance.setReadOnly(True)
        self.Amount = QtWidgets.QLineEdit(self.centralwidget)
        self.Amount.setGeometry(QtCore.QRect(260, 190, 221, 31))
        self.Amount.setObjectName("Amount")
        self.Amount.setValidator(QtGui.QIntValidator())
        self.WithdrawButton = QtWidgets.QPushButton(self.centralwidget)
        self.WithdrawButton.setGeometry(QtCore.QRect(180, 240, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(21)
        self.WithdrawButton.setFont(font)
        self.WithdrawButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.WithdrawButton.setObjectName("WithdrawButton")
        Withdraw.setCentralWidget(self.centralwidget)

        self.retranslateUi(Withdraw)
        QtCore.QMetaObject.connectSlotsByName(Withdraw)
        self.Back_Button.clicked.connect(self.Go_Back)
        self.WithdrawButton.clicked.connect(self.Withdrawing_Amount)

    def Withdrawing_Amount(self):
        try:
            if not Internet_Available():
                raise No_Internet
            if "," in self.Amount.text() or "-" in self.Amount.text() or self.Amount.text() == "":
                raise Invalid_Amount
            if int(self.Amount.text()) > int(self.Balance.text().replace(" Rs", "")):
                raise Insufficient_Balance
        except No_Internet:
            Error_Message(2)
        except Invalid_Amount:
            Error_Message(12)
        except Insufficient_Balance:
            Error_Message(13)
        else:
            Success_Message(10)
            global user_data
            amount = int(self.Amount.text())
            user_data[4] = str(int(user_data[4]) + 1)
            user_data[3] = str(int(user_data[3]) - amount)
            Modify_Content_In_File(user_data)
            Write_To_Passbook(1, Get_User_Position(user_data[1]), str(amount), user_data[3])
            Transactional_Email(1, user_data, str(amount))
            Success_Message(12)
            Payments.show()
            Withdraw.hide()

    def Go_Back(self):
        Payments.show()
        Withdraw.hide()

    def retranslateUi(self, Withdraw):
        _translate = QtCore.QCoreApplication.translate
        Withdraw.setWindowTitle(_translate("Withdraw", "Withdraw"))
        self.Back_Button.setToolTip(_translate("Withdraw", "<html><head/><body><p><span style=\" font-weight:600;\">Back To Payments</span></p></body></html>"))
        self.label_3.setText(_translate("Withdraw", "<html><head/><body><p><span style=\" color:#ffffff;\">Account Balance</span></p></body></html>"))
        self.label_4.setText(_translate("Withdraw", "<html><head/><body><p><span style=\" color:#ffffff;\">Amount</span></p></body></html>"))
        self.Balance.setToolTip(_translate("Withdraw", "<html><head/><body><p><span style=\" font-weight:600;\">Current Account Balance</span></p></body></html>"))
        self.Amount.setToolTip(_translate("Withdraw", "<html><head/><body><p><span style=\" font-weight:600;\">Amount To Withdraw</span></p></body></html>"))
        self.WithdrawButton.setToolTip(_translate("Withdraw", "<html><head/><body><p><span style=\" font-weight:600;\">Withdraw Amount From Account</span></p></body></html>"))
        self.WithdrawButton.setText(_translate("Withdraw", "Withdraw"))


class Ui_Deposit(object):
    def setupUi(self, Deposit):
        global user_data
        Deposit.setObjectName("Deposit")
        Deposit.resize(500, 300)
        Deposit.setMaximumSize(QtCore.QSize(500, 300))
        Deposit.setBaseSize(QtCore.QSize(500, 300))
        Deposit.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Deposit.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Deposit)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 500, 300))
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 42, 42))
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Back_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Back_Button.setGeometry(QtCore.QRect(0, 0, 42, 42))
        self.Back_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_Button.setIcon(icon1)
        self.Back_Button.setObjectName("Back_Button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 84, 84))
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/add.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(21)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(21)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Balance = QtWidgets.QLineEdit(self.centralwidget)
        self.Balance.setGeometry(QtCore.QRect(260, 120, 221, 31))
        self.Balance.setObjectName("Balance")
        self.Balance.setText(user_data[3] + " Rs")
        self.Balance.setReadOnly(True)
        self.Amount = QtWidgets.QLineEdit(self.centralwidget)
        self.Amount.setGeometry(QtCore.QRect(260, 190, 221, 31))
        self.Amount.setObjectName("Amount")
        self.Amount.setValidator(QtGui.QIntValidator())
        self.DepositButton = QtWidgets.QPushButton(self.centralwidget)
        self.DepositButton.setGeometry(QtCore.QRect(180, 240, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(21)
        self.DepositButton.setFont(font)
        self.DepositButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DepositButton.setObjectName("DepositButton")
        Deposit.setCentralWidget(self.centralwidget)

        self.retranslateUi(Deposit)
        QtCore.QMetaObject.connectSlotsByName(Deposit)
        self.Back_Button.clicked.connect(self.Go_Back)
        self.DepositButton.clicked.connect(self.Depositing_Amount)

    def Depositing_Amount(self):
        try:
            if not Internet_Available():
                raise No_Internet
            if "," in self.Amount.text() or "-" in self.Amount.text() or self.Amount.text() == "":
                raise Invalid_Amount
        except No_Internet:
            Error_Message(2)
        except Invalid_Amount:
            Error_Message(12)
        else:
            Success_Message(10)
            global user_data
            amount = int(self.Amount.text())
            user_data[4] = str(int(user_data[4]) + 1)
            user_data[3] = str(int(user_data[3]) + amount)
            Modify_Content_In_File(user_data)
            Write_To_Passbook(0, Get_User_Position(user_data[1]), str(amount), user_data[3])
            Transactional_Email(0, user_data, str(amount))
            Success_Message(11)
            Payments.show()
            Deposit.hide()

    def Go_Back(self):
        Payments.show()
        Deposit.hide()

    def retranslateUi(self, Deposit):
        _translate = QtCore.QCoreApplication.translate
        Deposit.setWindowTitle(_translate("Deposit", "Deposit"))
        self.Back_Button.setToolTip(_translate("Deposit", "<html><head/><body><p><span style=\" font-weight:600;\">Back To Payments</span></p></body></html>"))
        self.label_3.setText(_translate("Deposit", "<html><head/><body><p><span style=\" color:#ffffff;\">Account Balance</span></p></body></html>"))
        self.label_4.setText(_translate("Deposit", "<html><head/><body><p><span style=\" color:#ffffff;\">Amount</span></p></body></html>"))
        self.Balance.setToolTip(_translate("Deposit", "<html><head/><body><p><span style=\" font-weight:600;\">Current Account Balance</span></p></body></html>"))
        self.Amount.setToolTip(_translate("Deposit", "<html><head/><body><p><span style=\" font-weight:600;\">Amount To Deposit</span></p></body></html>"))
        self.DepositButton.setToolTip(_translate("Deposit", "<html><head/><body><p><span style=\" font-weight:600;\">Deposit Amount To Account</span></p></body></html>"))
        self.DepositButton.setText(_translate("Deposit", "Deposit"))


class Ui_Details_Of_SUser(object):
    def setupUi(self, Details_Of_SUser):
        global dummy_user
        Details_Of_SUser.setObjectName("Details_Of_SUser")
        Details_Of_SUser.resize(600, 400)
        Details_Of_SUser.setMinimumSize(QtCore.QSize(600, 400))
        Details_Of_SUser.setMaximumSize(QtCore.QSize(600, 400))
        Details_Of_SUser.setBaseSize(QtCore.QSize(600, 400))
        Details_Of_SUser.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Details_Of_SUser.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Details_Of_SUser)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Back_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Back_Button.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.Back_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_Button.setIcon(icon1)
        self.Back_Button.setObjectName("Back_Button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 0, 120, 120))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/users.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 130, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(330, 140, 191, 31))
        self.Name.setObjectName("Name")
        self.Name.setText(dummy_user[0])
        self.Name.setReadOnly(True)
        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(330, 200, 191, 31))
        self.Username.setObjectName("Username")
        self.Username.setText(dummy_user[1])
        self.Username.setReadOnly(True)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 190, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Member_Since = QtWidgets.QLineEdit(self.centralwidget)
        self.Member_Since.setGeometry(QtCore.QRect(330, 260, 191, 31))
        self.Member_Since.setObjectName("Member_Since")
        self.Member_Since.setText(dummy_user[5])
        self.Member_Since.setReadOnly(True)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 250, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        Details_Of_SUser.setCentralWidget(self.centralwidget)

        self.retranslateUi(Details_Of_SUser)
        QtCore.QMetaObject.connectSlotsByName(Details_Of_SUser)
        self.Back_Button.clicked.connect(self.Back_To_All_Users)

    def Back_To_All_Users(self):
        Available_Users.show()
        Details_Of_SUser.hide()

    def retranslateUi(self, Details_Of_SUser):
        _translate = QtCore.QCoreApplication.translate
        Details_Of_SUser.setWindowTitle(_translate("Details_Of_SUser", "Detail Of The User"))
        self.Back_Button.setToolTip(_translate("Details_Of_SUser", "<html><head/><body><p><span style=\" font-weight:600;\">Back To All Users</span></p></body></html>"))
        self.label_3.setText(_translate("Details_Of_SUser", "<html><head/><body><p><span style=\" color:#ffffff;\">Name</span></p></body></html>"))
        self.label_4.setText(_translate("Details_Of_SUser", "<html><head/><body><p><span style=\" color:#ffffff;\">Username</span></p></body></html>"))
        self.label_5.setText(_translate("Details_Of_SUser", "<html><head/><body><p><span style=\" color:#ffffff;\">Member Since</span></p></body></html>"))


class Ui_Available_Users(object):
    def setupUi(self, Available_Users):
        Available_Users.setObjectName("Available_Users")
        Available_Users.resize(500, 500)
        Available_Users.setMinimumSize(QtCore.QSize(500, 500))
        Available_Users.setMaximumSize(QtCore.QSize(500, 500))
        Available_Users.setBaseSize(QtCore.QSize(500, 500))
        Available_Users.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Available_Users.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Available_Users)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.BackButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.BackButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon1)
        self.BackButton.setObjectName("BackButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, -10, 120, 120))
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/users.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.UsersWidget = QtWidgets.QListWidget(self.centralwidget)
        self.UsersWidget.setGeometry(QtCore.QRect(30, 130, 441, 281))
        self.UsersWidget.setObjectName("UsersWidget")
        for x in Retreive_All_Users_Names():
            self.UsersWidget.addItem(x)
        self.ViewDetailsButton = QtWidgets.QPushButton(self.centralwidget)
        self.ViewDetailsButton.setGeometry(QtCore.QRect(170, 430, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(18)
        self.ViewDetailsButton.setFont(font)
        self.ViewDetailsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ViewDetailsButton.setObjectName("ViewDetailsButton")
        Available_Users.setCentralWidget(self.centralwidget)

        self.retranslateUi(Available_Users)
        QtCore.QMetaObject.connectSlotsByName(Available_Users)
        self.BackButton.clicked.connect(self.Back_To_Menu)
        self.ViewDetailsButton.clicked.connect(self.Showing_Details_Of_Selected_User)

    def Showing_Details_Of_Selected_User(self):
        try:
            current_user = self.UsersWidget.currentItem().text()
        except:
            pass
        else:
            global dummy_user, ui11
            dummy_user = Retrieve_Users_Data(current_user)
            ui11.setupUi(Details_Of_SUser)
            Details_Of_SUser.show()
            Available_Users.hide()

    def Back_To_Menu(self):
        After_Log_In.show()
        Available_Users.hide()

    def retranslateUi(self, Available_Users):
        _translate = QtCore.QCoreApplication.translate
        Available_Users.setWindowTitle(_translate("Available_Users", "All Users"))
        self.BackButton.setToolTip(_translate("Available_Users", "<html><head/><body><p><span style=\" font-weight:600;\">Back To Menu</span></p></body></html>"))
        self.ViewDetailsButton.setToolTip(_translate("Available_Users", "<html><head/><body><p><span style=\" font-weight:600;\">View Details</span></p></body></html>"))
        self.ViewDetailsButton.setText(_translate("Available_Users", "View Details"))


class Ui_Payments(object):
    def setupUi(self, Payments):
        Payments.setObjectName("Payments")
        Payments.resize(500, 300)
        Payments.setMinimumSize(QtCore.QSize(500, 300))
        Payments.setMaximumSize(QtCore.QSize(500, 300))
        Payments.setBaseSize(QtCore.QSize(500, 300))
        Payments.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Payments.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Payments)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 500, 300))
        self.background.setMinimumSize(QtCore.QSize(500, 300))
        self.background.setMaximumSize(QtCore.QSize(500, 300))
        self.background.setBaseSize(QtCore.QSize(500, 300))
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 50, 161, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/passbook.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 39, 111, 91))
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/add.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 170, 111, 91))
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/minus.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 170, 111, 91))
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/send.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.PassBookButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.PassBookButton.setGeometry(QtCore.QRect(80, 50, 161, 81))
        self.PassBookButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PassBookButton.setIcon(icon1)
        self.PassBookButton.setObjectName("PassBookButton")
        self.DepositButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.DepositButton.setGeometry(QtCore.QRect(330, 40, 111, 91))
        self.DepositButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DepositButton.setIcon(icon1)
        self.DepositButton.setObjectName("DepositButton")
        self.WithdrawButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.WithdrawButton.setGeometry(QtCore.QRect(100, 200, 111, 31))
        self.WithdrawButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.WithdrawButton.setIcon(icon1)
        self.WithdrawButton.setObjectName("WithdrawButton")
        self.TransferMoney = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.TransferMoney.setGeometry(QtCore.QRect(330, 180, 111, 71))
        self.TransferMoney.setFocusPolicy(QtCore.Qt.NoFocus)
        self.TransferMoney.setText("")
        self.TransferMoney.setIcon(icon1)
        self.TransferMoney.setObjectName("TransferMoney")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.BackButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.BackButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.BackButton.setIcon(icon1)
        self.BackButton.setObjectName("BackButton")
        Payments.setCentralWidget(self.centralwidget)

        self.retranslateUi(Payments)
        QtCore.QMetaObject.connectSlotsByName(Payments)
        self.BackButton.clicked.connect(self.Back_To_Home)
        self.DepositButton.clicked.connect(self.Take_To_Deposit)
        self.WithdrawButton.clicked.connect(self.Take_To_Withdraw)
        self.PassBookButton.clicked.connect(self.Take_To_Passbook)
        self.TransferMoney.clicked.connect(self.Take_To_Transfer)

    def Take_To_Transfer(self):
        global ui15
        ui15.setupUi(TransferMoney)
        TransferMoney.show()
        Payments.hide()

    def Take_To_Passbook(self):
        global ui14
        ui14.setupUi(Passbook)
        Passbook.show()
        Payments.hide()

    def Take_To_Deposit(self):
        global ui12
        ui12.setupUi(Deposit)
        Deposit.show()
        Payments.hide()

    def Take_To_Withdraw(self):
        global ui13
        ui13.setupUi(Withdraw)
        Withdraw.show()
        Payments.hide()

    def Back_To_Home(self):
        After_Log_In.show()
        Payments.hide()

    def retranslateUi(self, Payments):
        _translate = QtCore.QCoreApplication.translate
        Payments.setWindowTitle(_translate("Payments", "Payments"))
        self.PassBookButton.setToolTip(_translate("Payments", "<html><head/><body><p><span style=\" font-weight:600;\">View Passbook</span></p></body></html>"))
        self.DepositButton.setToolTip(_translate("Payments", "<html><head/><body><p><span style=\" font-weight:600;\">Deposit Money</span></p></body></html>"))
        self.WithdrawButton.setToolTip(_translate("Payments", "<html><head/><body><p><span style=\" font-weight:600;\">Withdraw Money</span></p></body></html>"))
        self.TransferMoney.setToolTip(_translate("Payments", "<html><head/><body><p><span style=\" font-weight:600;\">Transfer Money</span></p></body></html>"))
        self.BackButton.setToolTip(_translate("Payments", "<html><head/><body><p><span style=\" font-weight:600;\">Back To Menu</span></p></body></html>"))


class Ui_DP_Settings(object):
    def setupUi(self, DP_Settings):
        global user_data
        DP_Settings.setObjectName("DP_Settings")
        DP_Settings.resize(600, 600)
        DP_Settings.setMinimumSize(QtCore.QSize(600, 600))
        DP_Settings.setMaximumSize(QtCore.QSize(600, 600))
        DP_Settings.setBaseSize(QtCore.QSize(600, 600))
        DP_Settings.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DP_Settings.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(DP_Settings)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/user.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Back_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Back_Button.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.Back_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Back_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_Button.setIcon(icon1)
        self.Back_Button.setObjectName("Back_Button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 120, 120))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/settings_icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 190, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(260, 200, 191, 31))
        self.Name.setObjectName("Name")
        self.Name.setText(user_data[0])
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 250, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(260, 260, 191, 31))
        self.Username.setObjectName("Username")
        self.Username.setText(user_data[1])
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 310, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Name_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.Name_3.setGeometry(QtCore.QRect(260, 320, 191, 31))
        self.Name_3.setObjectName("Name_3")
        self.Name_3.setText(user_data[2])
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 370, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.Name_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.Name_4.setGeometry(QtCore.QRect(260, 380, 191, 31))
        self.Name_4.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.Name_4.setObjectName("Name_4")
        self.Name_4.setText(user_data[-1])
        self.Change_Name = QtWidgets.QPushButton(self.centralwidget)
        self.Change_Name.setEnabled(False)
        self.Change_Name.setGeometry(QtCore.QRect(490, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        self.Change_Name.setFont(font)
        self.Change_Name.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Change_Name.setObjectName("Change_Name")
        self.Change_Username = QtWidgets.QPushButton(self.centralwidget)
        self.Change_Username.setEnabled(False)
        self.Change_Username.setGeometry(QtCore.QRect(490, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        self.Change_Username.setFont(font)
        self.Change_Username.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Change_Username.setObjectName("Change_Username")
        self.Change_Email = QtWidgets.QPushButton(self.centralwidget)
        self.Change_Email.setEnabled(False)
        self.Change_Email.setGeometry(QtCore.QRect(490, 320, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        self.Change_Email.setFont(font)
        self.Change_Email.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Change_Email.setObjectName("Change_Email")
        self.Change_Name_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Change_Name_4.setEnabled(False)
        self.Change_Name_4.setGeometry(QtCore.QRect(490, 380, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        self.Change_Name_4.setFont(font)
        self.Change_Name_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Change_Name_4.setObjectName("Change_Name_4")
        DP_Settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(DP_Settings)
        QtCore.QMetaObject.connectSlotsByName(DP_Settings)
        self.Back_Button.clicked.connect(self.Go_To_Profile)

        self.Name.textChanged.connect(self.Name_Edited)
        self.Username.textChanged.connect(self.Username_Edited)
        self.Name_3.textChanged.connect(self.Email_Edited)
        self.Name_4.textChanged.connect(self.Password_Edited)

        self.Change_Name.clicked.connect(self.Changing_Name)
        self.Change_Email.clicked.connect(self.Changing_Email)
        self.Change_Username.clicked.connect(self.Changing_Username)
        self.Change_Name_4.clicked.connect(self.Changing_Password)

    def Changing_Name(self):
        global user_data
        user_data[0] = self.Name.text()
        self.Change_Name.setEnabled(False)
        Overwrite_Data(user_data)
        Success_Message(5)

    def Changing_Email(self):
        if Check_For_Availabilty(2, self.Name_3.text()):
            Error_Message(1)
        else:
            global user_data
            user_data[2] = self.Name_3.text()
            self.Change_Email.setEnabled(False)
            Overwrite_Data(user_data)
            Success_Message(6)

    def Changing_Username(self):
        if Check_For_Availabilty(1, self.Username.text()):
            Error_Message(5)
        else:
            global user_data
            user_data[1] = self.Username.text()
            self.Change_Username.setEnabled(False)
            Overwrite_Data(user_data, 1)
            Success_Message(7)

    def Changing_Password(self):
        global user_data
        user_data[-1] = self.Name_4.text()
        self.Change_Name_4.setEnabled(False)
        Overwrite_Data(user_data)
        Success_Message(8)

    def Name_Edited(self):
        global user_data
        if self.Name.text() != "" and self.Name.text() != user_data[0]:
            self.Change_Name.setEnabled(True)
        else:
            self.Change_Name.setEnabled(False)

    def Username_Edited(self):
        global user_data
        if self.Username.text() != "" and self.Username.text() != user_data[1]:
            self.Change_Username.setEnabled(True)
        else:
            self.Change_Username.setEnabled(False)

    def Email_Edited(self):
        global user_data
        if self.Name_3.text() != "" and self.Name_3.text() != user_data[2]:
            self.Change_Email.setEnabled(True)
        else:
            self.Change_Email.setEnabled(False)

    def Password_Edited(self):
        global user_data
        if self.Name_4.text() != "" and self.Name_4.text() != user_data[-1]:
            self.Change_Name_4.setEnabled(True)
        else:
            self.Change_Name_4.setEnabled(False)

    def Go_To_Profile(self):
        global ui7
        ui7.setupUi(Profile_Window)
        Profile_Window.show()
        DP_Settings.hide()

    def retranslateUi(self, DP_Settings):
        _translate = QtCore.QCoreApplication.translate
        DP_Settings.setWindowTitle(_translate("DP_Settings", "Settings Window"))
        self.Back_Button.setToolTip(_translate("DP_Settings", "<html><head/><body><p><span style=\" font-weight:600;\">Back To Profile</span></p></body></html>"))
        self.label_3.setText(_translate("DP_Settings", "<html><head/><body><p><span style=\" color:#ffffff;\">Name</span></p></body></html>"))
        self.Name.setToolTip(_translate("DP_Settings", "<html><head/><body><p><span style=\" font-weight:600;\">Your Name</span></p></body></html>"))
        self.label_4.setText(_translate("DP_Settings", "<html><head/><body><p><span style=\" color:#ffffff;\">Username</span></p></body></html>"))
        self.Username.setToolTip(_translate("DP_Settings", "<html><head/><body><p><span style=\" font-weight:600;\">Your Username</span></p></body></html>"))
        self.label_5.setText(_translate("DP_Settings", "<html><head/><body><p><span style=\" color:#ffffff;\">Email</span></p></body></html>"))
        self.Name_3.setToolTip(_translate("DP_Settings", "<html><head/><body><p><span style=\" font-weight:600;\">Your Email Address</span></p></body></html>"))
        self.label_6.setText(_translate("DP_Settings", "<html><head/><body><p><span style=\" color:#ffffff;\">Password</span></p></body></html>"))
        self.Name_4.setToolTip(_translate("DP_Settings", "<html><head/><body><p><span style=\" font-weight:600;\">Your Password</span></p></body></html>"))
        self.Change_Name.setToolTip(_translate("DP_Settings", "<html><head/><body><p><span style=\" font-weight:600;\">Change Name</span></p></body></html>"))
        self.Change_Name.setText(_translate("DP_Settings", "Change"))
        self.Change_Username.setToolTip(_translate("DP_Settings", "<html><head/><body><p><span style=\" font-weight:600;\">Change Username</span></p></body></html>"))
        self.Change_Username.setText(_translate("DP_Settings", "Change"))
        self.Change_Email.setToolTip(_translate("DP_Settings", "<html><head/><body><p><span style=\" font-weight:600;\">Change Email Address</span></p></body></html>"))
        self.Change_Email.setText(_translate("DP_Settings", "Change"))
        self.Change_Name_4.setToolTip(_translate("DP_Settings", "<html><head/><body><p><span style=\" font-weight:600;\">Change Password</span></p></body></html>"))
        self.Change_Name_4.setText(_translate("DP_Settings", "Change"))


class Ui_Profile_Window(object):
    def setupUi(self, Profile_Window):
        global user_data
        Profile_Window.setObjectName("Profile_Window")
        Profile_Window.resize(600, 600)
        Profile_Window.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(Profile_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 10, 120, 120))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/user.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(60, 220, 201, 31))
        self.Name.setClearButtonEnabled(False)
        self.Name.setObjectName("Name")
        self.Name.setText(user_data[0])
        self.Name.setReadOnly(True)
        self.CPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.CPassword.setGeometry(QtCore.QRect(60, 360, 201, 31))
        self.CPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.CPassword.setClearButtonEnabled(False)
        self.CPassword.setObjectName("CPassword")
        self.CPassword.setText(user_data[5])
        self.CPassword.setReadOnly(True)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 320, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(350, 220, 201, 31))
        self.Username.setClearButtonEnabled(False)
        self.Username.setObjectName("Username")
        self.Username.setText(user_data[1])
        self.Username.setReadOnly(True)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 250, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.Email = QtWidgets.QLineEdit(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(60, 290, 201, 31))
        self.Email.setClearButtonEnabled(False)
        self.Email.setObjectName("Email")
        self.Email.setText(user_data[2])
        self.Email.setReadOnly(True)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 320, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(350, 360, 201, 31))
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setClearButtonEnabled(False)
        self.Password.setObjectName("Password")
        self.Password.setText(user_data[-1])
        self.Password.setReadOnly(True)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(400, 250, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.VCCode = QtWidgets.QLineEdit(self.centralwidget)
        self.VCCode.setGeometry(QtCore.QRect(350, 290, 201, 31))
        self.VCCode.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.VCCode.setClearButtonEnabled(False)
        self.VCCode.setObjectName("VCCode")
        self.VCCode.setText(user_data[3] + " Rs")
        self.VCCode.setReadOnly(True)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 180, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 450, 120, 120))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/settings_icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.SettingsButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.SettingsButton.setGeometry(QtCore.QRect(240, 440, 121, 131))
        self.SettingsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.SettingsButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SettingsButton.setIcon(icon)
        self.SettingsButton.setObjectName("SettingsButton")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.ExitButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.ExitButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ExitButton.setText("")
        self.ExitButton.setIcon(icon)
        self.ExitButton.setObjectName("ExitButton")
        Profile_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Profile_Window)
        QtCore.QMetaObject.connectSlotsByName(Profile_Window)
        self.ExitButton.clicked.connect(self.Back_To_Lobby)
        self.SettingsButton.clicked.connect(self.Go_To_Settings)

    def Go_To_Settings(self):
        global ui8
        ui8.setupUi(DP_Settings)
        DP_Settings.show()
        Profile_Window.hide()

    def Back_To_Lobby(self):
        After_Log_In.show()
        Profile_Window.hide()

    def retranslateUi(self, Profile_Window):
        _translate = QtCore.QCoreApplication.translate
        Profile_Window.setWindowTitle(_translate("Profile_Window", "MainWindow"))
        self.Name.setToolTip(_translate("Profile_Window", "<html><head/><body><p><span style=\" font-weight:600;\">Your Name</span></p></body></html>"))
        self.CPassword.setToolTip(_translate("Profile_Window", "<html><head/><body><p><span style=\" font-weight:600;\">Your Account Creation Time And Date</span></p></body></html>"))
        self.label_5.setText(_translate("Profile_Window", "<html><head/><body><p><span style=\" color:#ffffff;\">Password</span></p></body></html>"))
        self.Username.setToolTip(_translate("Profile_Window", "<html><head/><body><p><span style=\" font-weight:600;\">Your Username</span></p></body></html>"))
        self.label_7.setText(_translate("Profile_Window", "<html><head/><body><p><span style=\" color:#ffffff;\">Email</span></p></body></html>"))
        self.Email.setToolTip(_translate("Profile_Window", "<html><head/><body><p><span style=\" font-weight:600;\">Your Email Address</span></p></body></html>"))
        self.label_6.setText(_translate("Profile_Window", "<html><head/><body><p><span style=\" color:#ffffff;\">Member Since</span></p></body></html>"))
        self.Password.setToolTip(_translate("Profile_Window", "<html><head/><body><p><span style=\" font-weight:600;\">Your Password</span></p></body></html>"))
        self.label_4.setText(_translate("Profile_Window", "<html><head/><body><p><span style=\" color:#ffffff;\">Username</span></p></body></html>"))
        self.label_8.setText(_translate("Profile_Window", "<html><head/><body><p><span style=\" color:#ffffff;\">Balance</span></p></body></html>"))
        self.VCCode.setToolTip(_translate("Profile_Window", "<html><head/><body><p><span style=\" font-weight:600;\">Your Account Balance</span></p></body></html>"))
        self.label_3.setText(_translate("Profile_Window", "<html><head/><body><p><span style=\" color:#ffffff;\">Name</span></p></body></html>"))
        self.SettingsButton.setToolTip(_translate("Profile_Window", "<html><head/><body><p><span style=\" font-weight:600;\">Change Details</span></p></body></html>"))
        self.ExitButton.setToolTip(_translate("Profile_Window", "<html><head/><body><p><span style=\" font-weight:600;\">Exit To Lobby</span></p></body></html>"))


class Ui_After_Log_In(object):
    def setupUi(self, After_Log_In):
        After_Log_In.setObjectName("After_Log_In")
        After_Log_In.resize(500, 300)
        After_Log_In.setMinimumSize(QtCore.QSize(500, 300))
        After_Log_In.setMaximumSize(QtCore.QSize(500, 300))
        After_Log_In.setBaseSize(QtCore.QSize(500, 300))
        After_Log_In.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(After_Log_In)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 120, 120))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/user.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 120, 120))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/users.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 150, 120, 120))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/payments.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 140, 120, 120))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/log_off.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.profile_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.profile_button.setGeometry(QtCore.QRect(90, 20, 121, 101))
        self.profile_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.profile_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profile_button.setIcon(icon)
        self.profile_button.setObjectName("profile_button")
        self.users_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.users_button.setGeometry(QtCore.QRect(270, 40, 121, 71))
        self.users_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.users_button.setText("")
        self.users_button.setIcon(icon)
        self.users_button.setObjectName("users_button")
        self.payments_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.payments_button.setGeometry(QtCore.QRect(90, 160, 121, 101))
        self.payments_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.payments_button.setText("")
        self.payments_button.setIcon(icon)
        self.payments_button.setObjectName("payments_button")
        self.logout_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.logout_button.setGeometry(QtCore.QRect(270, 140, 121, 121))
        self.logout_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.logout_button.setText("")
        self.logout_button.setIcon(icon)
        self.logout_button.setObjectName("logout_button")
        After_Log_In.setCentralWidget(self.centralwidget)

        self.retranslateUi(After_Log_In)
        QtCore.QMetaObject.connectSlotsByName(After_Log_In)
        self.logout_button.clicked.connect(self.Back_To_Login_Page)
        self.profile_button.clicked.connect(self.Take_To_Profile)
        self.payments_button.clicked.connect(self.Take_To_Payments)
        self.users_button.clicked.connect(self.Take_To_All_Users)

    def Take_To_All_Users(self):
        global ui10
        ui10.setupUi(Available_Users)
        Available_Users.show()
        After_Log_In.hide()

    def Take_To_Payments(self):
        global ui9
        ui9.setupUi(Payments)
        Payments.show()
        After_Log_In.hide()

    def Take_To_Profile(self):
        global ui7
        ui7.setupUi(Profile_Window)
        Profile_Window.show()
        After_Log_In.hide()

    def Back_To_Login_Page(self):
        Login_Form.show()
        After_Log_In.hide()

    def retranslateUi(self, After_Log_In):
        _translate = QtCore.QCoreApplication.translate
        After_Log_In.setWindowTitle(_translate("After_Log_In", "MainWindow"))
        self.profile_button.setToolTip(_translate("After_Log_In", "<html><head/><body><p><span style=\" font-weight:600;\">Profile</span></p></body></html>"))
        self.users_button.setToolTip(_translate("After_Log_In", "<html><head/><body><p><span style=\" font-weight:600;\">Users</span></p></body></html>"))
        self.payments_button.setToolTip(_translate("After_Log_In", "<html><head/><body><p><span style=\" font-weight:600;\">Payments</span></p></body></html>"))
        self.logout_button.setToolTip(_translate("After_Log_In", "<html><head/><body><p><span style=\" font-weight:600;\">Log Out</span></p></body></html>"))


class Ui_PasswordReset(object):
    def setupUi(self, PasswordReset):
        PasswordReset.setObjectName("PasswordReset")
        PasswordReset.resize(350, 350)
        PasswordReset.setMinimumSize(QtCore.QSize(350, 350))
        PasswordReset.setMaximumSize(QtCore.QSize(350, 350))
        PasswordReset.setBaseSize(QtCore.QSize(350, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PasswordReset.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(PasswordReset)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 350, 350))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 0, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(80, 50, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(70, 170, 201, 31))
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setClearButtonEnabled(True)
        self.Password.setObjectName("Password")
        self.VCCode = QtWidgets.QLineEdit(self.centralwidget)
        self.VCCode.setGeometry(QtCore.QRect(70, 90, 201, 31))
        self.VCCode.setMaxLength(6)
        self.VCCode.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.VCCode.setClearButtonEnabled(True)
        self.VCCode.setObjectName("VCCode")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 210, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.CPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.CPassword.setGeometry(QtCore.QRect(70, 250, 201, 31))
        self.CPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CPassword.setClearButtonEnabled(True)
        self.CPassword.setObjectName("CPassword")
        self.ResetButton = QtWidgets.QPushButton(self.centralwidget)
        self.ResetButton.setGeometry(QtCore.QRect(100, 290, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        self.ResetButton.setFont(font)
        self.ResetButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ResetButton.setObjectName("ResetButton")
        PasswordReset.setCentralWidget(self.centralwidget)

        self.retranslateUi(PasswordReset)
        QtCore.QMetaObject.connectSlotsByName(PasswordReset)
        self.ResetButton.clicked.connect(self.Resetting_Password)

    def Resetting_Password(self):
        try:
            global vcc
            if vcc != self.VCCode.text():
                raise Wrong_VCCode
            if self.Password.text() != self.CPassword.text():
                raise Password_Did_Not_Match
        except Wrong_VCCode:
            Error_Message(8)
        except Password_Did_Not_Match:
            Error_Message(7)
        else:
            global user_email
            Reset_Password(user_email, self.Password.text())
            Success_Message(4)
            PasswordReset.hide()

    def retranslateUi(self, PasswordReset):
        _translate = QtCore.QCoreApplication.translate
        PasswordReset.setWindowTitle(_translate("PasswordReset", "Reset Password"))
        self.label.setText(_translate("PasswordReset", "<html><head/><body><p><span style=\" color:#00ff00;\">Password Reset</span></p></body></html>"))
        self.label_8.setText(_translate("PasswordReset", "<html><head/><body><p><span style=\" color:#ffffff;\">Verification Code</span></p></body></html>"))
        self.Password.setToolTip(_translate("PasswordReset", "<html><head/><body><p><span style=\" font-weight:600;\">Your Password</span></p></body></html>"))
        self.VCCode.setToolTip(_translate("PasswordReset", "<html><head/><body><p><span style=\" font-weight:600;\">Verification Code</span></p></body></html>"))
        self.VCCode.setPlaceholderText(_translate("PasswordReset", "Eg: 475326"))
        self.label_5.setText(_translate("PasswordReset", "<html><head/><body><p><span style=\" color:#ffffff;\">Password</span></p></body></html>"))
        self.label_6.setText(_translate("PasswordReset", "<html><head/><body><p><span style=\" color:#ffffff;\">Confirm Password</span></p></body></html>"))
        self.CPassword.setToolTip(_translate("PasswordReset", "<html><head/><body><p><span style=\" font-weight:600;\">Your Password</span></p></body></html>"))
        self.ResetButton.setToolTip(_translate("PasswordReset", "<html><head/><body><p><span style=\" font-weight:600;\">Reset Password</span></p></body></html>"))
        self.ResetButton.setText(_translate("PasswordReset", "Reset"))


class Ui_Login_Form(object):
    def setupUi(self, Login_Form):
        Login_Form.setObjectName("Login_Form")
        Login_Form.resize(400, 400)
        Login_Form.setMinimumSize(QtCore.QSize(400, 400))
        Login_Form.setMaximumSize(QtCore.QSize(400, 400))
        Login_Form.setBaseSize(QtCore.QSize(600, 600))
        Login_Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login_Form.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Login_Form)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 400, 400))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.ExitButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.ExitButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ExitButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExitButton.setIcon(icon1)
        self.ExitButton.setObjectName("ExitButton")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(150, 10, 71, 71))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 80, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 120, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 200, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Username_Email = QtWidgets.QLineEdit(self.centralwidget)
        self.Username_Email.setGeometry(QtCore.QRect(90, 160, 201, 31))
        self.Username_Email.setClearButtonEnabled(True)
        self.Username_Email.setObjectName("Username_Email")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(90, 240, 201, 31))
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setClearButtonEnabled(True)
        self.Password.setObjectName("Password")
        self.KeepButton = QtWidgets.QRadioButton(self.centralwidget)
        self.KeepButton.setGeometry(QtCore.QRect(90, 280, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        self.KeepButton.setFont(font)
        self.KeepButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.KeepButton.setIconSize(QtCore.QSize(41, 16))
        self.KeepButton.setObjectName("KeepButton")
        self.LogInButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogInButton.setGeometry(QtCore.QRect(120, 320, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        self.LogInButton.setFont(font)
        self.LogInButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LogInButton.setObjectName("LogInButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 355, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ForgotButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.ForgotButton.setGeometry(QtCore.QRect(20, 360, 361, 21))
        self.ForgotButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ForgotButton.setText("")
        self.ForgotButton.setIcon(icon1)
        self.ForgotButton.setObjectName("ForgotButton")
        self.background.raise_()
        self.logo.raise_()
        self.label.raise_()
        self.ExitButton.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.Username_Email.raise_()
        self.Password.raise_()
        self.KeepButton.raise_()
        self.LogInButton.raise_()
        self.label_3.raise_()
        self.ForgotButton.raise_()
        Login_Form.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login_Form)
        QtCore.QMetaObject.connectSlotsByName(Login_Form)
        self.ExitButton.clicked.connect(self.Back_To_Main_Page)
        self.LogInButton.clicked.connect(self.Take_To_Account)
        self.ForgotButton.clicked.connect(self.Password_Reset)

    def Password_Reset(self):
        try:
            if not Internet_Available():
                raise No_Internet
            if not Check_For_Availabilty(2, self.Username_Email.text()):
                raise No_User
        except No_Internet:
            Error_Message(2)
        except No_User:
            Error_Message(10)
        else:
            global user_email, vcc
            user_email = self.Username_Email.text()
            vcc = Generate_Verification_Code()
            Send_Password_Code(user_email, vcc)
            Success_Message(0)
            global ui5
            ui5.setupUi(PasswordReset)
            PasswordReset.show()

    def Take_To_Account(self):
        try:
            if not Check_True_User(self.Username_Email.text(), self.Password.text()):
                raise No_User
        except No_User:
            Error_Message(11)
        else:
            Success_Message(3)
            if not self.KeepButton.isChecked():
                self.Username_Email.clear()
                self.Password.clear()
            global user_data
            user_data = Retrieve_Users_Data(self.Username_Email.text())
            global ui6
            ui6.setupUi(After_Log_In)
            After_Log_In.show()
            Login_Form.hide()

    def Back_To_Main_Page(self):
        if not self.KeepButton.isChecked():
            self.Username_Email.clear()
            self.Password.clear()
        After_Splash.show()
        Login_Form.hide()

    def retranslateUi(self, Login_Form):
        _translate = QtCore.QCoreApplication.translate
        Login_Form.setWindowTitle(_translate("Login_Form", "Log In"))
        self.ExitButton.setToolTip(_translate("Login_Form", "<html><head/><body><p><span style=\" font-weight:600;\">Exit To Main Page</span></p></body></html>"))
        self.label_2.setText(_translate("Login_Form", "<html><head/><body><p><span style=\" color:#00ff7f;\">Log In</span></p></body></html>"))
        self.label_4.setText(_translate("Login_Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Username/Email</span></p></body></html>"))
        self.label_5.setText(_translate("Login_Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Password</span></p></body></html>"))
        self.Username_Email.setToolTip(_translate("Login_Form", "<html><head/><body><p><span style=\" font-weight:600;\">Enter Username Or Email Address</span></p></body></html>"))
        self.Username_Email.setPlaceholderText(_translate("Login_Form", "Eg: Tim Or tim@abc.co.in"))
        self.Password.setToolTip(_translate("Login_Form", "<html><head/><body><p><span style=\" font-weight:600;\">Enter Password</span></p></body></html>"))
        self.KeepButton.setToolTip(_translate("Login_Form", "<html><head/><body><p><span style=\" font-weight:600;\">This Would Keep You Signed In</span></p></body></html>"))
        self.KeepButton.setText(_translate("Login_Form", "Keep Me Signed In"))
        self.LogInButton.setToolTip(_translate("Login_Form", "<html><head/><body><p><span style=\" font-weight:600;\">Log In To Your Account</span></p></body></html>"))
        self.LogInButton.setText(_translate("Login_Form", "Log In"))
        self.label_3.setText(_translate("Login_Form", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Forgot Password ? Click Here To Reset Password</span></p></body></html>"))
        self.ForgotButton.setToolTip(_translate("Login_Form", "<html><head/><body><p><span style=\" font-weight:600;\">Enter Your Email Address In The Username/Email Field Before Clicking Here</span></p></body></html>"))


class Ui_Register_Form(object):
    def setupUi(self, Register_Form):
        Register_Form.setObjectName("Register_Form")
        Register_Form.resize(600, 600)
        Register_Form.setMinimumSize(QtCore.QSize(600, 600))
        Register_Form.setMaximumSize(QtCore.QSize(600, 600))
        Register_Form.setBaseSize(QtCore.QSize(600, 600))
        Register_Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Register_Form.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Register_Form)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(240, 10, 121, 121))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.ExitButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.ExitButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ExitButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExitButton.setIcon(icon1)
        self.ExitButton.setObjectName("ExitButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 140, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(21)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 190, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(50, 230, 201, 31))
        self.Name.setClearButtonEnabled(True)
        self.Name.setObjectName("Name")
        self.Name.setText(Get_System_Owner_Name())
        self.Username = QtWidgets.QLineEdit(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(340, 230, 201, 31))
        self.Username.setClearButtonEnabled(True)
        self.Username.setObjectName("Username")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 270, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(50, 310, 201, 31))
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setClearButtonEnabled(True)
        self.Password.setObjectName("Password")
        self.CPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.CPassword.setGeometry(QtCore.QRect(340, 310, 201, 31))
        self.CPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CPassword.setClearButtonEnabled(True)
        self.CPassword.setObjectName("CPassword")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(350, 270, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.Email = QtWidgets.QLineEdit(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(50, 380, 201, 31))
        self.Email.setClearButtonEnabled(True)
        self.Email.setObjectName("Email")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 340, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.VCCode = QtWidgets.QLineEdit(self.centralwidget)
        self.VCCode.setGeometry(QtCore.QRect(340, 380, 201, 31))
        self.VCCode.setMaxLength(6)
        self.VCCode.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.VCCode.setClearButtonEnabled(True)
        self.VCCode.setObjectName("VCCode")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(350, 340, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.GetCodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.GetCodeButton.setGeometry(QtCore.QRect(200, 420, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        self.GetCodeButton.setFont(font)
        self.GetCodeButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.GetCodeButton.setObjectName("GetCodeButton")
        self.AgreeButton = QtWidgets.QRadioButton(self.centralwidget)
        self.AgreeButton.setGeometry(QtCore.QRect(50, 466, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        self.AgreeButton.setFont(font)
        self.AgreeButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.AgreeButton.setIconSize(QtCore.QSize(41, 16))
        self.AgreeButton.setObjectName("AgreeButton")
        self.RegisterButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegisterButton.setGeometry(QtCore.QRect(170, 520, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(16)
        self.RegisterButton.setFont(font)
        self.RegisterButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.RegisterButton.setObjectName("RegisterButton")
        Register_Form.setCentralWidget(self.centralwidget)

        self.retranslateUi(Register_Form)
        QtCore.QMetaObject.connectSlotsByName(Register_Form)
        self.ExitButton.clicked.connect(self.Back_To_Main_Page)
        self.GetCodeButton.clicked.connect(self.Sending_Verification_Code)
        self.RegisterButton.clicked.connect(self.Complete_The_Registration)

    def Complete_The_Registration(self):
        try:
            if not Internet_Available:
                raise No_Internet
            if self.Name.text() == "":
                raise Invalid_Name
            if self.Username.text() == "":
                raise Invalid_Username
            if Check_For_Availabilty(1, self.Username.text()):
                raise Username_Taken
            if self.Password.text() == "":
                raise Invalid_Password
            if self.Email.text() == "" or "@" not in self.Email.text():
                raise Invalid_Email
            if "." not in self.Email.text():
                raise Invalid_Email
            if Check_For_Availabilty(2, self.Email.text()):
                raise Email_Taken
            if self.Password.text() != self.CPassword.text():
                raise Password_Did_Not_Match
            global vcc
            if self.VCCode.text() != vcc or self.VCCode.text() == "":
                raise Wrong_VCCode
            if not self.AgreeButton.isChecked():
                raise Not_Agreed
        except No_Internet:
            Error_Message(2)
        except Invalid_Name:
            Error_Message(3)
        except Invalid_Username:
            Error_Message(4)
        except Username_Taken:
            Error_Message(5)
        except Invalid_Password:
            Error_Message(6)
        except Invalid_Email:
            Error_Message(0)
        except Email_Taken:
            Error_Message(1)
        except Password_Did_Not_Match:
            Error_Message(7)
        except Wrong_VCCode:
            Error_Message(8)
        except Not_Agreed:
            Error_Message(9)
        else:
            Success_Message(2)
            self.RegisterButton.setEnabled(False)
            New_User_Write([self.Name.text(), self.Username.text(), self.Email.text(), "0", "0", Current_Date_Time(), self.Password.text()])
            Registration_Completion_Mail(self.Name.text(), self.Email.text())
            Success_Message(1)
            global ui2
            ui2.setupUi(After_Splash)
            After_Splash.show()
            Register_Form.hide()

    def Sending_Verification_Code(self):
        try:
            if not Internet_Available():
                raise No_Internet
            if self.Email.text() == "" or "@" not in self.Email.text():
                raise Invalid_Email
            if "." not in self.Email.text():
                raise Invalid_Email
            if Check_For_Availabilty(2, self.Email.text()):
                raise Email_Taken
        except No_Internet:
            Error_Message(2)
        except Invalid_Email:
            Error_Message(0)
        except Email_Taken:
            Error_Message(1)
        else:
            global vcc
            vcc = Generate_Verification_Code()
            Send_Verification_Code(self.Email.text(), vcc)
            Success_Message(0)

    def Back_To_Main_Page(self):
        global ui2
        ui2.setupUi(After_Splash)
        After_Splash.show()
        Register_Form.hide()

    def retranslateUi(self, Register_Form):
        _translate = QtCore.QCoreApplication.translate
        Register_Form.setWindowTitle(_translate("Register_Form", "Registration"))
        self.ExitButton.setToolTip(_translate("Register_Form", "<html><head/><body><p><span style=\" font-weight:600;\">Exit To Main Page</span></p></body></html>"))
        self.label_2.setText(_translate("Register_Form", "<html><head/><body><p><span style=\" color:#00ff00;\">Account Registration</span></p></body></html>"))
        self.label_3.setText(_translate("Register_Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Name</span></p></body></html>"))
        self.Name.setToolTip(_translate("Register_Form", "<html><head/><body><p><span style=\" font-weight:600;\">Your Name</span></p></body></html>"))
        self.Name.setPlaceholderText(_translate("Register_Form", "Eg : John Hingston"))
        self.Username.setToolTip(_translate("Register_Form", "<html><head/><body><p><span style=\" font-weight:600;\">Your Desired Username</span></p></body></html>"))
        self.Username.setPlaceholderText(_translate("Register_Form", "Eg: hinGstoN_joHN"))
        self.label_4.setText(_translate("Register_Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Username</span></p></body></html>"))
        self.label_5.setText(_translate("Register_Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Password</span></p></body></html>"))
        self.Password.setToolTip(_translate("Register_Form", "<html><head/><body><p><span style=\" font-weight:600;\">Your Password</span></p></body></html>"))
        self.CPassword.setToolTip(_translate("Register_Form", "<html><head/><body><p><span style=\" font-weight:600;\">Your Password</span></p></body></html>"))
        self.label_6.setText(_translate("Register_Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Confirm Password</span></p></body></html>"))
        self.Email.setToolTip(_translate("Register_Form", "<html><head/><body><p><span style=\" font-weight:600;\">Your Email Address</span></p></body></html>"))
        self.Email.setPlaceholderText(_translate("Register_Form", "Eg: john_hingston@xyz.com"))
        self.label_7.setText(_translate("Register_Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Email</span></p></body></html>"))
        self.VCCode.setToolTip(_translate("Register_Form", "<html><head/><body><p><span style=\" font-weight:600;\">If Your Email Is Correct, Check Your Inbox For Verification Code. Else Change The Email And Get The Code Again</span></p></body></html>"))
        self.VCCode.setPlaceholderText(_translate("Register_Form", "Eg: 475326"))
        self.label_8.setText(_translate("Register_Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Verification Code</span></p></body></html>"))
        self.GetCodeButton.setToolTip(_translate("Register_Form", "<html><head/><body><p><span style=\" font-weight:600;\">You Will Recieve An Mail Containing Verification Code</span></p></body></html>"))
        self.GetCodeButton.setText(_translate("Register_Form", "Get Verification Code"))
        self.AgreeButton.setToolTip(_translate("Register_Form", "<html><head/><body><p><span style=\" font-weight:600;\">By Checking This You Agree To Our Terms And Conditions</span></p></body></html>"))
        self.AgreeButton.setText(_translate("Register_Form", "I Agree To The Terms And Conditions"))
        self.RegisterButton.setToolTip(_translate("Register_Form", "<html><head/><body><p><span style=\" font-weight:600;\">Register Account</span></p></body></html>"))
        self.RegisterButton.setText(_translate("Register_Form", "Register"))


class Ui_After_Splash(object):
    def setupUi(self, After_Splash):
        After_Splash.setObjectName("After_Splash")
        After_Splash.resize(600, 600)
        After_Splash.setMinimumSize(QtCore.QSize(600, 600))
        After_Splash.setMaximumSize(QtCore.QSize(600, 600))
        After_Splash.setBaseSize(QtCore.QSize(600, 600))
        After_Splash.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        After_Splash.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(After_Splash)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(210, 80, 161, 141))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 540, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.ExitButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(540, 540, 51, 51))
        self.ExitButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ExitButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExitButton.setIcon(icon1)
        self.ExitButton.setObjectName("ExitButton")
        self.RegisterButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegisterButton.setGeometry(QtCore.QRect(170, 290, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.RegisterButton.setFont(font)
        self.RegisterButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.RegisterButton.setObjectName("RegisterButton")
        self.LogInButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogInButton.setGeometry(QtCore.QRect(170, 380, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(14)
        self.LogInButton.setFont(font)
        self.LogInButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LogInButton.setObjectName("LogInButton")
        After_Splash.setCentralWidget(self.centralwidget)

        self.retranslateUi(After_Splash)
        QtCore.QMetaObject.connectSlotsByName(After_Splash)
        self.ExitButton.clicked.connect(self.Home_Page)
        self.RegisterButton.clicked.connect(self.Show_Registration_Form)
        self.LogInButton.clicked.connect(self.Show_Login_Form)

    def Show_Login_Form(self):
        Login_Form.show()
        After_Splash.hide()

    def Show_Registration_Form(self):
        global ui3
        ui3.setupUi(Register_Form)
        Register_Form.show()
        After_Splash.hide()

    def Home_Page(self):
        MainWindow.show()
        After_Splash.hide()

    def retranslateUi(self, After_Splash):
        _translate = QtCore.QCoreApplication.translate
        After_Splash.setWindowTitle(_translate("After_Splash", "After Splash"))
        self.ExitButton.setToolTip(_translate("After_Splash", "<html><head/><body><p><span style=\" font-weight:600;\">Exit To Home Page</span></p></body></html>"))
        self.RegisterButton.setToolTip(_translate("After_Splash", "<html><head/><body><p><span style=\" font-weight:600;\">Register An New Account</span></p></body></html>"))
        self.RegisterButton.setText(_translate("After_Splash", "Register"))
        self.LogInButton.setToolTip(_translate("After_Splash", "<html><head/><body><p><span style=\" font-weight:600;\">Log In To Existing Account</span></p></body></html>"))
        self.LogInButton.setText(_translate("After_Splash", "Log In"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        MainWindow.setBaseSize(QtCore.QSize(600, 600))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/main_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/splash_screen.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.MainButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.MainButton.setGeometry(QtCore.QRect(214, 184, 191, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainButton.sizePolicy().hasHeightForWidth())
        self.MainButton.setSizePolicy(sizePolicy)
        self.MainButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.MainButton.setAcceptDrops(False)
        self.MainButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainButton.setIcon(icon1)
        self.MainButton.setCheckable(False)
        self.MainButton.setObjectName("MainButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 10, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.ExitButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(530, 10, 51, 51))
        self.ExitButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ExitButton.setText("")
        self.ExitButton.setIcon(icon1)
        self.ExitButton.setObjectName("ExitButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.ExitButton.clicked.connect(self.Exit_Application)
        self.MainButton.clicked.connect(self.Go_Inside)

    def Go_Inside(self):
        global ui2
        ui2.setupUi(After_Splash)
        After_Splash.show()
        MainWindow.hide()

    def Exit_Application(self):
        app.quit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bank"))
        self.MainButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Get In</span></p></body></html>"))
        self.ExitButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Quit</span></p></body></html>"))


if __name__ == "__main__":
    Initialise()

    app = QtWidgets.QApplication(sys.argv)

    TransferMoney = QtWidgets.QMainWindow()
    ui15 = Ui_TransferMoney()

    Passbook = QtWidgets.QMainWindow()
    ui14 = Ui_Passbook()

    Withdraw = QtWidgets.QMainWindow()
    ui13 = Ui_Withdraw()

    Deposit = QtWidgets.QMainWindow()
    ui12 = Ui_Deposit()

    Details_Of_SUser = QtWidgets.QMainWindow()
    ui11 = Ui_Details_Of_SUser()

    Available_Users = QtWidgets.QMainWindow()
    ui10 = Ui_Available_Users()

    Payments = QtWidgets.QMainWindow()
    ui9 = Ui_Payments()

    DP_Settings = QtWidgets.QMainWindow()
    ui8 = Ui_DP_Settings()

    Profile_Window = QtWidgets.QMainWindow()
    ui7 = Ui_Profile_Window()

    After_Log_In = QtWidgets.QMainWindow()
    ui6 = Ui_After_Log_In()

    PasswordReset = QtWidgets.QMainWindow()
    ui5 = Ui_PasswordReset()

    Login_Form = QtWidgets.QMainWindow()
    ui4 = Ui_Login_Form()
    ui4.setupUi(Login_Form)

    Register_Form = QtWidgets.QMainWindow()
    ui3 = Ui_Register_Form()

    After_Splash = QtWidgets.QMainWindow()
    ui2 = Ui_After_Splash()

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())

#