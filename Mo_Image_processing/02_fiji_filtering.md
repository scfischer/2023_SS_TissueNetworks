# General
 
More information on the different steps can be found in the ImageJ user manual:
https://imagej.nih.gov/ij/docs/guide/146.html 
 
The sample data on which you can perform this exercise can be accessed 

on the CCTB network at storage/full-share/2023_SummerSchool/exampleData

or from this link: 
https://gigamove.rwth-aachen.de/de/download/433a3392993bf94bec80d568bb09d4d0
  
Unless otherwise stated, you can use default settings. Always keep track of your individual work steps. To do this, it is advisable to record a macro before you start the exercises:
Plugins → Macros → Record 

# 2) Filter
Please use the example image ”cell.png“.

2.1) First create three images with different image errors and save them 

	a) Salt-and-pepper noise
	
	b) High-frequency noise
	
	c) Uneven exposure
	
For a) and b), see Process → Noise. 
For c) you can proceed as follows: Create a new image (File → New → Image, Type: 8-bit, Fill with: Ramp, Width: 640, Height: 550), reduce the intensity to half: (Process → Math → Multiply (0.5)), add this image to the original image (Process → Image Calculator → Add). 

2.2) Try different filters (especially Subtract Background, Gaussian Blur and Median Filter) to remove the errors produced in 1. as good as possible. If necessary, also try different parameter values. For the uneven exposure, a Gaussian Blur with an extremely large kernel and then subtraction might help.

2.3) Create a difference image between the original "cell.png" and the images restored in 2. For each case (Process → Image Calculator → Subtract (activate 32-bit! Why?)). Also look at the corresponding histograms.
