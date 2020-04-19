import os
import cv2


class LoadVideo:
    def __init__(self):
        self.basedir = os.path.abspath(os.path.dirname(__file__))
        self.input_path = os.path.join(self.basedir, "input/hc.mp4")
        self.output_path = os.path.join(self.basedir, "output/out_hc.avi")
        self.video_file = cv2.VideoCapture(self.input_path)

        self.video_length = int(self.video_file.get(cv2.CAP_PROP_FRAME_COUNT))
        self.cap_video_fps = int(self.video_file.get(cv2.CAP_PROP_FPS))
        self.cap_video_width = int(self.video_file.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.cap_video_height = int(self.video_file.get(cv2.CAP_PROP_FRAME_HEIGHT))


class Main:
    def __init__(self, fps, color, weight, height):

        self.file = LoadVideo()
        self.video_width = int(weight)
        self.video_height = int(height)

        self.video_fps = (self.file.cap_video_fps * float(fps))
        self.video_color = int(color)
        print("COLOR", type(self.video_color))

        self.fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        self.out = cv2.VideoWriter(self.file.output_path,
                                   self.fourcc,
                                   self.video_fps,
                                   (self.video_width, self.video_height),
                                   self.video_color
                                   )

    def modify(self):

        while True:
            ret, frame = self.file.video_file.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
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
        cv2.destroyAllWindows()



