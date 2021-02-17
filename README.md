# Sperm Heads Segmentation and Localization using Urbano's Method
 In this repositoty, I will provide a Python code to the segmentation and localization method presented in Urbano *et al.* (2017) [1]. There are three main functions namely, Frame_Generation_From_Main_Video.py, Urbano_Binarization_and_Localization.py, and Video_Generation_with_Detections.py.  
 
### (1) Frame_Generation_From_Main_Video.py:  
This function will (1) import a video from your working directory, (2) create a folder and name it "image" in this it didn't exist already, and (3) generate a user-specified number of frames and then same them in the folder "image." The three variables that the user can change are "Initial_Frame" (line 7), "Final_Frame" (line 8), and "Video_name" (line 9).
 
### (2) Urbano_Binarization_and_Localization.py:  
This function is the segmentation and localization method proposed by Urbano *et al.* [1]. 
 
 
 ## Reference:  
 [1] Urbano, L. F., Masson, P., VerMilyea, M., & Kam, M. (2016). Automatic tracking and motility analysis of human sperm in time-lapse images. IEEE transactions on medical imaging, 36(3), 792-801.
