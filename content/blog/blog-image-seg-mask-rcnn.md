# Create binary mask for objects in an image using Python and Computer Vision

* [Resources](#resources)
* [Outline](#outline)
* [Goal](#goal)
  * [Computer vision](#computer-vision)
  * [Mask R-CNN](#mask-r-cnn)

## Resources

* [Mask R-CNN](https://github.com/matterport/Mask_RCNN/)
* Other models / frameworks
  * [CenterMask2](https://github.com/youngwanLEE/centermask2)
  * [Yolact](https://github.com/dbolya/yolact)

## Outline

* Intro
  * Goal
  * Solution
    * Computer vision models
    * Mask R-CNN
* Content
  * Using pre-trained weights
  * Training a custom model
  * Extracting the data from the predictions:
    * Masks
    * Bounding boxes
* Conclusion

## Goal

The goal of this article is to describe a possible process for utilizing an image segmentation model to create binary masks for one or more objects in an image. A binary mask essentially is a black and white (like actually only pure black and pure white) image with the same dimensions of the image that can be used to distinguish pixels in the original image.

One important use-case for something like this is to separate the foreground from the background, making it possible to easily manipulate background pixels without affecting the foreground. For example, blurring the background to give a greater depth of field effect, or removing the color from the background to make the foreground really pop out.

### Computer vision

In order to generate binary masks based on the content of the image, the algorithm must be somewhat intelligent. That is, it must be able to process the image in such a way that it can recognize where the foreground is and draw a polygon around it with some degree of accuracy.

Luckily, there are a number of machine learning models that will do just that. The field is called Computer Vision. More specifically, the models described in this article are known as image segmentation models.

Don't worry if you don't have any experience with this type of thing, or even if you don't want to _get_ experience with it. Modern machine learning tooling makes it incredibly quick and easy to get a model up and predicting with pre-trained weights.

One caveat though: the pre-trained models will do great with the objects that were in their training data. Depending on what the object in the foreground is that you are trying to extract, you may or may not need to extend the model with a custom dataset and training session.

### Mask R-CNN

The primary model used in this article is Matterport's implementation of a Mask R-CNN (Regional Convolutional Neural Network). Although it hasn't changed much in the last couple years, it is still one of the best implementations of an image segmentation model out there today.
