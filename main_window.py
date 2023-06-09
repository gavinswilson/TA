import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QFileDialog, QTextEdit,
    QDialogButtonBox, QVBoxLayout, QMenuBar, QGroupBox, QHBoxLayout, QMenu,
    QGridLayout, QLabel, QLineEdit, QFormLayout, QComboBox, QSpinBox, QDialog, QColorDialog, QSlider)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from aboutDialog import AboutDialog
from drawing_tools import image_analysis
from settings import *

class main_window(QDialog):
    version = "0.1"
    settings = yaml_data()
    yamlSettings = None
    settings_file = 'settings.yaml'
    num_grid_rows = 3

    def __init__(self):
        super().__init__()
        
        self.read_settings_file()
        
        self.image = image_analysis()
        self.filename = ""
        self.default_color = (255,0,0)
        self.create_top_menu()
        self.create_file_options_box()
        self.create_sliders()
        self.create_file_info_box()
        # self.create_form_group_box()

        big_editor = QTextEdit()
        big_editor.setPlainText("Information will go here")

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.setMenuBar(self._main_menu_bar)
        main_layout.addWidget(self._file_options_box)
        main_layout.addWidget(self._sliderbox)
        main_layout.addWidget(self._file_info_box)
        # main_layout.addWidget(self._form_group_box)
        # main_layout.addWidget(big_editor)
        main_layout.addWidget(button_box)
        self.setLayout(main_layout)

        self.setWindowTitle("Analysis")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        pass

    def create_top_menu(self):
        
        # -------- file Menu -----------
        self._file_menu = QMenu("&File", self)
        
        self.open_action = self._file_menu.addAction("&Open")
        self.open_action.triggered.connect(self.open_file_dialog)

        self.open_settings = self._file_menu.addAction("Open Settings")
        self.save_image = self._file_menu.addAction("&Save")
        self.save_settings = self._file_menu.addAction("Save Settings")
        
        self._exit_action = self._file_menu.addAction("E&xit")
        self._exit_action.triggered.connect(self.accept)
        # -------- View Menu -----------
        self._view_menu = QMenu("&View", self)
        self.view_image = self._view_menu.addAction("View")
        self.view_image.triggered.connect(self.view_image_file)
        # -------- Help Menu ----------- 
        self._help_menu = QMenu("&Help", self)
        self.help_image = self._help_menu.addAction("Help")
        self.help_image.triggered.connect(self.show_help)
        self.about_image = self._help_menu.addAction("About")
        self.about_image.triggered.connect(self.about)
        # -------- build Menu ----------- 
        self._main_menu_bar = QMenuBar()
        self._main_menu_bar.addMenu(self._file_menu)
        self._main_menu_bar.addMenu(self._view_menu)
        self._main_menu_bar.addMenu(self._help_menu)
        
    def create_sliders(self):   
        self._sliderbox = QGroupBox("Drawing Options")
        layout = QHBoxLayout()
        self.thickness_label = QLabel()
        self.slider = QSlider()
        self.slider.setMinimum(1)
        self.slider.setMaximum(15)

        line_color_button = QPushButton()
        line_color_button.setText("Line Color")
        line_color_button.setObjectName('button4')
        # button2.move(10,60)
        line_color_button.clicked.connect(self.get_drawing_color)
        newcolorrgb = (self.image.color[2], self.image.color[1], self.image.color[0])
        newStyle = "background-color : rgb" + str(newcolorrgb) + ";"
        print(newStyle)
        line_color_button.setStyleSheet(newStyle)
        
        # self.slider.setTickPosition(TicksLeft)
        # self.slider.setOrientation(Horizontal)
        layout.addWidget(line_color_button)
        layout.addWidget(self.slider)
        layout.addWidget(self.thickness_label)
        
        self._sliderbox.setLayout(layout)
        # self.setGeometry(300, 300, 300, 150)
        self.slider.valueChanged.connect(self.valuechange)
        # self.show()

    def valuechange(self):
        txt = str(self.slider.value())
        self.image.set_thickness(int(self.slider.value()))
        self.thickness_label.setText(txt)      

    def create_file_options_box(self):
        self._file_options_box = QGroupBox("Image Options")
        layout = QHBoxLayout()
        
        button1 = QPushButton()
        button1.setText("View Image")
        # button1.move(10,10)
        button1.clicked.connect(self.view_image_file)
        
        button3 = QPushButton()
        button3.setText("Open File")
        # button3.move(10,30)
        button3.clicked.connect(self.open_file_dialog)
        
        # button2 = QPushButton()
        # button2.setText("Change Line Color")
        # button2.move(10,60)
        # button2.clicked.connect(self.flip_color)
        
        
      

        layout.addWidget(button3)
        layout.addWidget(button1)
        # layout.addWidget(button2)
        
        # for i in range(self.num_buttons):
        #     button = QPushButton(f"Button {i + 1}")
        #     layout.addWidget(button)

        self._file_options_box.setLayout(layout)

    def create_file_info_box(self):
        self._file_info_box = QGroupBox("File Information")
        layout = QGridLayout()

        for i in range(self.num_grid_rows):
            label = QLabel(f"Line {i + 1}:")
            line_edit = QLineEdit()
            layout.addWidget(label, i + 1, 0)
            layout.addWidget(line_edit, i + 1, 1)

        self._small_editor = QTextEdit()
        self._small_editor.setPlainText("file info will be shown here!")

        layout.addWidget(self._small_editor, 0, 2, 4, 1)

        layout.setColumnStretch(1, 10)
        layout.setColumnStretch(2, 20)
        self._file_info_box.setLayout(layout)

    def create_form_group_box(self):
        self._form_group_box = QGroupBox("Form layout")
        layout = QFormLayout()
        layout.addRow(QLabel("Line 1:"), QLineEdit())
        layout.addRow(QLabel("Line 2, long text:"), QComboBox())
        layout.addRow(QLabel("Line 3:"), QSpinBox())
        self._form_group_box.setLayout(layout)


    def window(self):
        app = QApplication(sys.argv)
        widget = QWidget()
        
        button1 = QPushButton(widget)
        button1.setText("Open Image")
        button1.move(10,10)
        button1.clicked.connect(self.button1_clicked)
        
        button3 = QPushButton(widget)
        button3.setText("Open")
        button3.move(10,30)
        button3.clicked.connect(self.open_file_dialog)

        button2 = QPushButton(widget)
        button2.setText("Change Color")
        button2.move(10,60)
        button2.clicked.connect(self.flip_color)

        widget.setGeometry(50,50,320,200)
        widget.setWindowTitle("Analyse")
        widget.show()
        sys.exit(app.exec_())
    
    def button1_clicked(self):
        print("Button 1 Pushed")
        self.image.open_image(self.filename)

    def view_image_file(self):
        print("open file clicked")
        self.image.open_image(self.filename)

    def flip_color(self):
        print("Flip button Pushed")
        self.image.flip_color()
    
    def get_drawing_color(self):
        color = QColorDialog.getColor()
        newcolorbgr = (color.blue(), color.green(), color.red())
        newcolorrgb = (color.red(), color.green(), color.blue())
        newStyle = "QPushButton#line_color_button {background-color : rgb" + str(newcolorrgb) + ";}"
        print(newStyle)
        self._file_options_box.setStyleSheet(newStyle)
        self.image.set_drawing_color(newcolorbgr)

    def open_file_dialog(self):
        fname = QFileDialog.getOpenFileName()
        # fname = QFileDialog.getOpenFileName("Select a File", "/home/gavinswilson/Downloads","Images (*.png *.jpg)")
        # for file in fname:
        #     self.image.open_image(file)
        self.filename = fname[0]
        print(self.filename)
        self.image.set_file_name(self.filename)
        self._small_editor.setPlainText(self.filename + "file loaded!")
    
    def read_settings_file(self):
        self.settings.setFilename('settings.yaml')
        self.settings.readFile()
        self.settings.printData()
        self.settings.changeData('filename', 'hello')
        self.settings.printData()
        self.settings.saveSettings()

    def get_version(self):
        return self.version
    
    def show_help(self):
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://github.com/gavinswilson/TA"))
        print('Help Me!')
    
    def about(self):
        dlg = AboutDialog(self.get_version(), self.image.get_version(), self.settings.getVersion()) 
        dlg.exec_()