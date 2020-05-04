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


