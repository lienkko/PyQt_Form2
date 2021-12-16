from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI import Ui_MainWindow
import sys
import random
from PIL import Image, ImageDraw


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet("background: white")
        self.box = [self.ui.label, self.ui.label_2, self.ui.label_3]
        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColor(0, 0, 0, 10))
        for i in self.box:
            i.setPalette(pal)
            i.hide()
        self.ui.pushButton.clicked.connect(self.run)

    def run(self):
        self.ui.pushButton.hide()
        for i in self.box:
            wh = random.randint(20, 100)
            image = Image.new('RGB', (wh + 1, wh + 1), "white")
            draw = ImageDraw.Draw(image)

            draw.ellipse((0, 0, wh, wh), (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 'blue')
            image.save('el.png')
            i.setGeometry(QRect(random.randint(20, 380), random.randint(20, 250), wh + 1, wh + 1))
            i.setPixmap(QPixmap("el.png"))
            i.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    root = mywindow()

    root.show()

    sys.exit(app.exec())
