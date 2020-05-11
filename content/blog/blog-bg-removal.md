# Automated image background removal with Python

> Series: Automated Image Background Removal Using Python

* [Resources](#resources)
* [Outline](#outline)
* [Introduction](#introduction)
  * [Photoshop](#photoshop)
  * [GIMP](#gimp)
  * [OpenCV.GrabCut](#opencvgrabcut)
  * [Image Segmentation](#image-segmentation)
* [Mask Generation using Image Segmentation](#mask-generation-using-image-segmentation)
* [Background Removal Using a Binary Mask](#background-removal-using-a-binary-mask)
  * [The Pipeline](#the-pipeline)

## Resources

* Mask R-CNN
  * [Mask R-CNN: paper](https://arxiv.org/abs/1703.06870)
  * [Mask R-CNN: MatterPort Implementation](https://github.com/matterport/Mask_RCNN/)
  * [R-CNN, Fast R-CNN, Faster R-CNN, YOLO: Object Detection Algorithms](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)
* Object detection
  * [Deep Learning for Object Detection: a Comprehensive Review](https://towardsdatascience.com/deep-learning-for-object-detection-a-comprehensive-review-73930816d8d9)
* Image processing
  * [Modular image processing pipeline](https://medium.com/deepvisionguru/modular-image-processing-pipeline-using-opencv-and-python-generators-9edca3ccb696)
* OpenCV
  * [cv2.GrabCut classes](https://docs.opencv.org/master/d7/d1b/group__imgproc__misc.html)
  * [OpenCV modules](https://docs.opencv.org/master/modules.html)
* Publications
  * [pyimagesearch](https://www.pyimagesearch.com/)

## Outline

* Introduction
  * Brief summary of the reasoning behind the problem and the proposed solution(s)
* Solution
  * Brief summary of different potential solutions, with pros and cons
    * OpenCV.GrabCut  (Link to separate article)
    * Image segmentation  (Link to separate articles)
      * Detectron2
      * Mask R-CNN
    * Others?
* Conclusions
  * Performance and level of involvitivity of each
  * Resources and further reading

## Introduction

Building pipelines. Applied machine learning is all about pipelines. And by "all about" I mean the various (ETL) pipelines that are built will do a great deal to determine the ultimate outcome of a project.

While working on a computer vision project with a team that included 3 other data scientists, we spent at least half of the entire project working on simply (or not) building the pipeline. At least one step in the main pipeline that we built to gather and process or image dataset involved a nested pipeline.

I'm not going to detail every step of the main pipeline. The example reviewed in this article is the step in the main pipeline that involved a nested pipeline. The goal with this step in the pipeline was to remove the backgrounds of images in such a way to be automated by the main pipeline. Images could then be downloaded and processed without any manual image processing needed. That was the idea anyways, and we did get it working.

I was tasked with the background removal step of the pipeline, and it was quite a journey.

### Photoshop

The first solution I came up with was to batch automate Photoshop to select and remove the backgrounds. This method was relatively simple and easy, and provided very good results, Photoshop is not open source, and thus every image that needed to have its background removed would have to be processed by my computer. We imagined what it would be like to install Photoshop on a server, but figured that Jerry-rig was not worth the trouble.

If you're interested in how I set up and executed this batch automation in Photoshop, I will eventually post a tutorial on that process.

### GIMP

After Photoshop was ruled out, the next idea was to use the open source version of it: Gnu Image Manipulation Program, better known as GIMP.

There are methods of automating GIMP using Python (a necessary part of the ideal solution). However, the features are just not quite up to snuff with that of Photoshop, enough so that we thought the work required to get that up and running wouldn't be worth it.

As an Adobe user, I'd never used GIMP prior to this. I was honestly very impressed with the functionality it did have, for being an open source software package that is maintained by volunteers.

### OpenCV.GrabCut

The next open source solution that I found in my search was an algorithm called GrabCut, of which the OpenCV library has an implementation.

* ["GrabCut": interactive foreground extraction using iterated graph cuts](https://dl.acm.org/doi/10.1145/1186562.1015720)
* [OpenCV.GrabCut](https://www.docs.opencv.org/trunk/d8/d83/tutorial_py_grabcut.html)
* [GrabCut foreground extraction OpenCV Python tutorial](https://pythonprogramming.net/grabcut-foreground-extraction-python-opencv-tutorial/)

While I was able to get some OK results using this GrabCut implementation, to get results that were somewhat close to what we wanted there was still some interaction needed. One method I tried to get around this was to simply define the bounding box of the foreground object as everything in the image except something like 1 to 20 pixels around the outside (say around 1% of the width / height), depending on the size of the image.

[ARTICLE: Foreground Extraction Using OpenCV GrabCut]

I'm sure that this algorithm could be tuned to get some better results that would have been usable for us, but in the day or so I spent on it, I was not able to do so.

So...it was onto the next.

### Image Segmentation

After some more digging around on the internet for methods of automated image background removal (or foreground extraction, depending on your viewpoint), I found an area of deep learning / computer vision called image segmentation which seemed to be exactly what we were looking for.

I had not until this point thought to use something like deep learning. The more I thought about it the more sense it made, and the demos I saw online seemed to be exactly what was needed. Basically, with image segmentation, each individual pixel is classified as either an object or not an object, with multiple object classes per image possible. The result is an image like the following, with the object, or as I'd been referring to it, the "foreground" of the image perfectly outlined and masked.

[IMAGE SEGMENTATION IMAGE]

Of course I'd have to find a way to use that mask to cut it out or remove the background, but that seemed to be the easier part. The difficult part is finding the foreground in the first place.

## Mask Generation using Image Segmentation

This article is primarily about the process of removing the backgrounds using a mask generated by an image segmentation model. Although the code is all in a single pipeline (shout-out to this article for the inspiration and structure), this article will not go into detail on how to set up the actual model(s).

For details on that step in the process, review the following articles:

[ARTICLE: Image Segmentation Using Detectron2]

[ARTICLE: Image Segmentation Using Mask R-CNN (TensorFlow)]

## Background Removal Using a Binary Mask

To a computer, an image is just an array of values that tell the display the color and intensity for each pixel. Thinking about images in that way was essential in understanding how to accomplish the background removal task in an efficient manner.

from this perspective, the binary mask generated via Detectron2 or Mask R-CNN simply classifies each pixel as a 1 or a 0 (hence the binary descriptor). Therefore, with the image and mask as arrays of the same shape, it really just comes down to inverting the mask so that the background is the 1, and subtracting that area from the original image.

The one tricky bit that had to go through a number of iterations before a good solution was found was dealing with the alpha channel. Because the images we were running through the pipeline came straight from the interwebs, the quality and format varied wildly.

### The Pipeline

The way I set up the image removal was heavily inspired by the pipeline in this article: [Modular image processing pipeline using OpenCV and Python generators](https://medium.com/deepvisionguru/modular-image-processing-pipeline-using-opencv-and-python-generators-9edca3ccb696).

The basic concept is that there is a base Pipeline class which sets up the structure such that the individual pieces of the pipeline can pass data back and forth between and among them in a modular fashion. The `RemoveBg` class below inherits from the main pipeline class, giving it the methods needed to add its processed data to the main "data" dictionary that's being passed down the pipeline.

I won't go into any more detail about the pipeline itself, as the original author of the [article](https://medium.com/deepvisionguru/modular-image-processing-pipeline-using-opencv-and-python-generators-9edca3ccb696) does a great job explaining it.

So I will start at line 36 and work my way down.

```py
import os
import sys

import cv2
import numpy as np

from forecut_pipeline.pipeline import Pipeline


class RemoveBg(Pipeline):
    def __init__(self, dst):
        self.dst = dst

        super().__init__()

    def map(self, data):
        self.remove_bg(data)

        return data

    def remove_bg(self, data):
        if "result" not in data:
            return

        result = data["result"]
        if "masks" not in result:
            return

        # Extract mask and image from data
        mask = result["masks"]
        image = data["image"]

        # We're treating all instances as one, so collapse the mask into one layer
        mask = np.sum(mask, -1, keepdims=True) >= 1

        # Create blank black background
        background = np.zeros(image.shape)

        # Copy color pixels from the original color image where mask is set
        dst_image = np.where(mask, image, background).astype(np.uint8)

        # Convert to 4-channel image
        tmp = cv2.cvtColor(dst_image.astype("uint8"), cv2.COLOR_BGR2GRAY)
        _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
        b, g, r = cv2.split(dst_image.astype("uint8"))
        rgba = [b, g, r, alpha]
        dst2 = cv2.merge(rgba, 4)

        data[self.dst] = dst2
```

Line 36 is an optional step I added in to make the mask more likely to cover the entire object in the image. Basically it just collapses all of the top object recognition masks into a single mask using an additive strategy — meaning the resulting area will be the total area of all of the masks combined, as if layered one on top of another.

CUE-- @ 07:17 | rmbg ~ CHECK: Line 36 `>=` is broadcasting boolean values to array?  

Then a black image array the same size as the image is defined. It was imperative that the final output of the image removal process be an image of the same dimensions as the original (aside from the added alpha channel). The blank black image is used in the next line as the base image array into which the pixels inside the mask (hopefully the foreground) are copied.

At this point, the image array should hold the foreground object pixels over a blank black background. The next block goes through the rather lengthy process of making the image to transparent.

First, the uint8 array is temporarily converted to OpenCV grayscale. In this case, the greyscale part is not necessarily as important as being able to manipulate it with OpenCV — i.e. the next step requires a grayscale image. After conversion, the temporary image array is run through a threshold. As described in the [cv2.threshold documentation](https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html?highlight=threshold#threshold):

> The function is typically used to get a binary image out of a grayscale image.

The purpose of the threshold, as can be derived from the variable name, is to get only the pixels in background area which will become the new alpha channel. The threshold determines at what value the pixels will be converted either to white or to black.

This is done by simply splitting the red, green, and blue channels from the image with the foreground object(s) over a black background, then joining them together again with alpha as the fourth channel.

CUE-- @ 07:41 | rmbg ~ FIX: rgba = [r, g, b, a], fix the ordering of the channels  

Once that is complete, the image array is added to the data dictionary to make it accessible by any proceeding steps in the pipeline.
