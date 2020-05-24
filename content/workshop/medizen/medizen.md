# MediZen

* [Intro](#intro)
  * [Stack](#stack)
  * [Summary](#summary)
  * [Data](#data)
* [Build](#build)
  * [Recommendation system](#recommendation-system)
  * [Endpoint](#endpoint)

## Intro

### Stack

> Technologies

* Python
* Pandas
  * Data cleaning and preparation
* Scikit-learn
  * K-Nearest Neighbor
  * TFIDF Vectorizer
* Flask
  * API to serve recommendations

> Topics

* Recommendation system + API
* Natural Language Processing

### Summary

MediZen is an app for cannabis patients to get strain recommendations based on their
desired effects and characteristics. The goal was to provide a platform for users to
research new strains and document their experience with each strain, such as keeping
track of dose amounts and times, as well as a list of favorites.

Myself and the other data scientists on the team were tasked with developing and
deploying the strain recommendation system. Our API would receive a set of effects,
characteristics, and descriptions chosen by the user, and return a list of strains.

The recommendation API was built using Flask, with the recommendations themselves coming
from two pickled objects: a word vectorizer that turns text inputs into vectors, and a
k-nearest neighbor model. Both of these were built and trained using Scikit-learn.

### Data

The dataset that was used to train the model and vectorizer can be found on Kaggle:
[Cannabis Strains](https://www.kaggle.com/kingburrito666/cannabis-strains).

## Build

### Recommendation system

The input that the recommendation system receives is a comma-separated list combining
the `type`, `effects`, and `flavor` options chosen by the user.

The goal of the recommendation system was to provide a list of strains with the most
similar characteristics to the input. In order to convert the input, which was text,
into something that could be understood by the model, we used one of the vectorizers
built into scikit-learn: TFIDFVectorizer.

The TF-IDF Vectorizer is trained on a corpus of text to find the unique characteristics
of the input text. [link to vectorizers blog post]

[needs rewrite]
Once the text is vectorized, a Nearest Neighbors model was trained on the corpus. This
calculates distances between data points / observations. This becomes the basis for a
recommendation system by allowing a vectorized input to be processed, the nearest
neighbors to that input returned as the most similar to the input.

[link to nearest neighbors blog post]

[look at my presentation notebook for more inspiration]

## Deployment

The recommendation API was built using Flask and deployed to Heroku. Both the vectorizer
(the "dictionary") and the nearest neighbors model were serialized in order to be used
in the Flask API.

The API took in a long string of all of the characteristics, which was run through the
serialized vectorizer to turn that string into a vector. Once in the vector, it could
easily be compared to the dataset. The nearest neighbor model returned the k-nearest
neighbors to the input vector.







