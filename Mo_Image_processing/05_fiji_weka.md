# 5) Machine Learning Segmentation

This tutorial was adapted from https://imagej.net/plugins/tws/.

## 5.1) Opening the example image and the WEKA plugin

Open the example image *TEM Neurons*. The goal here is to detect the cell boundaries in order to trace the neurons in this electron microscopy image of brain tissue. Intensity tresholding will not work here, since there are other dark structures such as mitochondria. Instead, we will use machine learning to train an algorithm using pixel features (filters).

Start the WEKA Segmentation plugin (Plugins -> Segmentation -> Trainable Weka Segmentation). The open image will automatically be loaded. On the left side you find the buttons for training and options - currently most of them are greyed out. On the right hand side, there is a list of all pixel classes. For now, two classes have been defined (for example, foreground and background).

## 5.2) Labelling training examples (ground truth)

The trainable WEKA segmentation plugin is an example for pixel classification. So we first have to label a few pixels as training examples for the classifier to be able to predict the class of unlabelled pixels based on their features.

You can use any of the ROI tools in Fiji - the freehand tool is initially selected. The line thickness can be varied by double click on the tool button. Create a few ROIs of cell membranes or cell interior and add them to the first or second class using the buttons on the right. Traces can be removed from the list by double click.

## 5.3) Training a classifier

Now click on the button "train classifier" to start training using the ground truth labels. As a first step, the features of the image are calculated - this can take some time depending on the size of the image and the number of features, but only needs to be done once. After training is finished, every pixel will be colored with one of the two class colors.

Try to improve the quality of the prediction by adding new labels. With "create result" you can obtain a new binary image with the predictions, and "get probability" generates separate probability maps for each class.

For a more detailed introduction, have a look at the official documentation (see link on top).


