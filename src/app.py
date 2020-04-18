import os
import cv2
basedir = os.path.abspath(os.path.dirname(__file__))
input_path = os.path.join(basedir, "input/hc.mp4")
output_path = os.path.join(basedir, "output/out_hc.avi")

my_video = cv2.VideoCapture(input_path)

video_length = int(my_video.get(cv2.CAP_PROP_FRAME_COUNT))
video_fps = int(my_video.get(cv2.CAP_PROP_FPS))
w = int(my_video.get(cv2.CAP_PROP_FRAME_WIDTH ))
h = int(my_video.get(cv2.CAP_PROP_FRAME_HEIGHT ))

print(video_length, video_fps)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_path, fourcc, video_fps, (w, h))
while True:
    ret, frame = my_video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)

    # cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

my_video.release()
out.release()
cv2.destroyAllWindows()
