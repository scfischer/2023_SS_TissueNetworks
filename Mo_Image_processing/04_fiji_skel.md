# 4) Skeletonization

## 4.1) Opening and viewing the volume

The determination of the medial axis skeleton of structures in images is an important processing step towards analyzing network structure.

As a simple demonstration, you will here learn how to do preprocessing and skeletonization in Fiji using a small 3D confocal image stack of the osteocyte network in bone as example.

Open the image `/storage/full-share/ocy_example.tif` ("File -> Open"), set Zoom to 200%, and duplicate the image. Using *3D Stack projection* and *Orthogonal views* (`Ctrl+Shift+h`), you can get an idea of the contents of the image volume. In the case of filamentous structures such as here, a Z projection of the standard deviation can also give a good impression - try it.

## 4.2) Filtering and Tresholding

First, we filter the image to enhance linear structures. The *Tubeness*-Plugin ("Plugins -> Analyze -> Tubeness") with *sigma=2* enhances structures where the second derivative of the intensity (curvature) is negative in at least two spatial directions (negative Eigenvalues of the Hesse matrix).

In the next step, we will apply the *Otsu* automated threshold algorithm to assign the voxels to foreground and background (Image -> Adjust -> Threshold). Select "Dark Background", then "Apply", and press "Convert to mask" and "OK" in the following dialogs.

## 4.3) Skeletonization

Now we will reduce this binary image to its *Skeleton* to be able to determine parameters such as link length and connectivity. Select the skeletonization plugin (Plugins -> Skeleton -> Skeletonize (2D/3D)). The skeletonized volume can best be viewed by projecting it with "Hyperstack -> Temporal Color Code".

The result can be investigated with "Analyze -> Skeleton". In the window "Branch Information" you get for example an evaluation of the different branches of the network. The possibilities of this plugin are quite limited however - tomorrow you will learn how to perform more advanced skeleton and network analysis in Python.