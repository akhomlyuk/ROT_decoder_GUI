import sys
from cipher_functions import decrypt, encrypt
from PySide6.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow


class RotDecoder(QMainWindow):
    def __init__(self):
        super(RotDecoder, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_slider_to_spinbox()
        self.decrypting()
        self.ui.spinBox.valueChanged.connect(self.decrypting)
        self.ui.textEdit.textChanged.connect(self.decrypting)
        self.ui.encrypt_btn.clicked.connect(self.checked_dec_btn)
        self.ui.decrypt_btn.clicked.connect(self.checked_enc_btn)
        self.ui.brute_btn.clicked.connect(self.bruteforce)

    def bruteforce(self):
        self.ui.textEdit_2.clear()
        if decrypt(self.ui.textEdit.toPlainText(), 1)[1] > decrypt(self.ui.textEdit.toPlainText(), 1)[2]:
            for i in range(1, 33):
                ls = ['ROT key ' + str(i) + ': ' + decrypt(self.ui.textEdit.toPlainText(), i)[0] + '\n' for i in
                      range(1, 33)]
                with open('bruted.txt', 'w', encoding='UTF-8') as file:
                    file.writelines(ls)
                    self.ui.textEdit_2.append(f'ROT key {i}:{decrypt(self.ui.textEdit.toPlainText(), i)[0]}')
        else:
            for i in range(1, 27):
                ls = ['ROT key ' + str(i) + ': ' + decrypt(self.ui.textEdit.toPlainText(), i)[0] + '\n' for i in
                      range(1, 27)]
                with open('bruted.txt', 'w', encoding='UTF-8') as file:
                    file.writelines(ls)
                    self.ui.textEdit_2.append(f'ROT key {i}: {decrypt(self.ui.textEdit.toPlainText(), i)[0]}')

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

    def connect_slider_to_spinbox(self) -> None:
        self.ui.horizontalSlider.valueChanged.connect(self.ui.spinBox.setValue)
        self.ui.spinBox.valueChanged.connect(self.ui.horizontalSlider.setValue)

    def decrypting(self):
        self.ui.textEdit_2.setText(decrypt(self.ui.textEdit.toPlainText(), self.ui.spinBox.value())[0])

    def encrypting(self):
        self.ui.textEdit_2.setText(encrypt(self.ui.textEdit.toPlainText(), self.ui.spinBox.value()))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = RotDecoder()
    window.show()

    sys.exit(app.exec())
