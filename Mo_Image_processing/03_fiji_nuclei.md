# Segmentation

## 3.1) Segmentation in 2D
Please use the example image “cellNuclei_cropped.tiff“.
1.	Adjust the brightness and contrast (Image->Adjust->Brightness->Contrast->Auto)
2.	Choose an appropriate threshold to separate the image in foreground and background (Image → Adjust → Threshold)
3.	Measure the cell nuclei (Analyze → Analyze Particles: Show: Outlines, tick Display results, see also https://imagej.nih.gov/ij/docs/menus/analyze.html#ap for details on the options)
4.	Redo those steps and apply a Gaussian filter after step 1. How does the result change?
5.	Play around with the parameters. Once you are confident that all segmented structures are nuclei, save the Results table as .csv file.

## 3.2) Segmentation in 3D
Please use the example image “3DBlobs.tif”
1. Change Image-> Properties to 1,1,4
2. 2D Projections: Image -> Stacks -> Orthogonal Views
3. Analyze->3D objects counter
>Do not tick „Exclude objects on edges“  
 Look at the result. Is it correct?
 4. Again: Analyze->3D objects counter of the original image
>Now, please tick „Exclude objects on edges“  
How does this result differ from the previous one? Why?



## 3.3) Advanced: Real images
2D segmentation of example image “cellNuclei.tif”

3D segmentation Dapi channel of mouse embryo, example image “DAPI_mouseEmbryo.tif”
