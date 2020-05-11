# Trash Panda

## Table of Contents

* Overview
  * Technologies
  * Topics
  * Intro
* The Data Pipeline
  * Challenges
* The Model

## Overview

### Technologies

* Python
* OpenCV
* Mask R-CNN
* Flask
* Docker

### Topics

* Computer vision
* Object detection
* Data engineering

### Intro

Trash Panda is the largest machine learning endeavor I have yet embarked on. I worked on
a team of three other data scientists / machine learning engineers, four web developers,
and two UX designers.

The goal was to build an app that helps create better recycling habits by reducing the
the effort required to find accurate information on how to properly dispose of any given
item of waste. To make this possible, we needed to reduce the friction so much so that
looking up how to dispose of something that a user is holding in their hand is just as
easy as debating for a few seconds on what bin it goes in.

Put another way, our goal was to reduce the cognitive tax of getting relevant recycling
information so much that disposing of every item of waste properly, regardless of what
is is, becomes effortless.

The way our stakeholder (one of the other DS team members) envisioned this goal being
achieved was to use computer vision to recognize objects and have the system
automatically bring up the relevant disposal information for the area.
[[::Rewrite::]]
The way our stakeholder envisioned it working is the user would snap a photo of
something they are about to toss but are unsure of which bin it should be tossed into.
Then, the app's computer vision (object detection) functionality would recognize the
object and automatically pull up the relevant information on how it should be disposed
of according to the user's location and available services. The user would ideally know
immediately if the item should be thrown in the trash, recycle, or compost, or if it is
recyclable but only at an offsite facility. If the latter is the case, then the user can
view a list of nearby facilities where they can take it.

We were not blessed with an iOS or Android developer, and thus were limited to using web
technologies for the app. Thus, we decided to go with a progressive web app, or PWA. For
those who aren't familiar, a PWA is basically a web app that can both be used via the
browser and downloaded to the home screen of a mobile device.

Google has been moving to fully support PWAs, and that means Trash Panda is available on
the Play Store right now. Of course the benefit of a PWA is you don't actually have to
download it at all if you don't want to. You can use it directly from the browser.

Apple is pretty far behind in their support of PWAs. As a result, the behavior on an iOS
device is not ideal. For those on iOS, be sure to use Safari and when taking a picture
of an item, you have to exit out of the video window before pressing the normal shutter
button.

You'll figure it out—I believe in you!

## Data Pipeline

As seems to be the case with most, if not all, machine learning projects, we spent the
vast majority of the time gathering and labeling our dataset.

In an ideal world, our model would be able to recognize any object that anyone would
ever want to throw away. But the reality is that this is practically impossible,
particularly within the 8 weeks we had to work on Trash Panda.

We were granted an API key from Earth911 to utilize their recycling center search
database. When we were working with it, the database held information on around 300
items—how they should be recycled based on location, and facilities that accept them if
they are not curbside recyclable.

We had our starting point for the list of items our system should be able to
recognize. However, the documentation for the neural network architecture we'd decided
to use suggested that to create a robust model, it should be trained with at least
1,000 instances (in this case, images) of each of the classes we wanted it to detect.

Gathering 300,000 images was also quite a bit out of the scope of the project at that
point. So the DS team spent many hours reducing the size of that list to something a
little more manageable and realistic.

The main method of doing so was to group the items based primarily on visual
similarity. We knew it was also out of the scope of our time with the project to train
a model that could tell the difference between #2 plastic bottles and #3 plastic
bottles, or motor oil bottles and brake fluid bottles.

[Image of plastic bottles / example]

Given enough time and resources, who knows? Maybe we could train an object detection
model that could accurately recognize 300+ items and distinguish between similar-looking
items.

We also considered the items that 1) users would be throwing away on a somewhat
regular basis, and 2) users would usually either be unsure of how to dispose of properly
or would dispose of properly.

By the end of this process, we managed to cluster and prune the original list of about
300 items and materials down to 73.

We were ready to start building out the data pipeline. We split up the tasks between the
four of us and got to coding!

I go into detail on my role in the build below, in the "Background Removal" section.

### Gather

The next step after defining our list of classes was to figure out some way of getting
somewhere in the range of 1,000 images for each one.

Timothy built the piece of the pipeline that we used to gather the majority of images. I
say majority because we also used Google's Open Images Dataset for any classes we could.

Somewhat to our surprise, Bing ended up being the most fruitful, primarily due to the
friendliness of the API.

Timothy's blog post about the Trash Panda project can be found below.

[LinkBlock]
[Trash Panda](https://www.gamesbytim.com/2020/03/trash-panda.html)

### Annotate

To train an object detection model, each image in the training dataset must be annotated
with rectangular bounding boxes (or, more accurately, the coordinates that define the
bounding box) surrounding each of the objects belonging to a class that we want the
model to recognize. These are used as the label, or target, for the model—i.e. what the
model will be trying to predict.

In order to gather and annotate over 70,000 images between four of us in only a handful
of weeks while keeping our sanity, we had to come up with some way of automating all or
part of the process.

Trevor, one of the other Data Scientists on the team, came up with an idea to automate
the labeling part of the process—arguably the most time-intensive part. Basically, the
idea was to use images that feature the items over transparent backgrounds. If the item
is the only object in the image, it would be relatively simple and straightforward to
write a script that draws a bounding box around it.

If you'd like some more detail on this, Trevor wrote a blog post about it.

[LinkBlock]
[automated bbox](https://tclack88.github.io/blog/code/2020/02/17/automated-bounding-boxes.html)

All of the major search engines allow an advanced search for transparent images, which
is what we did. Of course finding a thousand unique images of a single class of object
is already something of a task. And depending on the object, finding that many without
backgrounds was virtually impossible.

For the images that had backgrounds, we would either have to manually label them, or
find a way to automate the process and build it into the pipeline.

Because the script to label images without backgrounds was already written and working,
we decided the way to go was to find a way of automatically removing the background from
images.

This is the part of the pipeline that I built.

### Automated Background Removal

I'll give a brief overview here of how I built a system for automatically removing
backgrounds from images. If you're curious about the details, check out my separate blog
post on the topic.

[LinkBlock]
[Automated BG Removal With Python, OpenCV, and Mask R-CNN]()

I tested out a few different methods of image background removal, or foreground
extraction, depending on how you look at it. I ended up building a short image
processing pipeline that utilized a pre-trained image segmentation model (similar to
object detection) to find the object(s) in the image.

Part of the output of the image segmentation model is a series of coordinates that
describe an outline of the object(s) in the image. I then used that as a binary mask to
define the area of the image that should be kept, making the rest of it transparent.

Unfortunately, I did not have much time to spend on improving the performance of the
image segmentation model, and as a result there was still a fair amount of manual
labeling to be done after the pipeline. For example, I could have trained the image
segmentation model using around 50 images of each class. This would've made the output
mask much more accurate and reduced the time spent fixing the labels afterwards.

As it was, using only the pretrained weights, there were some object classes that it
performed very well on, while for others it did not.

### Running the Pipeline

As with building the pipeline, we split up the classes evenly amongst the four of us and
got to work gathering and labeling the images.

[Talk a bit about the challenges faced during this part?]

## The Model

### Architecture

The neural network architecture we used to train the main object detection system used
in the app (and still is being used, in case you want to try it out) is called YOLOv3:
You Only Look Once, version 3.

YOLOv3 is a state-of-the-art, real-time, single-shot object detection system.

[Use some verbiage from Shark Tank demo?]

### Training

The model was trained on a XXX sagemaker instance over the course of roughly 60 hours.

[Talk about accuracy and other metrics]

### Deployment

The trained model was deployed as a Flask API to AWS Elastic Beanstalk. Once a user
takes a photo in the app, it is sent to the detection API. The trained model runs
inference on the image, and sends back the class of item with the highest probability.






