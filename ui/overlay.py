
import sys
from PySide6.QtCore import Qt, QTimer, QRectF
from PySide6.QtGui import QPainter, QColor, QPen, QFont
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
        self.angle = (self.angle + 1.5) % 360
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.translate(210, 210)

        # Outer rotating ring
        painter.save()
        painter.rotate(self.angle)
        painter.setPen(QPen(QColor(0, 200, 255), 4))
        painter.drawArc(
            QRectF(-150, -150, 300, 300),
            0, 140 * 16
        )
        painter.restore()

        # Inner counter-rotating ring
        painter.save()
        painter.rotate(-self.angle * 0.7)
        painter.setPen(QPen(QColor(70, 225, 255), 3))
        painter.drawArc(
            QRectF(-115, -115, 230, 230),
            60 * 16, 170 * 16
        )
        painter.restore()

        # Central text
        painter.setPen(QColor(100, 230, 255))
        painter.setFont(QFont("Sans Serif", 20, QFont.Weight.Bold))
        painter.drawText(
            QRectF(-150, -25, 300, 50),
            Qt.AlignmentFlag.AlignCenter,
            "J.A.R.V.I.S."
        )

        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JarvisOverlay()
    window.show()
    sys.exit(app.exec())
