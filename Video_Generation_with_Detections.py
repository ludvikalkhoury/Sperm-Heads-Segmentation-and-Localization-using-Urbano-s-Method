import cv2
import numpy as np



Initial_Frame = 900
Final_Frame   = 1190
video_name = 'Sample2 with detections.avi'

frame = cv2.imread("image/Seg_frame%d.jpg" % Initial_Frame)
height, width, layers = frame.shape

fps = 15
video = cv2.VideoWriter(video_name, 0, fps, (width,height))



for x in range(Initial_Frame,Final_Frame+1,1):
    frame = cv2.imread("image/Seg_frame%d.jpg" % x)
    video.write(frame)
    print(round(((x - Initial_Frame) / (Final_Frame - Initial_Frame)) * 100, 2), '%')


cv2.destroyAllWindows()
video.release()