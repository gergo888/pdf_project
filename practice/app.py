import sys

from PyQt6.QtCore import (Qt, QSize)
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        lbl_text = QLabel("Coordinates: ")
        lbl_position = QLabel("123, 456")
        lbl_image = QLabel("hrlo")
        lbl_image.setStyleSheet("border: 1px solid black;")

        img = QPixmap("/home/gergo/PycharmProjects/createGUI/pyqt6-source/basic/otje.jpg")
        size = QSize(300, 200)
        img2 = img.scaled(size)
        print(img2.size())

        lbl_image.setPixmap(img2)

        layout = QVBoxLayout()
        layout.addWidget(lbl_text)
        layout.addWidget(lbl_position)
        layout.addWidget(lbl_image)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
