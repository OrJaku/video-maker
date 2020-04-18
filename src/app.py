import os
import cv2
basedir = os.path.abspath(os.path.dirname(__file__))
input_path = os.path.join(basedir, "input/hc.mp4")
output_path = os.path.join(basedir, "output/out_hc.avi")

my_video = cv2.VideoCapture(input_path)

video_length = int(my_video.get(cv2.CAP_PROP_FRAME_COUNT))
video_fps = int(my_video.get(cv2.CAP_PROP_FPS))
cap_video_width = int(my_video.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_video_height = int(my_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

video_width = int(input(f'Put video width (current: {cap_video_width}): '))
video_height = int(input(f'Put video height (current: {cap_video_height}): '))

video_color = int(input('RGB = 1, Gray = 0: '))

print(f"Video length: {video_length},FPS {video_fps}, width/height {video_width}/{video_height}")
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter(output_path, fourcc, video_fps, (video_width, video_height), video_color)
while True:
    ret, frame = my_video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    if ret:
        if video_color == 0:
            color_value = gray
        elif video_color == 1:
            color_value = frame
        else:
            color_value = frame
        resized = cv2.resize(color_value, (video_width, video_height))
        out.write(resized)
    else:
        break

    # cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cv2.destroyAllWindows()
