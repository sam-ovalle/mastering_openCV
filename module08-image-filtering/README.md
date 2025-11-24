# Module 8: Image Filterning 

## Exercises

### M08.01: Image Filtering and Convolution

Exercises to understand how low frequency and high frequency filters are represented as NxN kernels in images that blur or sharpen images

In the first exercise, kitten.jpg is blurred using a box filter. These NxN kernels change the pixel value to be the average value of an NxN box surrounding them at the center

![Alt text](readme/08_03_filter1.png "Image of 3x3 box filter kernel") ![Alt text](readme/08_03_filter2.png "Image of 5x5 box filter kernel")
![Alt text](readme/08_03_example1.png "Image of kittens before and after box filter blurring")

Another method to blur an image is using a Gaussian filter, which calculates the mean of a normal distribution around the central pixel covering an NxN box, defined by a standard deviation

![Alt text](readme/08_03_filter3.png "Image of gaussian plot turned into a 5x5 kernel")
![Alt text](readme/08_03_example2.png "Image of resulting blur from box filter versus gaussian filter")

Increasing the standard deviation produces higher blur in the output image

![Alt text](readme/08_03_example3.png "Image of resulting plot at varying standard deviations when using a gaussian filter")

In order to sharpen an image, the kernel type needed resembles this structure, where the central value outweighs its negating surrounding values

![Alt text](readme/08_03_filter4.png "Image of sharpening kernel used")
![Alt text](readme/08_03_example4.png "Image of resulting sharper image of saturn from applying sharpening kernel")

The blurred image of the kittens can be recovered using these sharpening kernels

![Alt text](readme/08_03_example5.png "Image of recovering the blurred image of a kitten using the sharpening kernel")

|

|

|

### M08.02: Edge Detection

Exercises to understand the use of convolution kernels to detect edges

First, we explored the Sobel edge detection method, where 3x3 kernels can identify edges in a direction

![Alt text](readme/08_04_exercise1.png "Image of Sobel filter kernels")

In the first example, we generate a vertical intensity gradient for a grayscale image using the Sobel-X kernel

![Alt text](readme/08_04_exercise2.png "Image of 8x8 grayscale processed into an intensity gradient using the Sobel-X kernel")

The vertical and horizontal edges are each identified separately, and their edge maps would need to be combined and thresholded in order to collect edges. This can be seen below with the processed checkerboard_color.png

![Alt text](readme/08_04_exercise3.png "Image of colored checkerboard processed using both Sobel-X and Sobel-Y to output a vertical and horizontal edge map")

We then discuss the Canny edge detection method, an expansion on the Sobel method where edges above a high threshold value are considered "sure" edges, and edges below that but within a lower threshold value are vetted against these "sure" edges to determine continuity, or else theyre discarded

![Alt text](readme/08_04_exercise4.png "Image of visualization of edge matching process used in Canny filter")

The Canny method can produce reliable edge maps as binary masks, such as this outline of the coca-cola-logo.jpg

![Alt text](readme/08_04_exercise5.png "Image of color coca cola logo processed into edges using Canny filter")

In addition, modifying the upper threshold for the Canny filter can remove edges with lower contrast, such as this gray phone's features from phone_ipad.jpg

![Alt text](readme/08_04_exercise6.png "Image of differing edges collected from iphone and ipad image at varying upper thresholds of the Canny filter")

In relation to the prior module, blurring the grayscale image smoothens edges, removing noise present in edge detection as seen below

![Alt text](readme/08_04_exercise7.png "Image of grayscale butterfly and iguana before and after blurring")
![Alt text](readme/08_04_exercise8.png "Image of edges detected by Canny filter before and after blurring")

Finally, lowering the lower threshold allows the Canny edge detector to pick up on less sharp edges, such as the antennae of this butterfly

![Alt text](readme/08_04_exercise9.png "Image of differing edges collected from butterly image at varying lower thresholds of the Canny filter")

|

|

|

### M08.03: Camera Edge Detection

Exercise to combine reading camera frames with edge detection

The 08_03_Camera_Edge_Detection_Demo.py script accesses the camera on my computer and outputs preview frames and frames that have passed through a Canny filter for edge detection

Below is a gif of myself using it

![Alt text](readme/08_05_exercise.gif "Gif of output of script that reads camera input and outputs binary mask frames (edge detection from the Canny filter)")

|

|

|

## Applications

### M08.04: Image Filter Effects

Exercises to understand how different image filter effects may be generated using convolutions

Image filters explored:

Sepia / Vintage is generated through a 3x3 kernel

![Alt text](readme/08_05_exercise1.png "Image of Sepia image filter input / output")

Vignette is generated through gaussian blur encompassing the width and height

![Alt text](readme/08_05_exercise2.png "Image of Vignette image filter input / output")

Embossed is generated through a diagonal 3x3 linear filter

![Alt text](readme/08_05_exercise3.png "Image of Embossed image filter input / output")

Exposure is increased through an absolute scale kernel (abstracted cv2 method)

![Alt text](readme/08_05_exercise4.png "Image of Exposure image filter input / output")

Outlines are sharpened through a 3x3 kernel

![Alt text](readme/08_05_exercise5.png "Image of Outlines image filter input / output")

A pencil sketch can be generated from an abstracted cv2 method

This increases outlines on an embossed grayscale image

![Alt text](readme/08_05_exercise6.png "Image of Pencil Sketch image filter input / output")

Stylization can similarly be generated from an abstracted cv2 method

An edge detection mask is set to a color value (such as black)

![Alt text](readme/08_05_exercise7.png "Image of Stylization image filter input / output")

|

|

|

### M08.05: Streamlit Filters App

Expanding on the prior application by turning it into a WebUI with Streamlit

![Alt text](readme/08_06_exercise.gif "Gif of Streamlit webUI for image filters")