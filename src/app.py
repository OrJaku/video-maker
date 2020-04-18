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

        self.video_width = int(self.cap_video_width/2)
        self.video_height = int(self.cap_video_height/2)

# video_width = int(input(f'Put video width (current: {cap_video_width}): '))
# video_height = int(input(f'Put video height (current: {cap_video_height}): '))


        self.video_fps =(self.cap_video_fps * float((input(f'Video speed (1: Normar, 0.2: Slow, 2: Fast ): '))))
        self.video_color = int(input('RGB = 1, Gray = 0: '))

        print(f"Video length: {self.video_length},FPS {self.video_fps}, width/height {self.video_width}/{self.video_height}")
        self.fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        self.out = cv2.VideoWriter(self.output_path, self.fourcc, self.video_fps, (self.video_width, self.video_height), self.video_color)


class Main:
    def __init__(self):
        pass  

    def modify(self):
        self.file = LoadVideo()
        while True:
            self.ret, self.frame = self.file.video_file.read()
            self.gray = cv2.cvtColor(self.frame, cv2.COLOR_RGB2GRAY)
            if self.ret:
                if self.file.video_color == 0:
                    self.file.color_value = self.gray
                elif self.file.video_color == 1:
                    self.file.color_value = self.frame
                else:
                    self.file.color_value = self.frame
                self.resized = cv2.resize(self.file.color_value, (self.file.video_width, self.file.video_height))
                self.file.out.write(self.resized)
            else:
                break
            # cv2.imshow('frame', gray)
            if cv2.waitKey(0) & 0xFF == ord('q'):
                break

        self.file.out.release()
        cv2.destroyAllWindows()

main = Main()
main.modify()