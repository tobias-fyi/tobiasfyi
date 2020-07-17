# Skim images quicker with Python and OpenCV

## Resources

- [OpenCV: Getting started with images](https://docs.opencv.org/master/dc/d2e/tutorial_py_image_display.html)

---

## Outline

- Intro
  - Brief summary of the problems
    - Current one: visually vetting / organizing images for CV dataset
    - On-going: organizing large numbers of GoPro time-lapse images
  - Brief summary of the solution
    - Python
    - OpenCV (note about macOS versions)
      - TODO: Test it out on Ubuntu
    - Click (or other cli tool like clize)
- The Code / Tutorial (In The Weeds)
  - More in-depth walk-through of the solution
  - How to utilize it
    - Installation
    - Configuration
    - Usage
- Conclusion
  - Summary and outro
  - Future iterations

---

## Article Body

### Overview

To skip to the tutorial section of this article, use these links:

- [Resources](#resources)
- [Outline](#outline)
- [Article Body](#article-body)
  - [Overview](#overview)
  - [The Problem](#the-problem)
  - [The Solution](#the-solution)
    - [v0.0](#v00)
    - [v0.1](#v01)
    - [v0.2](#v02)
  - [The Breakdown](#the-breakdown)
    - [Function Definition](#function-definition)
    - [Files Loop](#files-loop)
    - [Valid Files](#valid-files)
    - [Load and Display Images with `opencv-python`](#load-and-display-images-with-opencv-python)
    - [Accepting Key Commands](#accepting-key-commands)
    - [Walka Walka](#walka-walka)
    - [Creating a CLI with Clize](#creating-a-cli-with-clize)
  - [Conclusion](#conclusion)
    - [Future iterations](#future-iterations)
      - [v0.3](#v03)
  - [Summary](#summary)

A small disclaimer: this is by no means the best or most efficient method of sifting through large numbers of images. This article simply describes the mental processes I went through and code I wrote to make them work.

If you have a better way of doing the below, I'd love to discuss it with you!

### The Problem

Even before I got into computer vision, I commonly spent what I'd deem an inordinate amount of time sifting through large quantities of images.

For the last 15 or so years, my primary device for capturing photos, particularly while traveling, has been my beloved GoPro (more precisely, GoPros, plural). I love the fact that I can attach one or more GoPros to different surfaces or objects, usually via a flexible tentacle tripod, and leave it on photo time-lapse mode to capture an entire scene for an extended period of time.

There are a couple of benefits of this method that I particularly enjoy. First, I don't have to carry a camera around, and can thus take part in any activity without worrying about it. Second, it's easy for people to forget it's there, leading to truly candid shots, sometimes capturing rare, comical, or intimate moments that may otherwise not have been possible to capture.

The issue, as I'm sure you've already gathered, is that this leads to large numbers of image files. Sometimes, if I leave the camera on for long enough, we're talking thousands upon thousands of images.

I am currently working on a computer vision app, and as we started gathering our dataset of images with which we would train our object detection model, I soon realized that I was encountering the same problem. This time, however, it is tens of thousands of images—far too many to go through using my old method.

Not only did we have a fast-approaching deadline for having a decently-trained model deployed, but I simply wanted to spend as little time as possible sifting through images. In case you haven't had the pleasure, it's not a particularly joyful exercise (though it can be when sifting through GoPro time-lapse photos).

The method we decided to use to gather the images for our dataset involved utilizing various Python packages to bulk-download images from the largest image search engines (Google, Bing, Flickr, etc.). We basically trawled the internet with huge nets, capturing everything with vaguely similar characteristics to what we were looking for. Therefore, there was really no way of getting around the fact that, in order to have any decent level of quality and consistency in the final dataset, we'd have to visually vet.

As I'm sure you're aware, whether or not you've experienced it first-hand or not (yet), the internet is almost entirely made up of random stuff, some of which couldn't help but get caught up in our nets.

Just to be clear, I am very much opposed to the practice of trawling the ocean for fish. I used that analogy because it is so vivid and is a rather accurate one, though no actual nets are involved (if they were, it would literally be trawling).

On the internet—now that's a different story.

### The Solution

A good solution to this problem would allow me to easily and quickly move inside a directory of images, manipulating each file with a single keystroke.

#### v0.0

Before learning how to write scripts to automate this type of thing, I would sift through them very manually by opening up a finder window (I used Apple OS's almost exclusively until recently, and it's still my primary OS), selecting the top one, pressing the spacebar to preview it, and use the arrow keys to navigate up and down the list. When I came to an image or series of images I wanted to keep or label as "good", I manually selected and dragged them with the cursor.

This wasn't a terrible method, as the preview functionality on OS X (are we calling it macOS now?) is actually quite good. Clicking through images was quick enough; it was the manual file manipulation—using the cursor to (re)move and rename—that added the lion's share of time to the process.

I'm over a year into my Python programming journey and consider myself solidly in the "intermediate" stage. Nowadays, whenever I run into a process like this that requires a ton of repeated manual actions, my mind immediately starts thinking of ways I could automate it.

You're reading an article about it, so I imagine you can relate.

#### v0.1

The most straightforward, bare-bones version of this a program—proof-of-concept, one might say—would be set up as follows:

- Input
  - Path to a directory full of images
  - Path to a directory into which the good images will be moved
- Display images, one at a time
  - Move one-way through the list of images
- I tell the program what to do with it
  - "d" leaves the image as-is ("d" for to-be-deleted)
  - "s" moves image into "good" directory
  - "esc" closes the program

Simple as that. Even a simple script with the above functionality would save me valuable time.

The Python code I wrote to accomplish the above can be found HERE.

```py
# Some code
```

This implementation works. Not particularly well, but it does the basics of what I set out to do with this. Even if I left it at this stage, it would likely save me a significant amount of time.

However, as you may already be thinking, there are some more low-hanging fruit—easy additions to make it better.

#### v0.2

There is one piece of fruit in particular that I'm thinking of, without which one might run into issues with larger numbers of images.

Take a second and think about it...

Got it?

> The ability to move in both directions along the list of files.

During the beginning of the dataset aggregation and cleansing process for the CV project, I went through a few iterations of directories using v0.1 of the script. As I said above, the thing did what it was supposed to.

However, it was a huge bummer to accidentally save an image that absolutely didn't fit in the dataset, especially if that happened at image 1,200 out of 1,400. I would either have to start the process over from the very beginning or guess at the image's index, exit out of the script, and insert that index into the `for` loop (`for index, file in enumerate(sorted(files)[1200:]):`), and start the process from that index.

Obviously this is somewhat detrimental to the basic purpose of the script: to save time.

Therefore, my next goal was to modify the code to allow for all of the above functionality, plus moving in both directions along the list of files.

Now let's break down to different pieces of this to get a little better idea of how it works.

### The Breakdown

```py
# Entire block of code, or link to file in github repo.
```

I'll start with the standard library modules and work my way down, briefly explaining the purpose of each one in the script.

`os` and `shutil` are used to navigate and manipulate (read / write) the local filesystem. `sys.exit` The `collections.Counter` and `pprint` are used in a helper function to capture and display basic statistics about files in a directory tree (folders and sub-folders). They are not used in the main function of the skimmer.

[Could also just explain with short informative comments in the code]

```python
from collections import Counter  # Count files of each type
import imghdr  # Determine image file type
import os  # Used to navigate and manipulate the local filesystem
from pprint import pprint  # Display Python arrays in a more readable format
import shutil  # Used to navigate and manipulate the local filesystem
import sys  # `sys.exit` used to exit program early under certain conditions

import cv2  # Used to load and display images
```

The only third-party library I used for this iteration is `cv2` (opencv-python).

- [opencv-python on pypi](https://pypi.org/project/opencv-python/)
- [opencv-python on github](https://github.com/skvark/opencv-python)

Considering this use-case does not require most of the more extensive and intensive tools within OpenCV, I looked around for a lighter library that would allow me to view images and manipulate them based on keyboard input. I could not find any other library with that capability.

#### Function Definition

```py
def skim(src: str, dst: str, anno: str, exts: list = [".png", ".jpg", ".jpeg"]):
    """
    Skims through images in a directory, taking action on them as needed.
    Files with extensions not in the `exts` list will be removed automatically.
    """
    # Create destination directories if needed
    os.makedirs(dst, exist_ok=True)
    os.makedirs(anno, exist_ok=True)

    # Move into src directory
    os.chdir(src)
```

The first bit of actual code defines the function and its arguments. The list of extensions defaults to the usual image extensions but can be overridden by passing in a list. Files with extensions not in the list will be automatically deleted.

Inside the function, the first thing to do is make the directories into which files may be moved. The `exist_ok=True` flag simply means that if the directory already exists, move on and don't throw an error.

After that, the current working directory is switched to the source directory. While not completely necessary, it makes things simpler when referencing files in the case of this script not being called from the source directory, which is likely the case. By moving into the directory, the relative filepaths to the images will be something like `000001234.png`, instead of `../../pipeline/images/mixed_paper/000001234.png`.

#### Files Loop

Next, we set up the variables to be used in the loop. First, a list of files is generated from listing the contents of the source directory. This could also be done by passing `os.getcwd()` into the `os.listdir()` call, as we moved into the source directory already.

```py
def skim(...):
    ...
    # Set up loop vars
    files = sorted(os.listdir(src))  # List to manage active files
    counter = 0
    # Use while loop to be able to go both ways along active file list
    while counter < len(files):

        # Get current filename
        file = files[counter]
```

As I alluded to above, the reason I am using a `while` loop in this iteration is so I can have more control over how the loop progresses. The `counter` variable could just as well be `head` or `active_file`, both of which may be more indicative of the function of the variable. The `counter` is used to track the index of the current list item (image file) that is being viewed. And because a `while` loop is being used, this index can be used to move backward and forward through the list of files by adding 1 or subtracting 1, respectively.

Inside the loop, the name of the current file is extracted from the list using the `counter` as the index. I did this to be able to refer to the filename itself rather than use the indexing syntax every time. That would work as well, and wouldn't really change anything except, in my opinion, readability.

The reason for the next block of code is solely because I wanted some sort of indication of where I was in the list. When sorting through 2,000 files, it is nice to know how far I've come. Plus, in case something blows up and/or the program fails, I'll know generally where it was when that happened. There are, of course, many better ways of tracking this, but this was my initial solution.

```py
if counter % 10 == 0 and counter != 0:
    print("!!...........CONGRATS..........!!")
    print(f"You are at -> {counter} <- images!")
```

After that, we get to where the code checks the file's extension against the list of valid extensions.

#### Valid Files

First, the extension is extracted using the `os.path.splitext()` function. The output of that function is a list in which the extension is the last item, accessed via the `list[-1]` syntax. The output of that is then forced into lowercase to normalize any funky capitalizations.

The `imghdr.what()` function is also called on the file to determine if the file is in fact an image file (and not a directory). If the file is not an image, the option is provided to delete the file.

```py
def skim(..., exts: list = [".png", ".jpg", ".jpeg"]):
    ...
    while counter < len(files):
        ...
        # Get file extension
        file_ext = os.path.splitext(file)[-1].lower()
        # Get file type
        file_type = imghdr.what(file)

        # Remove invalid file types
        if file_ext not in exts:
            if os.path.isfile(file):
                print(f"{file} is '{file_ext}'. Deleting...")
                os.remove(file)  # Delete file
                files.remove(file)  # Remove from active files list
                # Don't increment counter, because removal shifts index
                print("\b File deleted.")
                continue
            else:
                print(f"{file} is a directory.")
                counter += 1  # No change in file list, increment index
                continue
```

Once the extension and file type is extracted, we can check it against the list of valid extensions, which defaults to `[".png", ".jpg", ".jpeg"]`. If the current file's extension is not in the list, it should be removed. However, if that was the only logic, then anything without an extension would be removed, which includes directories. Thus, the extra `if` statement to determine if it is a file or directory. If it is a file, remove it; a directory, do nothing and move onto the next file in the list.

One bug I ran into when I was first developing this script was the whole deal with the files being removed from both the filesystem and the list of active files. I initially had the counter incrementing up by one in both cases: if the file was removed and if it wasn't.

Can you think of what issue that would create?

Of course the comment gives it away, but it took me a little while to figure it out. If the file is removed from the list of active files, all the proceeding items in the list get shifted over by 1. Therefore, with the `counter` not changing at all, it will point to the index of the next file in the list. If `counter` is _also_ incremented in this case, it would skip over an image every time one is removed.

One improvement that could be somewhat easily made here is using the [imghdr](https://docs.python.org/3/library/imghdr.html) module to confirm that the image

#### Load and Display Images with `opencv-python`

Now that we have an image file of an acceptable type, we get into the real meat of the code - using opencv-python to display the image.

```py
def skim(..., exts: list = [".png", ".jpg", ".jpeg"]):
    ...
    while counter < len(files):
        ...
        else:  # File has valid extension
            try:  # Load image
                img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
            except cv2.error:
                confirm = input(f"\nFailed to load {file}.\n-> Delete file? [Y/n]\n")
                if confirm.lower() != "n":
                    os.remove(file)  # Delete file
                    files.remove(file)  # Remove from active files list
                    # Don't increment counter, because removal shifts index
                    print("Deleted.")
                    continue
                else:
                    print("Exiting program...")
                    sys.exit()

            # Create and resize the display window
            window = f"{os.path.split(src)[-1]} - {file}"
            cv2.namedWindow(window, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(window, (800, 800))

            try:  # Show image
                cv2.imshow(window, img)
            except cv2.error:
                confirm = input(f"\nFailed to open {file}.\n-> Delete file? [Y/n]\n")
                if confirm.lower() != "n":
                    os.remove(file)  # Delete file from filesystem
                    files.remove(file)  # Remove from active files list
                    # Don't increment counter, because removal shifts index
                    print("Deleted.")
                    continue
                else:
                    print("Exiting program...")
                    sys.exit()
```

The first part here is loading the image file into an array that can be displayed using code. As I mentioned above, the only library I found that can both display images and process key commands was [OpenCV](https://docs.opencv.org/trunk/index.html). The try/except statement here is meant to prevent the program crashing due to incorrectly-labeled files (e.g. extension is `.jpg` but is actually a text file). When a file fails to load, the program gives the option to delete the file or exit the program.

Once the image is loaded, we create the window in which it will be displayed. The `namedWindow` method is used in order to, of course, give the window a name. That also allows the window to be resized, so that all images are squeezed or stretched into the 800x800 window.

After that, another try/except to catch any invalid files that somehow slipped through the cracks. Always good to handle exceptions. This block provides the same options as before for deleting the file or exiting the program.

#### Accepting Key Commands

With the image loaded and now displaying to the user, we are onto the last part: determining what to do when certain keys are pressed.

```py
def skim(..., exts: list = [".png", ".jpg", ".jpeg"]):
    ...
    while counter < len(files):
        ...
        else:  # File has valid extension
            ...
            # Wait for and take action based on keystroke
            # "0" means wait indefinitely
            k = cv2.waitKey(0) & 0xFF
            if k == 27:  # ESC key exits entire program
                cv2.destroyAllWindows()
                break
            elif k == ord("s"):  # Do nothing; open next image
                cv2.destroyAllWindows()
                counter += 1
                continue
            elif k == ord("b"):  # Do nothing; open previous image
                cv2.destroyAllWindows()
                counter -= 1
                continue
            elif k == ord("m"):  # Image is good; wrong class
                if not os.path.exists(os.path.join(dst, file)):
                    shutil.move(file, dst)
                    files.remove(file)  # Remove from active files list
                    # Don't increment counter, because removal shifts index
                    print(f"File moved to '{os.path.split(dst)[-1]}'.")
                else:
                    confirm = input("\n File exists. Delete file? [Y/n]\n")
                    if confirm.lower() != "n":
                        os.remove(file)  # Delete file from filesystem
                        files.remove(file)  # Remove from active files list
                        # Don't increment counter, because removal shifts index
                    else:
                        counter += 1
                cv2.destroyAllWindows()
                continue

            # Image is good; correct class; requires manual annotation
            # i.e. image contains multiple objects
            elif k == ord("a"):
                if not os.path.exists(os.path.join(anno, file)):
                    shutil.move(file, anno)
                    files.remove(file)  # Remove from active files list
                    # Don't increment counter, because removal shifts index
                    print(f"File moved to '{os.path.split(anno)[-1]}'.")
                else:
                    cv2.destroyAllWindows()
                    confirm = input("\n File exists. Delete file? [Y/n]\n")
                    if confirm.lower() != "n":
                        os.remove(file)  # Delete file from filesystem
                        files.remove(file)  # Remove from active files list
                        # Don't increment counter, because removal shifts index
                    else:
                        counter += 1
                cv2.destroyAllWindows()
                continue
            elif k == ord("d"):  # Image is bad; delete it altogether
                os.remove(file)  # Delete file from filesystem
                files.remove(file)  # Remove from active files list
                # Don't increment counter, because removal shifts index
                print("File deleted.")
                cv2.destroyAllWindows()
                continue
```

As the comment mentions, passing a `0` into the `cv2.waitKey()` function makes the program wait indefinitely for a key press. Alternatively, a number of milliseconds can be passed in here, after which the program will automatically move on.

I'm not going to go over every single option here, as I tried to make the comments as explanatory as possible. But here are the options:

- `ESC`: exit program
- `s`: move to next image
- `b`: move to previous image (note the negative increment of the counter variable)
- `m`: "mis-classified" - the image is good, but does not contain object(s) of the class in question
- `a`: "annotation required" - image requires manual annotation, because of multiple instances or a tricky angle
- `d`: delete the image

And that's about it! The details of what is happening in this block was either explained earlier or is self-explanatory. If not, all of the libraries used have good documentation.

#### Walka Walka

This part of the code is not _really_ part of the image_skimmer script, but I found it to be a nice addition so I'm including it here as well.

```py
from collections import Counter
from pprint import pprint

def walka(root_dir: str, exts: list = None, contains: list = None):
    """Walks through a directory tree and counts the leaves."""
    print(os.path.split(root_dir)[-1])  # Visual confirmation of root
    # Instantiate file extension counter
    if exts:  # Only count extensions in ext list
        ext_counter = Counter(exts)
    else:  # Count all extensions in tree
        ext_counter = Counter()
    counter = 1
    for root, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            counter += 1
            ext = os.path.splitext(file)[-1].lower()
            ext_counter[ext] += 1

    print("Total files:", counter)
    print("Extensions:")
    pprint(ext_counter.most_common())

    return counter
```

This function basically walks through every file in every directory under (inside) a root, counting the files. I found it very useful for getting a quick summary of how many files are in the directory that I am / was skimming, including a simple count of the number of each type.

The way the `skim.py` code is set up right now, the `walka()` function runs at the end up a skimming session. It counts the total number of files, the number of different extensions, and the number of files with each of the extensions.

To count the number of files with each extension, `walka()` utilizes the [Counter](https://docs.python.org/3/library/collections.html#collections.Counter) class, which is in Python's [collections](https://docs.python.org/3/library/collections.html) module.

#### Creating a CLI with Clize

One final piece to this puzzle that vastly increases the usefulness of this script is creating a command line interface for it. In addition, it can be organized into a package that can be installed into a Python virtual environment.

This way, the tool can be used in any directory, regardless of where the original script is located. Without it, the script would need to be opened and updated with filepaths and such in order to tell it where to look.

I had not used Clize prior to this, and had been wanting to try it out ever since hearing about it on Python Bytes (I think). The idea is that it builds the interface based on the class or function definitions themselves, without any additional configuration.

### Conclusion

#### Future iterations

##### v0.3

Although I have not yet written this version of it, I have an idea of the features I'd like to add in the next iteration.

The most important one for me would add the ability to manually annotate images on the fly without leaving the program. In case you're not a machine learning aficionado, annotating an image means to set up labels that can be read by a computer when a model is being trained.

There are different types of annotations, but most relevant to this project are bounding boxes. The name is rather self-explanatory, but to be explicit, annotating (or labeling) an image with bounding boxes means drawing a rectangle around each instance of each class of object in each image and labeling that bounding box with the name or id of the class.

I won't go any deeper into how the model is trained on these boxes, except to say that these bounding boxes are what the trained model will end up trying to predict, given a new (previously un-seen by the model) input image.

Anyways, I wanted to keep it simple in the earlier iterations of the image skim tool, and thus moving the images that require manual annotation into a separate directory was adequate.

### Summary

Just to recap really quickly:

- One solution to the problem of manually vetting and sorting large numbers of images
- The code itself was written in Python, and available here: image_skimmer
- Third-party libraries used:
  - opencv-python
  - clize
