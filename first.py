import io
import random
import sys

from PyQt5 import uic
from PyQt5.Qt import QColor, QApplication, QMainWindow
from PyQt5.QtGui import QPainter

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>AddAction</class>
 <widget class="QMainWindow" name="AddAction">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>883</width>
    <height>550</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Добавить элемент</string>
  </property>
  <widget class="QPushButton" name="button">
   <property name="geometry">
    <rect>
     <x>330</x>
     <y>500</y>
     <width>221</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>Нарисовать круг</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.button.clicked.connect(self.draw)
        self.draw_c = False

    def draw(self):
        self.draw_c = True
        self.repaint()

    def paintEvent(self, event):
        if self.draw_c:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
            self.draw_c = False

    def draw_circle(self, qp):
        qp.setBrush(QColor(254, 254, 34))
        x = random.randint(25, self.width() - 75)
        y = random.randint(10, 500)
        r = random.randint(10, 300)
        qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())
