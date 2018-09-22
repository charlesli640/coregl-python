from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    def __init__(self, canvasClass):
        super(Window, self).__init__()
        self.canvas = canvasClass(self)
        self.setCentralWidget(self.canvas)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('grasshopper')    
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
