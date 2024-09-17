from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Signal

class ClickableLabel(QLabel):
    clicked = Signal(str)

    def __init__(self, width, height):
        super(ClickableLabel, self).__init__()
        pixmap = QPixmap(width, height)
        self.setPixmap(pixmap)

    def mousePressEvent(self, event):
        self.clicked.emit(self.objectName())