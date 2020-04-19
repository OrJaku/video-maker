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


class Main:
    def __init__(self, fps, color, weight, height, path):
        self.output_path = os.path.join(basedir, "output/out_hc.avi")
        self.file = LoadVideo(path)
        self.video_width = int(weight)
        self.video_height = int(height)

        self.video_fps = (self.file.cap_video_fps * float(fps))
        self.video_color = int(color)

        self.fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        self.out = cv2.VideoWriter(self.output_path,
                                   self.fourcc,
                                   self.video_fps,
                                   (self.video_width, self.video_height),
                                   self.video_color
                                   )

    def modify(self):
        while True:
            ret, frame = self.file.video_file.read()
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
                resized = cv2.resize(self.file.color_value, (self.video_width, self.video_height))
                self.out.write(resized)
            else:
                break
            # cv2.imshow('frame', gray)
            if cv2.waitKey(0) & 0xFF == ord('q'):
                break

        self.out.release()



