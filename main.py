import sys
import os
from cipher_functions import decrypt, encrypt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from design import Ui_MainWindow


class RotDecoder(QMainWindow):
    def __init__(self):
        super(RotDecoder, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connection_slider_spinbox()
        self.decrypting()
        self.ui.spinBox.valueChanged.connect(self.decrypting)
        self.ui.textEdit.textChanged.connect(self.decrypting)
        self.ui.encrypt_btn.clicked.connect(self.checked_dec_btn)
        self.ui.decrypt_btn.clicked.connect(self.checked_enc_btn)
        self.ui.brute_btn.clicked.connect(self.bruteforce)
        self.ui.actionExit.triggered.connect(sys.exit)
        self.ui.actionabout.triggered.connect(self.about)
        self.ui.copy_btn.clicked.connect(self.copy_to_clipboard)
        self.ui.save_btn.clicked.connect(self.save_file)

    def about(self):
        a = 'Author:'
        b = "<a href='https://t.me/exited3n'>Exited3n</a>"
        QMessageBox.about(self, "About tool", f"{a} {b}")

    def bruteforce(self):
        self.ui.textEdit_2.clear()
        if decrypt(self.ui.textEdit.toPlainText(), 1)[1] > decrypt(self.ui.textEdit.toPlainText(), 1)[2]:
            for i in range(1, 33):
                ls = ['ROT key ' + str(i) + ': ' + decrypt(self.ui.textEdit.toPlainText(), i)[0] + '\n' for i in
                      range(1, 33)]
                self.ui.textEdit_2.append(f'ROT key {i}:{decrypt(self.ui.textEdit.toPlainText(), i)[0]}')
        else:
            for i in range(1, 27):
                ls = ['ROT key ' + str(i) + ': ' + decrypt(self.ui.textEdit.toPlainText(), i)[0] + '\n' for i in
                      range(1, 27)]
                self.ui.textEdit_2.append(f'ROT key {i}: {decrypt(self.ui.textEdit.toPlainText(), i)[0]}')

    def save_file(self):
        s_file = QFileDialog.getSaveFileName(None, 'Save bruteforced text to a file', f'{os.path.abspath(os.getcwd())}', "Text Files (*.txt)")
        text = self.ui.textEdit_2.toPlainText()
        if s_file[0]:
            with open(s_file[0], 'w', encoding='UTF-8') as file:
                file.write(text)

    def checked_dec_btn(self):
        self.ui.decrypt_btn.nextCheckState()
        self.encrypting()
        self.ui.spinBox.valueChanged.connect(self.encrypting)
        self.ui.textEdit.textChanged.connect(self.encrypting)

    def checked_enc_btn(self):
        self.ui.encrypt_btn.nextCheckState()
        self.decrypting()
        self.ui.spinBox.valueChanged.connect(self.decrypting)
        self.ui.textEdit.textChanged.connect(self.decrypting)

    def connection_slider_spinbox(self) -> None:
        self.ui.horizontalSlider.valueChanged.connect(self.ui.spinBox.setValue)
        self.ui.spinBox.valueChanged.connect(self.ui.horizontalSlider.setValue)

    def decrypting(self):
        self.ui.textEdit_2.setText(decrypt(self.ui.textEdit.toPlainText(), self.ui.spinBox.value())[0])

    def encrypting(self):
        self.ui.textEdit_2.setText(encrypt(self.ui.textEdit.toPlainText(), self.ui.spinBox.value()))

    def copy_to_clipboard(self) -> None:
        QApplication.clipboard().setText(self.ui.textEdit_2.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = RotDecoder()
    window.show()

    sys.exit(app.exec())
