import ui.main
import sys
from PySide6.QtWidgets import (QApplication)

def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("KMITL")
    app.setApplicationName("Music Streaming Client")

    window = ui.main.MainWindow()
    window.show()
    app.exec()
    
if __name__ == "__main__":
    main()