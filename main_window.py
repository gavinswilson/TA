import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from drawing_tools import image_analysis

class main_window:
    def __init__(self) -> None:
        self.image = image_analysis()
        pass


    def window(self):
        app = QApplication(sys.argv)
        widget = QWidget()
        
        button1 = QPushButton(widget)
        button1.setText("Open Image")
        button1.move(64,32)
        button1.clicked.connect(self.button1_clicked)

        button2 = QPushButton(widget)
        button2.setText("Change Color")
        button2.move(64,64)
        button2.clicked.connect(self.flip_color)

        widget.setGeometry(50,50,320,200)
        widget.setWindowTitle("Analyse")
        widget.show()
        sys.exit(app.exec_())
    
    def button1_clicked(self):
        print("Button 1 Pushed")
        self.image.open_image()

    def flip_color(self):
        print("Flip button Pushed")
        self.image.flip_color()
    