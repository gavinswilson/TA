from PyQt5.QtWidgets import (QDialog,QDialogButtonBox, QVBoxLayout, QLabel)

class AboutDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("Mozarella Ashbadger")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        # logo = QLabel()
        # logo.setPixmap( QPixmap( os.path.join('icons','ma-icon-128.png') ) )
        # layout.addWidget(logo)

        layout.addWidget( QLabel("Version 23.35.211.233232") )
        layout.addWidget( QLabel("Copyright 2015 Mozarella Inc.") )

        for i in range(0, layout.count() ):
            layout.itemAt(i).setAlignment( Qt.AlignHCenter )

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)