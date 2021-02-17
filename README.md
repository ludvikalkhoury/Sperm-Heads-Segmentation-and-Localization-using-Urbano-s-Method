# Sperm Heads Segmentation and Localization using Urbano's Method [1]
 In this repositoty, I will provide a Python code to the segmentation and localization method presented in Urbano *et al.* (2017) [1]. There are three main functions namely, Frame_Generation_From_Main_Video.py, Urbano_Binarization_and_Localization.py, and Video_Generation_with_Detections.py. The main library I used in order to implement all Image Processing operations is "OpenCV."
 
### (1) Frame_Generation_From_Main_Video.py:  
This function will (1) import a video from your working directory, (2) create a folder and name it "image" in this it didn't exist already, and (3) generate a user-specified number of frames and then same them in the folder "image." The three variables that the user can change are "Initial_Frame" (line 7), "Final_Frame" (line 8), and "Video_name" (line 9).
 
### (2) Urbano_Binarization_and_Localization.py:  
This function is the segmentation and localization method proposed by Urbano *et al.* [1]. The input to this function is a frame ("FrameX" where X is the frame number) and the output is the same frame with squares around the detected sperm heads ("Seg_frameX" where X is the frame number). Note that the for loop at line 34 is used to process all the generated frames. This function could be devided into two main parts; (a) segmentation and (b) localization.  

**(a) Segmentation:** Each input frame undergoes a series of filtering before being binarized. First, the 3-channel frame is converted to a grayscale image (line 37). Second, the grayscale image is fed to a series of five Gaussian filters with size 11-by-11 and standard deviation 1. Thirds, the blurred (result of Gaussian filters) image is fed to LoG filter. Now the sharpened image (results of LoG filter) is binarized using Otsu's method [2]. In [1], the authors multiplied Otsu's threshold by a factor of 1.1 (line 45). Thereafter, the binarized image undergoes some morphological operations (closing, erosing, and dilation). At the end of this stage, the resultant binary image is ready for localization.      

**(b) Localization:** Blobs are now detected frame the binzary image. As presented in [1], blobs area is calculated and all blobs whose area is under 5 pixels are rejected. The rest are considered sperm heads and a red square a placed at the position of their centroids. At the end of this stage, images with squares around the detected heads are saved as "Seg_frameX" (where X is the frame number) in folder "image."  

*Note: In this work, I have shrunk the region of interest (RoI) of each frame by neglecting the borders (regions that are within 20 pixels from the borders). This is step, however, is not mentioned in [1]. The RoI is represented by a large red rectangle.*
  
### (3) Urbano_Binarization_and_Localization.py: 
This function generates a video from the all the images generated at the end of section **(2-b)** of this document, namely "Seg_frameX." The video is saved in the working directory. The video's name could be defined by the user at line 8.  

### (4) Testing Sample: 
"Sample2.mp4" is sperm sample I found on YouTube [3]. I used this sample in order to test the Urbano's segmentation and localization algorithm that was presented in [1].


## Reference:  
[1] Urbano, L. F., Masson, P., VerMilyea, M., & Kam, M. (2016). Automatic tracking and motility analysis of human sperm in time-lapse images. IEEE transactions on medical imaging, 36(3), 792-801.  
[2] Otsu, N. (1979). A threshold selection method from gray-level histograms. IEEE transactions on systems, man, and cybernetics, 9(1), 62-66.  
[3] Ovation Fertility. (2016, December 1). *Sperm Prep for IUI - Before and After* [Video]. YouTube. https://www.youtube.com/watch?v=5ytxRZ5i74g 


## Keywords:  
Urbano's Segmentation and Detection, Python, OpenCV, Image Processing, Binarization, Multiple Blobs Detection, Image Filtering, Blurring, Sharpening, Morphological Operations, Sperm Head Detection, Video Reading, and Video Generation.
