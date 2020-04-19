from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDir
from video_app import Main, LoadVideo, basedir

app = QtWidgets.QApplication([])
dlg = uic.loadUi('run.ui')


def loaded_video_data(path):
    load_file = LoadVideo(path)
    dlg.fpsVideo.setText(str(load_file.cap_video_fps))
    dlg.lengthVideo.setText(str(load_file.video_length))
    dlg.widthVideo.setText(str(load_file.cap_video_width))
    dlg.heightVideo.setText(str(load_file.cap_video_height))

    dlg.fpsConvert.setText(str(""))

    dlg.fpsConvert.setText('1')
    dlg.widthConvert.setText(str(load_file.cap_video_width))
    dlg.heightConvert.setText(str(load_file.cap_video_height))
    dlg.lengthConvert.setText(str(load_file.video_length))

    dlg.ComlitedLbl.setText(str(""))


def converting():
    path_to_file = dlg.filePathWindow.text()
    fps = dlg.fpsConvert.text()
    width = dlg.widthConvert.text()
    height = dlg.heightConvert.text()
    if dlg.colorRadio.isChecked():
        color = 1
    else:
        color = 0
    main = Main(fps, color, width, height, path_to_file)
    main.modify()
    dlg.ComlitedLbl.setText(str("Completed"))


def get_file():
    file_name = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', QDir.homePath())[0]
    dlg.filePathWindow.setText(file_name)
    loaded_video_data(file_name)


dlg.fpsVideo.setReadOnly(True)
dlg.lengthVideo.setReadOnly(True)
dlg.widthVideo.setReadOnly(True)
dlg.heightVideo.setReadOnly(True)
dlg.ComlitedLbl.setReadOnly(True)

dlg.browseButton.clicked.connect(get_file)
dlg.convertVideo.clicked.connect(converting)

if __name__ == "__main__":

    dlg.show()
    app.exec()
