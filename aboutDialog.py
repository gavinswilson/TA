from PyQt5.QtWidgets import (QDialog,QDialogButtonBox, QVBoxLayout, QLabel)
from PyQt5.QtCore import *

class AboutDialog(QDialog):
    version = "0.01"
    def __init__(self, main_window_version, image_manager_version, settings_version, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("Sports Analyser")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        # logo = QLabel()
        # logo.setPixmap( QPixmap( os.path.join('icons','ma-icon-128.png') ) )
        # layout.addWidget(logo)

        layout.addWidget( QLabel("Window Version: " + main_window_version ))
        layout.addWidget( QLabel("Settings Mgr Version: " + settings_version ))
        layout.addWidget( QLabel("Image Mgr Version: " + image_manager_version ))
        layout.addWidget( QLabel("Help/Diag Version: " + self.version ))

        layout.addWidget( QLabel("Copyright 2023 WilsonSoft Inc.") )

        for i in range(0, layout.count() ):
            layout.itemAt(i).setAlignment( Qt.AlignHCenter )

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)