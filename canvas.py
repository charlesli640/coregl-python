from PyQt5.QtOpenGL import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from OpenGL.GL import *
from time import time

# Set this 'None' to refresh as rapidly as possible
ThrottleFps = 60

class Canvas(QGLWidget):
    def __init__(self, parent):
        if hasattr(QGLFormat, 'setVersion'):
            f = QGLFormat(); f.setVersion(3, 2)
            f.setProfile(QGLFormat.CoreProfile)
            c = QGLContext(f)
            QGLWidget.__init__(self, c, parent)
        else:
            QGLWidget.__init__(self, parent) 
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateGL)
        interval = 1000.0 / ThrottleFps if ThrottleFps else 0
        self.timer.start( interval )
                        
    def paintGL(self):
        self.draw()

    def updateGL(self):
        self.draw()
        self.update()

    def draw(self):
        pass
