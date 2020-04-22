from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtCore import QDir, QBasicTimer
from PyQt5.QtGui import QPixmap
from PIL import Image

# from video_app import Main, LoadVideo, basedir


import os
import cv2

basedir = os.path.abspath(os.path.dirname(__file__))


class LoadVideo:
    def __init__(self, path_to_file):
        self.path = path_to_file

        self.input_path = os.path.join(self.path)
        self.video_file = cv2.VideoCapture(self.input_path)

        self.video_length = int(self.video_file.get(cv2.CAP_PROP_FRAME_COUNT))
        self.cap_video_fps = int(self.video_file.get(cv2.CAP_PROP_FPS))
        self.cap_video_width = int(self.video_file.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.cap_video_height = int(self.video_file.get(cv2.CAP_PROP_FRAME_HEIGHT))
        

    def preview(self):
        self.i = 0
        while self.i != 6:
            self.i += 1
            if self.i == 5:
                _, frame = self.video_file.read()
                img = Image.fromarray(frame)
                img.save("temp/preview.jpeg")
                pixmap = QPixmap("temp/preview.jpeg")
                pixmap = pixmap.scaled(dlg.ImageLbl.frameGeometry().width(), dlg.ImageLbl.frameGeometry().height())
                dlg.ImageLbl.setPixmap(pixmap)
            else:
                pass


class Main:
    def __init__(self, fps, color, weight, height, length, path):
        self.output_path = os.path.join(basedir, "output/out_hc.avi")
        self.file = LoadVideo(path)
        self.video_width = int(weight)
        self.video_height = int(height)
        self.video_length = int(length)

        self.video_fps = (self.file.cap_video_fps * float(fps))
        self.video_color = int(color)

        self.fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        self.out = cv2.VideoWriter(self.output_path,
                                   self.fourcc,
                                   self.video_fps,
                                   (self.video_width, self.video_height),
                                   self.video_color
                                   )
        self.timer = QBasicTimer()
        self.step = 0

    def modify(self):
        while True:
            ret, frame = self.file.video_file.read()
            self.step = self.step + 1
            try:
                gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            except cv2.error:
                break
            if ret:
                if self.video_color == 0:
                    self.file.color_value = gray
                elif self.video_color == 1:
                    self.file.color_value = frame
                else:
                    self.file.color_value = frame
                frame_number = self.step
                if frame_number <= self.video_length:
                    resized = cv2.resize(self.file.color_value, (self.video_width, self.video_height))
                    completed_percent = round(self.step * 100 / self.video_length)
                    dlg.progressBar.setProperty('value', completed_percent)
                    img = Image.fromarray(resized)
                    self.out.write(resized)
                else:
                    break
            else:
                break
            # cv2.imshow('frame', gray)
            if cv2.waitKey(0) & 0xFF == ord('q'):
                break

        self.out.release()


app = QtWidgets.QApplication([])
dlg = uic.loadUi('run.ui')


def loaded_video_data(path):
    load_file = LoadVideo(path)
    preview = LoadVideo(path).preview()
    dlg.fpsVideo.setText(str(load_file.cap_video_fps))
    dlg.lengthVideo.setText(str(load_file.video_length))
    dlg.widthVideo.setText(str(load_file.cap_video_width))
    dlg.heightVideo.setText(str(load_file.cap_video_height))

    dlg.widthConvert.setText(str(load_file.cap_video_width))
    dlg.heightConvert.setText(str(load_file.cap_video_height))

    dlg.videoLenSlider.setProperty('maximum',load_file.video_length)
    dlg.lengthConvert.setText(str(dlg.videoLenSlider.value()))


    dlg.progressBar.setProperty('value', 0)
    dlg.ComlitedLbl.setText(str(""))


def converting():
    path_to_file = dlg.filePathWindow.text()
    fps = dlg.fpsSpin.value()
    width = dlg.widthConvert.text()
    height = dlg.heightConvert.text()
    length = dlg.videoLenSlider.value()
    if dlg.colorRadio.isChecked():
        color = 1 #color
    else:
        color = 0 #gray
    main = Main(fps, color, width, height, length, path_to_file)
    main.modify()
    dlg.ComlitedLbl.setText(str("Completed"))


def get_file():
    file_name = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', QDir.homePath())[0]
    dlg.filePathWindow.setText(file_name)
    loaded_video_data(file_name)



dlg.browseButton.clicked.connect(get_file)
dlg.convertVideo.clicked.connect(converting)

if __name__ == "__main__":

    dlg.show()
    app.exec()
