import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
from PyQt5.QtGui import QIcon
from drawing_tools import image_analysis

class main_window:
    def __init__(self) -> None:
        self.image = image_analysis()
        self.filename = ""
        pass


    def window(self):
        app = QApplication(sys.argv)
        widget = QWidget()
        
        button1 = QPushButton(widget)
        button1.setText("Open Image")
        button1.move(64,32)
        button1.clicked.connect(self.button1_clicked)
        
        button3 = QPushButton(widget)
        button3.setText("Open")
        button3.move(0,32)
        button3.clicked.connect(self.open_file_dialog)

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
        self.image.open_image(self.filename)

    def flip_color(self):
        print("Flip button Pushed")
        self.image.flip_color()

    def open_file_dialog(self):
        fname = QFileDialog.getOpenFileName()
        # fname = QFileDialog.getOpenFileName("Select a File", "/home/gavinswilson/Downloads","Images (*.png *.jpg)")
        # for file in fname:
        #     self.image.open_image(file)
        self.filename = fname[0]
        print(self.filename)
    