print(fiction)

> A predictive modeling project

* [Introduction](#introduction)
  * [Stack](#stack)
  * [Overview](#overview)

* Intro
  * Stack
  * Overview
* Process
  * Gathering data
  * Modeling
  * Deployment
* Conclusion

## Introduction

> [print(fiction)](http://print-fiction.herokuapp.com/)

### Stack

> Technologies

* Python
* Pandas
* Scrapy
* Scikit-learn
* Random forest
* XGBoost
* Plotly Dash

> Topics

* Web scraping
* Predictive modeling
* Feature engineering
* Decision trees
* Random Forest
* Gradient-boosting

> Potential related blog posts

* Scrape book dataset from GoodReads using Scrapy
* Data cleaning and preparation using Pandas
* Train a random forest model using scikit-learn
* Train gradient-boosted ensemble models with XGBoost
* Deploy a predictive model using Plotly Dash
* The bias-variance tradeoff

## TLDR

print(fiction) is a solo project I worked on to explore the data on and around
fictional stories.

I used Scrapy to scrape metadata for over 20,000 books from GoodReads and used it to
train a gradient-boosted random forest classifier. The final version of the model
classified books as either fiction or nonfiction with 88% accuracy.

The dataset is available below:

There is a web app front end that combines an article and a dashboard that can be used to
play around with the model parameters. I built the front end with Plotly Dash and
deployed it to Heroku.

[LinkBlock]

## Intro

This project is part of an on-going series of exploratory articles and projects called
Sci-Fi IRL through which I am exploring the relationship between science-fiction and the
real world. It is my belief that the stories we read, write, and believe in,
particularly about our future, have an effect on how that future ultimately turns out.

Our human minds are geared toward thinking about what could go wrong. It follows that
the majority of stories in popular and niche culture are written about things going
wrong.

In the case of science-fiction, the vast majority of stories written and consumed are
dystopian in nature, showing what could go wrong if our technology advances down certain
avenues. Both from the creator's and consumer's perspectives, it "tells a good story" to
imagine what could go wrong.

But does this affect our outlook on what these technologies can do for us?

While it is always good to consider the possible ramifications of technological
advances, I believe that too many dystopian stories are causing us to fall short of our
potential. If instead of dystopian the majority of science-fiction was utopian in
nature, exploring the possible ways that things could go _right_ for us—the ways that
technology can lead to an overall better society—it would, in a very real sense, point
us a little bit more in that direction.

If that's a bit too lofty for you, another way to think about this is to imagine what
your life could be like 100 years from now (i.e. if you'd been born 60 years from now).
Depending on how things go, you could be poisoned with radiation, recovering from
nuclear holocaust. Or, you could be out exploring the stars with a lifespan in the
centuries.

This is the area I'm exploring with this series. I want to find the data and conduct the
analyses that begins to show us how our collective narrative (aliased by popular
science-fiction) can bring about changes in our technological progress.

[How after I came to the target, everything else fell into place]

### Data

I knew before starting the project that I wanted to do something with books. I also knew
that I wanted to gather my own dataset by scraping some sort of data from the web.

After some failed attempts at coming up with something interesting, such as predicting
the average rating, I found the following question to explore: given all the metadata
about a book, is it possible to predict if it is fiction or non-fiction?

The metadata I gathered from GoodReads included:

* num_reviews: number of text reviews
* avg_rating : average rating (1 - 5 stars)
* num_pages  : number of pages in book
* publish_year: year the book was published
* in_series  : book is part of series

At first glance, this question seems relatively straightforward to answer. However,
there don't seem to be all that many distinguishing differences on the surface. To get a
useful and interesting model, some feature engineering work had to be done.

## The Dataset

### Scraping

As mentioned above, the dataset of metadata for around 20,000 books was scraped from
GoodReads. I did not build the scraper from scratch, as I didn't have to. The scraper
itself wasn't an important part of this particular project and so I didn't want to spend
too much time building it.

Luckily for me, I ran across a small project on GitHub that was built for just this
purpose: [havanagrawal/GoodreadsScraper](https://github.com/havanagrawal/GoodreadsScraper).

I made some minor modifications to the code to fix some small bugs and make it fit my
use-case. But it was definitely a time-saver to find this project.

### Cleaning

There were outliers in some of the dimensions which could be easily removed. For
example, there were several books with over 5,000 pages when the majority had less than
500.

[Pages plot]

Also, as can be expected with media such as books, there are some large outliers with
regards to popularity. The vast majority of books had relatively few ratings and even
fewer reviews. However, there were some that got up in the millions of ratings and
hundreds of thousands of reviews.

[Reviews + ratings plot]

### Feature Engineering

As can be gleaned from the plots below, without any feature engineering the data does not
seem to separate out along any clear axes.

[Insert scatter plot matrix here]

Of course things may be different in higher dimensions. But I figured it wouldn't hurt
to look for opportunities to engineer some new useful features.

Here are the ones I engineered:

* Title begins with "the"
* Has subtitle: contains ":"
* Title character length
* Title word length
* Title longest word length
* Author number of names
* Author uses middle initial
* Ratio between 1 - 5 stars

Out of those new features, all but two had a positive permutation importance and were
thus used in the training of the model.

### Exploratory Data Analysis

[More plots and such here]

## The Model

[Maybe don't talk about switching targets?]

Before I came to the idea of using fiction / nonfiction as my target for this project,
I'd been playing around with predicting the average rating for the book.

At first things were looking good, as even with a simple linear regression I was
getting fairly high R^2 score. It was when I ran a gradient-boosted regression that I
began to get really suspicious of the results, as my R^2 was above 0.95.

That score led me to believe that there was some leakage between the target and the
features. 

In hindsight it was obvious which features were leaky, but the process of uncovering it
led me back down the path of thinking I could do better; I could set the problem up in a
way that was more interesting.



The purpose of creating the dataset was to build a predictive model that would hopefully
help answer an interesting question. Throughout the course of the project, I trained a
series of random forest classifiers with Scikit-learn, ultimately getting the best
performance from a gradient-boosted random forest, built and trained using XGBoost. 

































