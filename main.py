import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Random Circles')

        self.btn = QPushButton('Сгенерировать', self)
        self.btn.move(10, 10)
        self.btn.clicked.connect(self.drawCircle)

    def drawCircle(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawRandomCircles(qp)
        qp.end()

    def drawRandomCircles(self, qp):
        for _ in range(10):  # рисуем 10 случайных окружностей
            size = random.randint(10, 100)  # случайный размер
            x = random.randint(10, 500)  # случайная позиция по оси x
            y = random.randint(10, 500)  # случайная позиция по оси y
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # случайный цвет
            qp.setBrush(color)
            qp.drawEllipse(x, y, size, size)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
