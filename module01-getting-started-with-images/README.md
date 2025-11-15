# Module 01: Getting Started With Images

## Image Basics

### Geometry of Image Formation 

Understanding the theory of how an image is formed and camera intrisnics

In this simplified camera model, the pinhole size and focal length can be used to determine the expected size of an object, and its relationship to distance from the camera

![Alt text](readme/module1-geometry1.png "Image of camera intrinsics model")

In order to keep an object in focus across a lense, the object must be projected within an intersection plane between a ray across the center of the lense and a ray normal to the lense

![Alt text](readme/module1-geometry2.png "Image of rays defining a focus length")

### Digital Image Formation

Understanding the formation of digital color images and formatting used in openCV

Each of RGB color channels is generated on separate cells of a matrixed light sensor, and demoized to interpolate neighboring values, forming a complete color image

![Alt text](readme/module1-digital1.png "Image of color image formation process")

The data structure of a JPEG image

![Alt text](readme/module1-digital2.png "Image of JPEG data structure")

The data structure of an openCV C++ implementation Matrix (Mat) class image

![Alt text](readme/module1-digital3.png "Image of openCV Mat class image data structure")

### Image Formats

Understanding the history of image formats and their use cases

.gif

    - Useful in repeating moving image but memory dense

.png

    - Lossless image compression (good for maintaining details)
    - supports alpha channel

.jpg / .jpeg

    - Lossy image compression (leaves artefacts in image)
    - no alpha channel

.webm

    - Lossless and Lossy image compression
    - More memory efficient than PNG
    - Developed by Google under BSD license
    - Not widely adopted yet :(

## Module Projects

### M01.01: Reading, Displaying, Saving Images

Exercises to read image formats into openCV, view matrix data struccture, display images in line, and save images

The image Apollo-11-launch.jpg was read into openCV, displayed in jupyter notebooks, and saved to a png as Apollo-11-launch-edit.png

![Alt text](Apollo-11-launch-edit.png "Image of Apollo 11 launch vehicle used in exercise")

### M01.02: Color Images

Exercises to modify channels of color images, convert to different color formats, and ensure appropriate use of channels per image format

The image Emerald_Lakes_New_Zealand.jpg is read into openCV, converted to grayscale, and displayed with attribute data

![Alt text](readme/01_02_exercise.png "Image of New Zealand lake used in exercise")

### M01.03: Basic Image Manipulation

Exercises to copy images, manipulate pixel values, crop, resize, and flip images

The image New_Zealand_Boat.jpg is read into openCV, cropped, resized to double the size, and flipped

![Alt text](readme/01_03_exercise.png "Image of New Zealand boat used in exercise")

### M01.04: Annotating Images

Exercises to draw lines, circles, rectangles, and add text to images

The image Apollo-11-launch.jpgis read into openCV, text is added, and a rectangle is placed on the shuttle rocket

![Alt text](readme/01_04_exercise.png "Image of annotated Apollo 11 image used in exercise")