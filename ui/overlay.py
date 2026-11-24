import sys

from PySide6.QtCore import Qt, QTimer, QRectF
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtWidgets import QApplication, QWidget


class JarvisOverlay(QWidget):
    def __init__(self):
        super().__init__()

        self.angle = 0

        self.setFixedSize(420, 420)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.Tool
        )
        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(30)

    def animate(self):
        self.angle = (self.angle + 2) % 360
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )
        painter.setBrush(Qt.BrushStyle.NoBrush)

        painter.translate(210, 210)
        painter.rotate(self.angle)

        painter.setPen(QPen(QColor(0, 200, 255), 4))
        painter.drawArc(
            QRectF(-150, -150, 300, 300),
            0,
            120 * 16
        )

        painter.end()


app = QApplication(sys.argv)
window = JarvisOverlay()
window.show()
sys.exit(app.exec())
