Code Structure:

The model training and evaluation takes place in the Jupyter Notebooks for better development flow. 


The Scripts sub directory contains the Python scripts used for building the dataset. We attempted to extract all the relevant tweets from the beginning of the 2010 NBA season up to this year’s All Star weekend. It also includes the cleaning pre-processing for all the retrieved tweets. 


The Processed and Raw sub directories contain the datasets of ‘raw’ and ‘cleaned’ data. Here, the resulting cleaned data csv is the one used in the models.


The Models sub directory contains each model used. The Naive Bayes and SVM models are used as baselines, for comparison. The BERT and Bi-Directional LSTM models were the main target models, since they are by nature more complex and expected to have a better performance. We hoped for these models to give an increased accuracy compared to the baselines. The word2vec model is used to tokenise the data in the Bi-Directional LSTM. BERT uses the original HuggingFace tokeniser as our dataset was too small to fine tune it. 


How to run:
- run get_tweets.py to build raw tweets dataset;
- run data_preprocessing.py to build a processed dataset with cleaned text;
- the different Jupyter Notebooks contain the respective code for tokenising the data, training the model, and evaluating its performance;
- the demo notebook contains the code for classifying an input text using our trained BERT model, since it was our best performing one;


Links:
Raw data - https://drive.google.com/file/d/16BlnKMj3RSHFqT2zNw3xIhFDDkDlKMQw/view?usp=sharing
Processed/cleaned data - https://drive.google.com/file/d/1hRypGd3OwcgLPsPLJ4IqDNwaEWtvFXVm/view?usp=sharing

BERT model - https://drive.google.com/file/d/1RUe37Ph2uUk3WIkQcFKPT3wFKDfHrrTw/view?usp=share_link
LSTM model - https://drive.google.com/file/d/1ZRi_KF1yhmxF7HX9iFiPKsrEDjrNrRE3/view?usp=share_link
Naive Bayes model - https://drive.google.com/file/d/1lvJeS0iTL3TLorO8zniHo0wkBjN305fQ/view?usp=share_link
SVM model - https://drive.google.com/file/d/1NEqIEoqIAQAsC-9Xqo1mcmFXQt999ann/view?usp=share_link
Word2vec model - https://drive.google.com/file/d/1paI5QcTXtC8qBes4QnYmzPqPjbpw4Prx/view?usp=sharing



Attribution to sources:
BERT using PyTorch tutorial - https://neptune.ai/blog/how-to-code-bert-using-pytorch-tutorial
Building a Multiclass Classification model - https://machinelearningmastery.com/building-a-multiclass-classification-model-in-pytorch/
PyTorch Multiclass Classification - https://towardsdatascience.com/pytorch-tabular-multiclass-classification-9f8211a123ab
Twitter Sentiment Analysis with LSTM - https://towardsdatascience.com/using-lstm-in-twitter-sentiment-analysis-a5d9013b523b
Multi-label text classification with BERT - https://kyawkhaung.medium.com/multi-label-text-classification-with-bert-using-pytorch-47011a7313b9

The dataset was created from scratch using the Twitter API. 

