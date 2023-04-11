#!/usr/bin/python3

from main_window import *
from pathlib import Path

   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('stylesheet.qss').read_text())
    dialog = main_window()
    dialog.show()
    sys.exit(dialog.exec())

