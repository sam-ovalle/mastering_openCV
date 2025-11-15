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