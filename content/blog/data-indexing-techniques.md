# Efficient Python Data Indexing Techniques

I remember seeing that and was interested, as indexing is something that is incredibly important to know. Also, I was a little worried about how nonchalant the `format.py` code was in simply loading the entire json file into memory as is, and loop through (potentially) the entire thing every time a new annotation is loaded.

Not efficient at all.

That's where indexes come in!

This is a little difficult to follow but I'm going to try and spell it out...and actually while I was getting some frozen berries and a tiny but more kr for this last push, I started to be able to visualize and understand what an index does and why it's beneficial.

The term "lookup" does a good job getting part way to a clear and simple explanation of what an index is doing. I say that because, with my current elementary understanding of indexing, the idea is to make each "item" into an index in a separate "table" or dataframe. That index can then be used to look up the corresponding data that "belongs" to that new index (like a row or column in a database table?).

It's difficult to explain in the abstract, and the example here is perfect for understanding the concept - or at least the basics. In this example, we are building an index to make it quicker and easier to look up images by their annotations and by their classes. So, we have three distinct sections of the data we will be traversing in order to match things up.

- images
- annotations
- classes

> The Problem

I have a large COCO annotations file, which is a solid 448mb of minified JSON. The file lays out the annotations for the 1.5 million object instances across 250k images of the MS COCO dataset. This is a perfect example to use in explaining and demonstrating indexing, as it's large enough to see the benefits, yet not so large as to make it inaccessible to anyone with a semi-decent machine at their disposal.

One solution to extracting and transforming the data contained in the file is to simply dump the file into a variable and write a few nested loops and if statements to loop through and extract the needed information. However, this can start to get unwieldy pretty quickly, as every loop could potentially be looping through the _entire_ dataset, _every time_.

Obviously that is not efficient at all, and given a slightly larger dataset—or, say, a large database with several tables of millions of records each—would prove nigh impossible.

Enter, indexing!

```py
class PanCoco:
    ...
    def create_index(self):
        # Create index between images, classes, and annotations
        print("Creating index...")
        annos, cats, imgs = {}, {}, {}
        img_to_annos, class_to_imgs = defaultdict(list), defaultdict(list)
        if "annotations" in self.dataset:
            for anno in self.dataset["annotations"]:
                img_to_annos[anno["image_id"]].append(anno)
                annos[ann["id"]] = anno
```
