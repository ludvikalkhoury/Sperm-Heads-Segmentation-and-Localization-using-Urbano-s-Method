import cv2
import numpy as np
import os



Initial_Frame = 900
Final_Frame   = 1190
Video_name = 'Sample2.mp4'

# Import Video
Vid_Obj = cv2.VideoCapture(Video_name)
Vid_Obj.set(1,Initial_Frame)
success,image = Vid_Obj.read()

if not os.path.exists("image"):
    os.makedirs("image")

# Generate N Frames
for x in range(Initial_Frame,Final_Frame+1,1):
  cv2.imwrite("image/frame%d.jpg" % x, image)     # save frame as JPEG file
  Vid_Obj.set(1, x)
  success,image = Vid_Obj.read()

  print('Generate Frame Number: ', x)


