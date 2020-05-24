"""
:: SubWise :: Subreddit Recommendation API ::

A simple back-end Flask API for recommending
the best subreddits to post your masterpieces.
"""

import os
import pickle
import json
import pandas as pd

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# === Load in the pickled pre-trainees === #
# LabelEncoder
with open("assets/06_le.pkl", "rb") as p:
    le = pickle.load(p)

# chi2 selector
with open("assets/06_selector.pkl", "rb") as p:
    selector = pickle.load(p)

# Vectorizer
with open("assets/06_vocab.pkl", "rb") as p:
    vocab = pickle.load(p)

# Naive Bayes model
with open("assets/06_nb.pkl", "rb") as p:
    nb = pickle.load(p)


def predict(title: str, submission_text: str, return_count: int = 5):
    """
    Create subreddit predictions.

    Parameters
    ----------
    post : string
        Selftext that needs a home.
    n    : integer
        The desired name of the output file,
        not including the '.pkl' extension.

    Returns
    -------
    Python dictionary formatted as follows:
        [{'subreddit': 'PLC', 'proba': 0.014454},
        {'subreddit': 'Rowing', 'proba': 0.005206}]
    """
    # Concatenate title and post text
    fulltext = str(title) + str(submission_text)

    # Vectorize the post -> sparse doc-term matrix
    post_sparse = vocab.transform([fulltext])

    # Feature selection
    post_select = selector.transform(post_sparse)

    # Generate predicted probabilities from trained model
    proba = nb.predict_proba(post_select)

    # Wrangle into correct format
    proba_dict = (
        pd.DataFrame(proba, columns=[le.classes_])  # Classes as column names
        .T.reset_index()  # Transpose so column names become index
        .rename(columns={"level_0": "name", 0: "proba"})  # Rename for aesthetics
        .sort_values(by="proba", ascending=False)  # Sort by probability
        .iloc[:return_count]  # n-top predictions to serve
        .to_dict(orient="records")
    )

    proba_json = {"predictions": proba_dict}

    return proba_json


@app.route("/", methods=["POST", "GET"])
def rec():
    """
    Primary recommendation route.

    Parameters
    ----------
    post : string
        Content of post.
    n : int, optional
        Number of recommendations to return, by default 5.
    Returns
    -------
    top : JSON
        Returns a JSON array of top n recommendations and their
        relative probabilities.
    """
    if request.method == "POST":
        req_data = request.json

        submission_text = req_data["submission_text"]
        title = req_data["title"]
        return_count = req_data["return_count"]

        top = predict(title, submission_text, return_count)

        return top
    else:
        return "Get!"


if __name__ == "__main__":
    app.run()
