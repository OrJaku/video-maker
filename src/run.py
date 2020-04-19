from PyQt5 import QtWidgets, uic
from video_app import Main, LoadVideo


def loaded_video_data():
    load_file = LoadVideo()
    dlg.fpsVideo.setText(str(load_file.cap_video_fps))
    dlg.lengthVideo.setText(str(load_file.video_length))
    dlg.widthVideo.setText(str(load_file.cap_video_width))
    dlg.heightVideo.setText(str(load_file.cap_video_height))


def converting():
    fps = dlg.fpsConvert.text()
    width = dlg.widthConvert.text()
    height = dlg.heightConvert.text()
    color = dlg.colorConvert.text()
    main = Main(fps, color, width, height)
    main.modify()


app = QtWidgets.QApplication([])
dlg = uic.loadUi('run.ui')

dlg.loadVideo.clicked.connect(loaded_video_data)
dlg.convertVideo.clicked.connect(converting)

dlg.show()

app.exec()
