#!/usr/bin/python3

from main_window import *
   
if __name__ == '__main__':
    # window = main_window()
    # window.window()

    app = QApplication(sys.argv)
    dialog = main_window()
    sys.exit(dialog.exec())

