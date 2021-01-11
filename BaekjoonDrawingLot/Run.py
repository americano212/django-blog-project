import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit,QLabel, QPushButton,QVBoxLayout
from PyQt5.QtGui import QIcon
from Crawling import *

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):


        btn = QPushButton(self)
        btn.setText('Input URL HERE')
        btn.clicked.connect(self.on_click)

        self.qle = QLineEdit(self)
        self.lbl = QLabel(self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.qle)
        vbox.addWidget(btn)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)
        self.setWindowTitle('Baekjoon Drawing Lot')
        self.setWindowIcon(QIcon('img/sgcs_icon.png'))
        self.setGeometry(300, 300, 600, 400)
        self.show()

    def on_click(self):
        print(self.qle.text())
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = App()
   sys.exit(app.exec_())
