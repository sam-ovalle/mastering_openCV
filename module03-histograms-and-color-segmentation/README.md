# Module 3: Histograms and Color Segmentation

## Module Projects

### M03.01: Histograms

Exercises to obtain the distribution of values across channels of an image, and initial discussion of the use cases

The grayscale Apollo-8-Launch.jpg histogram is found using two methods:

![Alt text](readme/03_01_exercise1.png "Image of calcHist() linear plot versus hist() histogram")

The concept of histogram binning is best explained with this histogram of a checkerboard, containing values of either 0 or 255 at each pixel

![Alt text](readme/03_01_exercise2.png "Image of binning examples with checkerboard image")

calcHist() linear plots are partciularly helpful for viewing histogram distributions across different channels

![Alt text](readme/03_01_exercise3.png "Image of linear histogram plots for BGR channels")

Binary masks + bitwise operations can be used to isolate an object and perform histogram analysis only on that object. In this case, a square was simply pulled from the lake of the Emerald_Lakes_New_Zealand.jpg above

![Alt text](readme/03_01_exercise4.png "Image of isolating a mask of the lake for histogram plots of an object")

A good use case of histograms is improving contrast in an image through histogram equalization, as demonstrated below with parrot.jpg

![Alt text](readme/03_01_exercise5.png "Image of grayscale import of parrot.jpg")
![Alt text](readme/03_01_exercise6.png "Image of improved contrast on parrot image due to histogram equalization")

The same method used in the grayscale image above does not work well with BGR color channels due to the dependency of intensity on hue, thus it is better to first convert to HSV format

![Alt text](readme/03_01_exercise7.png "Image of poor color contrast improvement through equalizing BGR channel histograms")
![Alt text](readme/03_01_exercise8.png "Image of improved color contrast due to equalizing HSV channel histograms instead")

The grayscale version of the equalized HSV parrot image has a better equalized histogram distribution than before due to the accounting of intensity

![Alt text](readme/03_01_exercise9.png "Image of improved grayscale histogram from grayscale conversion of equalized HSV image of parrot")

|

|

|
