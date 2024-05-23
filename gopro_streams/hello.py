# hello.py

"""Simple Hello, World example with PyQt6."""

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QToolBar
from PyQt6.QtGui import QPalette, QColor, QAction, QIcon

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Hello App")
        layout = QVBoxLayout()
        window = QWidget()
        window.setMinimumSize(640, 480)
        window.setLayout(layout)
        self.setCentralWidget(window)
        
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        button_connect = QAction("Connect", self)
        button_connect.setStatusTip("Connect to GoPro")
        button_connect.triggered.connect(self.onConnect)
        toolbar.addAction(button_connect)

        button_connect = QAction("Start", self)
        button_connect.setStatusTip("Start streaming")
        button_connect.triggered.connect(self.onStart)
        toolbar.addAction(button_connect)

        button_connect = QAction("Stop", self)
        button_connect.setStatusTip("Stop streaming")
        button_connect.triggered.connect(self.onStop)
        toolbar.addAction(button_connect)

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_connect)

    def onConnect(self, s):
        print("click connect", s)

    def onStart(self, s):
        print("click start", s)

    def onStop(self, s):
        print("click stop", s)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()