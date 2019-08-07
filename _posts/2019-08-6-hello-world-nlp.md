---
title: 'Sentiment analysis: a roadtrip through the "Hello World" of NLP'
layout: single
toc: true
header: 
   image: /assets/images/header.jpg 
---


> Sharing what I learned from building a simple app to predict sentiment

# Why predicting sentiment
> TODO


# It all started with a sentiment analysis web UI 


A short time ago I decided to create a Flask application to do sentiment analysis on the fly and published it in a [github repo](https://github.com/robinicole/sentiment_analysis_app). It is divided in two parts: 

1. **The frontend:** A flask application that asks the user to write a sentence and will display the sentiment of the sentence predicted by the backend part of the code in real-time.

2. **The backend:** A RNN written with PyTorch which takes the string written by the user as an input, preprocess it,  feed it into the neural network and return a sentiment for the sentence

# How to try it ? 

If you want to try this app on your computer, you should first clone my git repository on your computer: 
```bash
git clone git@github.com:robinicole/sentiment_analysis_app.git
cd sentiment_analysis_app
```
Then, you can launch the app by using either *Docker* or install the app in a virtual environment

## Using a virtual environment

First, create a virtual environment and activate it. If you use a Conda environment, those commands should do the job, otherwise, you will have to adapt them slightly to the tool you use to manage virtual environments. 
```bash
conda create --name 'sentiment_app' python=3.6
conda activate sentiment_app
```

Once a new virtualenv is activated, it is always a good idea to check that the `pip` you will use to install packages is the one inside your environment and not the main one. You can do that with `which pip` which should return something like `SOME_PREFIX_PATH/sentiment_app/bin/pip`. In my case, I have 

```bash
which pip 
>>> /home/robinnicole/anaconda3/envs/sentiment_app/bin/pip
```


Then install the packages and run the app: 

```
pip install -r requirements.txt
python app.py
```


## Using docker 

Those commands assume that you have docker installed and running on your machine. If this is not the case, you can find many tutorials to install Docker on the internet. 

Once you are sure that you have Docker installed on your machine, all the command to build and run the Docker machine are inside a Makefile and you only have to run 

```bash 
make build_docker
make run_docker
```

to get your app running

## Once this is done? 


Once this is done, open <http://localhost:5000> in your browser, type your favorite sentence and check which sentiment the app predicts for it. 


# What Could be improved

Although I am happy with this app, there is still room for improvement, especially for the backend part. Here is a non-exhaustive list of all the things that could be improved: 


1. At the moment I use a simple RNN, what about adding more features in my model like attention, embedding with word2vec.

2. What about proposing to the user to choose which model he wants to use to predict the sentiment of his sentence. 

3. Should we train each of the models on different datasets, not only the IMDB dataset? To do that, it would be convenient to have a standardized interface to a dataset (`torchtext` might provide a solution for that)

4. It would be cool to understand the reason why a model predicts a sentiment. At the moment I use Lime which is a model agnostic feature explanation package but in the future, I could certainly use the attention layers to extract useful information about my model choice. 


# Where to learn the missing bits 


Before dealing with those three problems it would be a good idea to look a bit more at what's done on NLP at the moment. There is [paper with code](https://paperswithcode.com/) which is a great resource for advanced NLP task but let's not "put the cart before the horses". The first step is to ensure that the code is properly structured so we can integrate new models seamlessly. One good resource for that is [this git repo](https://github.com/bentrevett/pytorch-sentiment-analysis) which provide good code design tips and basic NLP model for sentiment analysis: they build a more and more efficient sentiment analysis model step by step and, along the way, show you a lot of tricks in for NLP. 


One thing, I found very interesting is that they use the `torchtext` package ([tutorial here](https://mlexplained.com/2018/02/08/a-comprehensive-tutorial-to-torchtext/)) to automate all their data processing which make their project very clean and well structured. I will have a look at it as it is likely to be simpler and faster than the custom data processing pipelines I implemented in my app. Ultimately I believe this will provide a good basis to write easily maintainable code and also provide a zoo of models to test to interface with my web UI. 


# Conclusion


The web-ui project mentioned in the first section is, in my opinion, the `hello world` of NLP but and it has the merit of taking you through all the common pitfalls of developing an NLP model one by one. This article is fare away from being complete and will be updated as the project progresses.


# Sources

- [1] The sentiment app Github repository  <https://github.com/robinicole/sentiment_analysis_app>

- [2] Tutorial to install Docker <https://runnable.com/docker/install-docker-on-linux>

- [3] Papers with code <https://paperswithcode.com/>

- [4] Tutorial on sentiment analysis with PyTorch <https://github.com/bentrevett/pytorch-sentiment-analysis>

- [5] Tutorial on the `torchtext` package <https://mlexplained.com/2018/02/08/a-comprehensive-tutorial-to-torchtext/>
