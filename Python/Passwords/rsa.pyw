from PyQt5 import QtCore, QtGui, QtWidgets
import os
import random
import sys
import time
import shutil
import pyperclip
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # set 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        MainWindow.setMinimumSize(QtCore.QSize(800, 400))
        MainWindow.setMaximumSize(QtCore.QSize(800, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.monty = QtWidgets.QGroupBox(self.centralwidget)
        self.monty.setGeometry(QtCore.QRect(10, 10, 781, 551))
        self.monty.setObjectName("monty")
        self.hello_label = QtWidgets.QLabel(self.monty)
        self.hello_label.setGeometry(QtCore.QRect(20, 30, 161, 21))
        self.hello_label.setObjectName("hello_label")
        self.password = QtWidgets.QTextEdit(self.monty)
        self.password.setGeometry(QtCore.QRect(20, 60, 741, 131))
        self.password.setObjectName("password")
        self.button_thing = QtWidgets.QLabel(self.monty)
        self.button_thing.setGeometry(QtCore.QRect(20, 210, 551, 21))
        self.button_thing.setObjectName("button_thing")
        self.numberChosen = QtWidgets.QComboBox(self.monty)
        self.numberChosen.setGeometry(QtCore.QRect(20, 240, 121, 22))
        self.numberChosen.setObjectName("numberChosen")
        self.encrypt_button = QtWidgets.QPushButton(self.monty)
        self.encrypt_button.setGeometry(QtCore.QRect(20, 280, 93, 28))
        self.encrypt_button.setObjectName("encrypt_button")
        # add text to the button
        self.encrypt_button.setText("Encrypt")
        self.decrypt_button = QtWidgets.QPushButton(self.monty)
        self.decrypt_button.setGeometry(QtCore.QRect(150, 280, 93, 28))
        self.decrypt_button.setObjectName("decrypt_button")
        self.decrypt_button.setText("Decrypt")
        self.exit_button = QtWidgets.QPushButton(self.monty)
        self.exit_button.setGeometry(QtCore.QRect(280, 280, 93, 28))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.setText("Exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        font_choice = "Arial"
        if os.path.isfile("rsa.pyw") == False:
            QtWidgets.QMessageBox.critical(None, "Error", "Please run this program in the correct directory\nRun this program in an IDE if the problem persists")
            sys.exit()
        if os.system("ruby -v") != 0:
            QtWidgets.QMessageBox.critical(None, "Error", "Ruby is not installed. Please install Ruby to use this program.")
            sys.exit()
        cwd = os.getcwd()
        if os.path.isfile(cwd + "\\rsa-password.rb") == False:
            QtWidgets.QMessageBox.critical(None, "Error", "rsa-password.rb is not installed. Please install rsa-password.rb to use this program.")
            sys.exit()
        if os.path.isfile(cwd + "\\rsa-decrypt.rb") == False:
            QtWidgets.QMessageBox.critical(None, "Error", "rsa-decrypt.rb is not installed. Please install rsa-decrypt.rb to use this program.")
            sys.exit()
        show_progress_bar = "True"
        self.password.setFont(QtGui.QFont(font_choice, 10))
        self.numberChosen.addItems(["1024", "2048", "4096", "8192", "16384", "32768", "65536"])
        self.numberChosen.setCurrentIndex(0)
        self.encrypt_button.clicked.connect(self.encrypt)
        self.decrypt_button.clicked.connect(self.decrypt)
        self.exit_button.clicked.connect(QtWidgets.qApp.quit)
        self.toolbar = QtWidgets.QToolBar()
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        self.toolbar.addAction("Copy", self.copy)
        self.toolbar.addAction("Save", self.save)
        self.toolbar.addAction("Clear", self.clear)
        self.toolbar.addAction("Exit", QtWidgets.qApp.quit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA Encryption and Decryption"))
        self.monty.setTitle(_translate("MainWindow", " RSA Encryption and Decryption "))
        self.hello_label.setText(_translate("MainWindow", "Enter a password:"))
        self.button_thing.setText(_translate("MainWindow", "Choose a bit option (above 4096 not recommended. Above 16384 will take a long time): "))
    def encrypt(self):
        global language
        filename = "key.txt"
        filename_key = "key.pem"
        # if it has more than one line, show error
        if self.password.toPlainText().count("\n") > 0:
            # remove the extra lines
            self.password.setPlainText(self.password.toPlainText().split("\n")[0])
        # if it has no text, show error
        if self.password.toPlainText() == "":
            QtWidgets.QMessageBox.critical(None, "Error", "Please enter a password")
            return
        if int(self.numberChosen.currentText()) > 16384 and int(self.numberChosen.currentText()) < 65536:
            messageBoxResponse = QtWidgets.QMessageBox.question(
                None, "Warning", "This will take about 4 hours to complete",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if messageBoxResponse == QtWidgets.QMessageBox.No:
                return
        elif int(self.numberChosen.currentText()) >= 65536:
            messageBoxResponse = QtWidgets.QMessageBox.question(
                None, "Warning", "This will take about 4 days to complete",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if messageBoxResponse == QtWidgets.QMessageBox.No:
                return
        elif int(self.numberChosen.currentText()) >= 16384 and int(self.numberChosen.currentText()) < 65536:
            messageBoxResponse = QtWidgets.QMessageBox.question(
                None, "Warning", "This will take about 1 minute to complete",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if messageBoxResponse == QtWidgets.QMessageBox.No:
                return
        else:
            pass
        self.statusbar.showMessage("Encrypting...")
        number = self.numberChosen.currentText()
        number = int(number)
        print (number)
        password = self.password.toPlainText()
        if password.count(" ") > 0:
            password = '"' + password + '"'
        else:
            pass
        os.system(f"ruby rsa-password.rb {password} {filename} {number}")
        self.statusbar.showMessage("Encryption complete.")
        # open key.txt and read it (remove newlines) and then add it to the text box
        with open(filename, "r") as f:
            self.password.setPlainText(f.read().replace("\n", ""))
        self.password.setReadOnly(True)
        self.encrypt_button.setEnabled(False)
        self.decrypt_button.setEnabled(True)
    def decrypt(self):
        global language
        # create a filedialog to choose a file then move it to the current directory and rename it to key.txt
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        fileName = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "Open file", "", "Text Files (*.txt);;All Files (*)", options=options)
        fileName = str(fileName)
        # output = ('C:/Users/Beans/Documents/Coding/Python/Passwords/key.txt', 'Text Files (*.txt)')
        # isolate the path from the output
        fileName = fileName.split(",")[0]
        # remove the first two characters
        fileName = fileName[2:]
        fileName = fileName.replace("\\", "/")
        fileName = fileName.replace("'", "")
        print (fileName)
        if fileName:
            try:
                shutil.copy(fileName, "key.txt")
                self.statusbar.showMessage(f"Opened {fileName}.")
            except shutil.SameFileError:
                self.statusbar.showMessage(f"Opened {fileName}.")
        else:
            return
        # create another filedialog to choose a file then move it to the current directory and rename it to key.pem
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        # make sure filename is a string
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "Open file", "", "Text Files (*.pem);;All Files (*)", options=options)
        fileName_Key = str(fileName)
        if fileName:
            try:
                shutil.copy(fileName, "key.pem")
                self.statusbar.showMessage(f"Opened {fileName_Key}.")
            except shutil.SameFileError:
                self.statusbar.showMessage(f"Opened {fileName_Key}.")
        else:
            return
        self.statusbar.showMessage("Decrypting...")
        decrypted = os.popen("ruby rsa-decrypt.rb key.txt key.pem").read()
        self.password.setPlainText(decrypted)
        self.statusbar.showMessage("Decryption complete.")
        self.encrypt_button.setEnabled(True)
        self.decrypt_button.setEnabled(False)
    def copy(self):
        # use pyperclip to copy the text in the text box
        if self.password.toPlainText() == "":
            QtWidgets.QMessageBox.critical(None, "Error", "Nothing to copy")
            return
        else:
            pass
        pyperclip.copy(self.password.toPlainText())
        self.statusbar.showMessage("Copied to clipboard.")
    def save(self):
        if self.password.toPlainText() == "":
            QtWidgets.QMessageBox.critical(None, "Error", "Nothing to save")
            return
        else:
            pass
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self.centralwidget, "Save file", "", "Text Files (*.txt);;All Files (*)", options=options)
        fileName = str(fileName)
        fileName = fileName.split(",")[0]
        # remove the first two characters
        fileName = fileName[2:]
        fileName = fileName.replace("\\", "/")
        fileName = fileName.replace("'", "")
        if fileName:
            if fileName.endswith(".txt"):
                pass
            else:
                fileName = fileName + ".txt"
            text_file = open(fileName, "w")
            text_file.write(self.password.toPlainText())
            text_file.close()
            self.statusbar.showMessage(f"Saved to {fileName}.")
    def clear(self):
        self.password.clear()
        self.statusbar.showMessage("Cleared.")
        self.encrypt_button.setEnabled(True)
        self.decrypt_button.setEnabled(True)
        self.password.setReadOnly(False)

    def _quit(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
