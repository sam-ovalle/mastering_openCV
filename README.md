# Mastering OpenCV

Coursework provided by OpenCV University 

![Alt text](readme/MOCV_cover.png "Homepage Image of MOCV course")

|

|

|

## Module 1: Getting Started with Images

Learning how to read in, modify, annotate, save, and display images

The image New_Zealand_Boat.jpg is read into openCV, cropped, resized to double the size, and flipped

![Alt text](module01-getting-started-with-images/readme/01_03_exercise.png "Image of New Zealand boat used in exercise")

The image Apollo-11-launch.jpgis read into openCV, text is added, and a rectangle is placed on the shuttle rocket

![Alt text](module01-getting-started-with-images/readme/01_04_exercise.png "Image of annotated Apollo 11 image used in exercise")

|

|

|

## Module 2: Arithmetic Logic and Thresholding

Learning how to change brightness, contrast, create binary masks, combine images, and remove backgrounds using alpha channels

The contrast is modified using matrix multiplication

![Alt text](module02-arithmetic-logical-thresholding/readme/02_01_exercise.png "Image of Santorini used in exercise, and modified contrasts using multiplication")

Thresholding is used to create binary masks where musical notes exist

![Alt text](module02-arithmetic-logical-thresholding/readme/02_02_exercise.png "Image of Music Sheet and output binary image")

The background of this sign JPEG image was removed, using binary masks to isolate the non-background component of the image, and merging this mask as the alpha channel to form a PNG

![Alt text](module02-arithmetic-logical-thresholding/readme/02_04_exercise3.png "Images for exercise M02.04")

An openCV logo watermark was placed on this image using masks and cv2.addWeighted()

![Alt text](module02-arithmetic-logical-thresholding/readme/02_05_exercise8.png "Images for exercise M02.05")

An e-signature transparent png was created from a handrawn signature imported as JPEG
![Alt text](module02-arithmetic-logical-thresholding/readme/02_06_exercise5.png "Images for exercise M02.06")
![Alt text](module02-arithmetic-logical-thresholding/readme/02_06_exercise6.png "Images for exercise M02.06")


|

|

|

## Module 3: Histograms and Color Segmentation