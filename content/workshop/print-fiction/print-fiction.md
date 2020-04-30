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

> Potential related blog posts

* Scrape book dataset from GoodReads using Scrapy
* Data cleaning and preparation using Pandas
* Train a random forest model using scikit-learn
* Train gradient-boosted ensemble models with XGBoost
* Deploy a predictive model using Plotly Dash
* The bias-variance tradeoff

### Overview

print(fiction) is a project I built with Plotly Dash and deployed to Heroku. I used
Scrapy to scrape the metadata for over 20,000 books from GoodReads, Pandas to manage and
clean it up, then scikit-learn and XGBoost to train a predictive model with it.

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

## The Model

Before I came to the idea of using fiction / nonfiction as my target for this project,
I'd been playing around with predicting the average rating for the book.

At first things were looking good, as even with a simple linear regression I was
getting fairly high R^2 score. It was when I ran a gradient-boosted regression that I
began to get really suspicious of the results, as my R^2 was above 0.95.

That score led me to believe that there was some leakage between the target and the
features. 


































