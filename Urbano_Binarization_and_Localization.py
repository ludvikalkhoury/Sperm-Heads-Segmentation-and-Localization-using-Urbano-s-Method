import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import imutils

#import cc3d
#import matplotlib.patches as patches
#import scipy as sp
#import scipy.ndimage as nd
#import argparse

LoG_Kernel = np.array([[0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556],
    [0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556],
    [0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160944539, 0.250960264167485, 0.250960160944539, 0.250960160438556, 0.250960160438556, 0.250960160438556],
    [0.250960160438556, 0.250960160438556, 0.250960160944539, 0.254266916542420, 0.636342447694017, 0.254266916542420, 0.250960160944539, 0.250960160438556, 0.250960160438556],
    [0.250960160438556, 0.250960160438556, 0.250960264167485, 0.636342447694017, -21.6315694274854, 0.636342447694017, 0.250960264167485, 0.250960160438556, 0.250960160438556],
    [0.250960160438556, 0.250960160438556, 0.250960160944539, 0.254266916542420, 0.636342447694017, 0.254266916542420, 0.250960160944539, 0.250960160438556, 0.250960160438556],
    [0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160944539, 0.250960264167485, 0.250960160944539, 0.250960160438556, 0.250960160438556, 0.250960160438556],
    [0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556],
    [0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556, 0.250960160438556]])

Disk_1 = np.uint8(np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]))
Diam_1 = np.uint8(np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]))
Diam_2 = np.uint8(np.array([[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]]))

Initial_Frame = 900
Final_Frame   = 1190
frame = cv2.imread("image/frame%d.jpg" % Initial_Frame)
height, width, layers = frame.shape



for y in range(Initial_Frame,Final_Frame+1,1):
    img = cv2.imread("image/frame%d.jpg" % y)
    Orig = img
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    for x in range(1,6,1):
        img = cv2.GaussianBlur(img,(11,11),1)

    laplacian = cv2.filter2D(img, -1, LoG_Kernel)
    Thres, Bin_img = cv2.threshold(laplacian,0,255,cv2.THRESH_OTSU)

    K = 1.1
    Bin_im = (laplacian > K*Thres)*255
    Bin_im = np.uint8(Bin_im)

    im_close = cv2.morphologyEx(Bin_im, cv2.MORPH_CLOSE, Disk_1,iterations = 1)
    im_erosion = cv2.erode(im_close,Diam_2,iterations = 1)
    im_dilate = cv2.dilate(im_erosion,Diam_1,iterations = 1)

    output = cv2.connectedComponentsWithStats(im_dilate, connectivity=8)

    num_labels = output[0]
    labels = output[1]
    stats = output[2]
    centroids = output[3]
    areas = output[2][:, 4]

    Blobs_Center = []
    inx = 0


    for c in range(0,num_labels,1):

        if areas[c] >= 5 and areas[c] <= 50:
            cent = centroids[c]

            if (cent[0] <= (width - 20) and cent[0] >= 21) and (cent[1] <= (height - 20) and cent[1] >= 21):

                Blobs_Center.append(centroids[c])

        inx += 1

    Blobs_Center = np.array(Blobs_Center)
    fig, ax = plt.subplots()

    plt.imshow(Orig)
    rect = patches.Rectangle((21, 21), width-40, height-40, linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect)

    if not Blobs_Center.size == 0:
        plt.scatter(Blobs_Center[:,0], Blobs_Center[:,1], marker="s", color="red", s=100, facecolors='none')
    plt.xticks([], [])
    plt.yticks([], [])
    plt.title("Frame %d" % y)
    fig.savefig("image/Seg_frame%d.jpg" % y)

    print(round(((y - Initial_Frame)/(Final_Frame - Initial_Frame))*100,2), '%')
