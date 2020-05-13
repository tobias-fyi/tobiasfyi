Title: Technical Terminology Velocity
Subtitle: Sci-Fi IRL, Part 1
Date: 2019-09-27
Modified: 2019-09-27
Category: Sci-Fi IRL
Tags: Python, Data, Media
Slug: technical-terminology-velocity
Author: Tobias Reaper
Cover: images/keyboard.jpg
Thumbnail: images/keyboard.jpg
Summary: A brief analysis of the velocities of technical terminology across different online communities.

## Sci-fi, IRL

This essay is the first in a series of data-driven essays, Sci-fi IRL, that will explore the relationship between science-fiction and IRL (in real life) science, technology, and philosophy.

## Introduction

I love reading and writing science-fiction for many reasons. At the top of that list is how the format of the genre can open doors to the exploration of important concepts and technology in ways that, in my view, no other genre of storytelling, fictional or not, can.

Of particular interest to me is the opportunity sci-fi presents for preemptively exploring near-to-mid-future ideas that have the potential to drastically affect our existence in the "real" world (I won't get into the weeds with that term right now—I hope you know what I mean).

One great example of this that immediately comes to mind is traveling through and living in outer space. (You thought I was going to say artificial intelligence, weren't you?)

Of course there are many stories set in space that do not pay much attention to the minute or day-to-day details of life in zero-gravity. However, as a powerful literary or plot device that can give a story depth and realism, it is usually addressed at some level. Although vast majority of the sci-fi I consume nowadays comes in the form of books, the most vivid portrayal of life in the void also happens to be one of my favorite book and television series, The Expanse.

The reason for it being high up on my list is not solely due to this portrayal or the fact that I enjoy hard sci-fi when it's done well. To go back to what I stated earlier, these stories give me new perspectives on novel concepts.

Stories like The Expanse allow us to explore the possible ramifications of potentially civilization-changing things *now*, before we're on our way past the stratosphere, en masse.

The Sci-Fi IRL series is my first attempt at connecting the various science-fiction universes with our own.

## Part 1: Goals

The goal of this particular piece is to make the smallest baby step possible toward the overarching goal of the project, which is to answer the question, "What is the relationship, if any, between the ideas and technology in science-fiction and those of the real world?"

In order to take this first small step for mankind, I will be using data to illustrate one potential point of relation between the science of fiction and the non—the terminology of technology.

My hypothesis is that there is a distinct, and to some degree regular, time lag between when the terminology describing some important new technology is introduced into popular discourse and when it begins to show up in popular culture. I'm using the term "popular culture" to refer to the overall, ever-changing corpus of (science-fiction) books, series, and video games.

I decided to call the measure of this relationship *Technical Terminology Velocity*.

## Next Steps

The next step after (hopefully) establishing the velocity of intellectual interchange from the real world to popular culture will be to test the hypothesis that a similar, complementary relationship exists going the other direction.

One way to phrase that line of inquiry as a question could be, "When popular culture introduces some new terminology, how long does it take to spread into the fields of science, technology, and philosophy?

However, I don't want to get ahead of myself. I'll save the latter half for next time.

## Methodology

### A Bit of Backstory

While considering how to go about testing this hypothesis, I ran across the somewhat-infamous [Reddit Dataset](https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/), which supposedly held every single publicly-available Reddit comment, totaling almost 2 billion.

As an on-and-off Redditor over the past decade or so, I immediately recognized the huge potential provided by this type of data source.

However, I held back at first because I did not necessarily want (let alone was even able) to download many hundreds of gigabytes of data. In reality, I would only be using a miniscule fraction of that in my analysis, at least at this early stage in my data science career—once I get into more advanced topics like machine learning, who knows?—if I could even figure out how to parse something that incredibly large.

I felt optimistic; up to the task. I stumbled on the [PushShift file directory](https://files.pushshift.io/reddit/), which is an actively-updated archive of that same data. Once I realized I could download the data month-by-month, I decided to go for it.

I spent a week or two downloading from the PushShift server, raking in around 200GB of data during that time. Several days ago, I happened to be poking around on the PushShift site and found out that along with providing all of the data for download, the maintainer, [Jason](https://pushshift.io/donations/), built and hosts [a public API](https://github.com/pushshift/api) for [querying the entire dataset](https://pushshift.io/api-parameters/) *without downloading all of it to my local storage*.

That benefitted me in a couple of very important ways. First, I no longer had to fill up the majority of my total digital storage capacity (quite literally—all of my externals and everything). Second, the data is already cleaned and organized, with infrastructure already in place to run the kinds of queries that I wanted to run for this essay.  

I want to give a huge shoutout to Jason (AKA [u/Stuck_in_the_Matrix](https://www.reddit.com/u/Stuck_In_the_Matrix/)) for providing such a valuable service, and allowing free and open access.

### For Key in Words

To start, I spent some time coming up with a list of words and phrases that I could use to test my hypothesis. In order to find anything interesting, it was *very* important to come up with effective criteria that was aligned with the goals of this research.

The fundamental criteria I used while creating the list were that the word or phrase should:

1. Be, or have been at some point in the last decade, popular enough to be considered a "normal" part of popular lexicon;
2. Describe a distinct technology, field, and/or ideology; and
3. Not be so specific as to prevent it from being explored in non-technical media.

#### Keywords

- Algorithm
- AI
- AR
- Big data
- Automation

### Equal Representation

Once I had my first basic list of around 10 terms (for the first run-through I ended up using 9 of them), the next step was to find or create a method of representing the groups I want to test. Of course, since I am using Reddit data, the obvious thing to do is find subreddits that fit into those groups.

With that in mind, I spent a while combing through the massive list of subreddits, adding to my list, grouping and re-grouping, pruning from the list...you get the point. The result was the following list:

#### Subreddits

- Science / Technology
  - r/Futurology, 14.2m
  - r/technology, 8.2m
  - r/science, 22.4m
  - r/askscience, 18.1m
  - r/gadgets, 15.9m
- Entertainment
  - r/books, 17.1m
  - r/scifi, 1.2m
  - r/movies, 21.5m
  - r/gaming, 23.7m
  - r/television, 15.7m
- Public Discourse
  - r/news, 19m
  - r/worldnews, 22.2m
  - r/politics, 5.4m
  - r/philosophy, 14.1m
- General Discussion
  - r/AskReddit, 24.6m
  - r/todayilearned, 21.6m
  - r/explainlikeimfive, 17.2m

##### Notes

1. I included the "General" groups as a sort of control group analogue. I thought it would be good to also look at the trend of general discussion alongside the more specific discussions in the other groups. However, it may be the case that these types of communities are a better indicator of the terminology being used in popular culture than the entertainment communities.
2. I used the above list to cast a somewhat wide net while gathering the initial data. The hope was that the wider the net, the greater the chance of finding something interesting.

### The Data is in the Details

Using Python, I wrote some clever loops (at least I thought so) that went through the lists of keywords and subreddits, constructing the URL for each combination and sending it off to the API. For each keyword-subreddit combination, the parameters I included in my request told the API to aggregate the number of comments containing the keywords into monthly buckets.

The function I wrote to do this saved the data to both a Pandas DataFrame, for immediate use in my JupyterLab environment, and to a CSV file, for future use. The raw data is [available in CSV form on GitHub](https://github.com/tobias-fyi/tobias-fyi/tree/master/data/001-sci_fi_irl), in case you want to take a look for yourself or use it to do your own analysis.

I'll be publishing a separate article that gets into the nitty gritty of the code I wrote to gather and visualize the data. If you're reading this paragraph, that "tutorial" piece has not been published yet. I will link to it from here when it goes live.

As this is only the very first piece in a series and I am still a fledgeling data scientist, none of the code or analysis is particularly complex. However, I want to get into the habit of explaining every step of my process well enough for anyone to understand, data scientist or not.

We all start somewhere.

### Some Considerations

In order to tell the story I want to tell with the time I had to do so and my currently limited knowledge of advanced methods, I had to make some strong assumptions and overlook some obvious shortfalls.

One important consideration for this data is the fact that these are comments posted to online internet forums. My assumption is that comments do a much better job representing popular discourse than the actual content of the books and shows.

An important shortfall in my data and subsequent analysis that is worth mentioning is the uncountable confounding variables that skew the data one way or another. At this point I do not have the skills or knowledge to adequately deal with such things.

Like I said, we all start somewhere. I'm doing my best to not let perfect be the enemy of good.

With all of that out of the way, let's get into it!

## The Velocity of Technology Terminology

Unfortunately, the data I was able to collect and analyze was not particularly conclusive. Although I did not conduct any formal statistical analysis to determine if I could safely reject my hypothesis, the visualizations seem to indicate that this is the case.

While I did not find any conclusive evidence that there is a time-lag, I did create a lot of graphs, some of which have some interesting features. The parts that I found interesting are for the most part not related to my hypothesis, but I will bring that up when it does happen to be relevant.

To start us out on this visual exploration, I'll go through each keyword starting with "algorithm", showing the data on that keyword for a number of subreddits and pointing out aspects the visualizations that I find interesting.

### Term Velocity: Algorithm

!["Algorithm" in r/technology]({static}/images/algorithm-technology.png)

!["Algorithm" in r/scifi]({static}/images/algorithm-scifi.png)

The relationship between the frequency of comments that mention "algorithm" in r/technology and r/scifi is one of the stronger examples that seems indicate that my hypothesis may have some inkling of truth. That outlier at the beginning of r/scifi's data was likely cause by someone mentioning "algorithm" while there was very few total comments in the subreddit, causing the percentage to be high.

This is why I stated that the results are inconclusive—picking out a significant relationship with simple numerical analysis and simple plots seems to be a huge stretch in this case.

However, I do find the below graph of r/philosophy to be interesting. First of all, the percentage of comments mentioning the term "algorithm" is for the most part even higher than that of r/technology. Thinking about algorithms from a philosophical standpoint can be rather interesting, particularly in the last decade as algorithms have automated a huge part of many people's lives. There are good and bad aspects of that, which seem to be sparking a good amount of (hopefully) intelligent discussion over at r/philosophy.

!["Algorithm" in r/philosophy]({static}/images/algorithm-philosophy.png)

### Term Velocity: AI

r/philosophy is also showing up strong for "AI". And as I'd expect, the discussions look to have been heating up over the last few years as the general public becomes more knowledgable about the ways that big tech is using AI to their advantage, sometimes with questionabble ethics.

!["AI" in r/philosophy]({static}/images/ai-philosophy.png)

I find the following three plots (r/movies, r/scifi, and r/science, respectively) interesting mostly because they all show large spikes in the number of comments that mention "AI" around the same time. This indicates that there was a popular science-fiction film that had some aspect of science that people were curious about or that was controversial.

!["AI" in r/movies]({static}/images/ai-movies.png)

!["AI" in r/scifi]({static}/images/ai-scifi.png)

!["AI" in r/science]({static}/images/ai-science.png)

I did a quick search for science-fiction films released in 2015 and found a few candidates that resulting in the increased number of comments: The Martian, Terminator Genisys, Avengers: Age of Ultron, Star Wars VII: The Force Awakens...there was actually a ton of science-fiction released that year. I'll leave it up to you to decided which one(s) it was.

!["AI" in r/politics]({static}/images/ai-politics.png)

The last "AI" example I'll look at is r/politics. The reason I find this interesting is simply how few comments were made in the subreddit that mention "AI", considering how much it has become a part of public discourse lately.

### Term Velocity: Automation

The number of comments that mention "automation" in r/politics shot up around the end of 2013 into the beginning of 2014, which coincides with a similar spike in r/worldnews (and even a smaller spike in r/scifi). What I find it interesting and a little bit funny is that r/politics mentions the term less and less, except for a spike at the end of 2016.

That spike is also visible in r/worldnews and (somewhat interestingly) r/scifi. My guess is that spike coincides with the last presidential election, when automation was brought forth into public discourse as a part of many candidates' platforms.

!["Automation" in r/worldnews]({static}/images/automation-worldnews.png)

!["Automation" in r/politics]({static}/images/automation-politics.png)

!["Automation" in r/scifi]({static}/images/automation-scifi.png)

## Conclusion

As I stated above, the visualizations of the data do not seem to indicate any sort of time-based relationship in the velocity of technical terminology between different subreddits. There are individual examples where one could make an argument for my hypothesis, but it would be a stretch to say the evidence is significant.

However, it is interesting to look at how different online communities have used different terms over time and the tools I built for myself to gather and display this data were a blast to work on. For that reason (and because I believe there are real, interesting relationships somewhere along this line of inquiry), I may decide to refine my data gathering and analysis process with this data set in order to uncover other relationships.
