#Text cleaning
import re, string
import demoji
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))


class CleanTweet():
    def __init__(self, raw_text) -> None:
        self.raw_text = raw_text

    # remove emojis from text
    def strip_emoji(self, text):
        return demoji.replace(text, '') #remove emoji

    # remove punctuations, links, stopwords, mentions and \r\n new line characters
    def strip_all_entities(self, text): 
        text = text.replace('\r', '').replace('\n', ' ').lower()
        text = re.sub(r"(?:\@|https?\://)\S+", "", text) # delete links and mentions
        text = re.sub(r'[^\x00-\x7f]',r'', text) # delete non utf8/ascii characters 
        banned_list= string.punctuation
        table = str.maketrans('', '', banned_list)
        text = text.translate(table)
        text = [word for word in text.split() if word not in stop_words]
        text = ' '.join(text)
        text =' '.join(word for word in text.split() if len(word) < 14) # remove words longer than 14 characters
        return text

    # remove contractions
    def decontract(self, text):
        text = re.sub(r"can\'t", "can not", text)
        text = re.sub(r"n\'t", " not", text)
        text = re.sub(r"\'re", " are", text)
        text = re.sub(r"\'s", " is", text)
        text = re.sub(r"\'d", " would", text)
        text = re.sub(r"\'ll", " will", text)
        text = re.sub(r"\'t", " not", text)
        text = re.sub(r"\'ve", " have", text)
        text = re.sub(r"\'m", " am", text)
        return text

    # remove hashtags at the end of the sentence, and keep those in the middle of the sentence by removing just the "#" symbol
    def clean_hashtags(self, tweet):
        new_tweet = " ".join(word.strip() for word in re.split('#(?!(?:hashtag)\b)[\w-]+(?=(?:\s+#[\w-]+)*\s*$)', tweet)) # remove last hashtags
        new_tweet2 = " ".join(word.strip() for word in re.split('#|_', new_tweet)) # remove hashtags symbol from words in the middle of the sentence
        return new_tweet2

    # filter special characters
    def filter_chars(self, a):
        sent = []
        for word in a.split(' '):
            if ('$' in word) | ('&' in word):
                sent.append('')
            else:
                sent.append(word)
        return ' '.join(sent)

    # remove multiple sequential spaces
    def remove_mult_spaces(self, text):
        return re.sub("\s\s+" , " ", text)

    # stemming
    def stemmer(self, text):
        tokenized = nltk.word_tokenize(text)
        ps = PorterStemmer()
        return ' '.join([ps.stem(words) for words in tokenized])

    # # lemmatization 
    # #NOTE:Stemming seems to work better for this dataset
    # def lemmatize(self, text):
    #     tokenized = nltk.word_tokenize(text)
    #     lm = WordNetLemmatizer()
    #     return ' '.join([lm.lemmatize(words) for words in tokenized])
    
    # Then we apply all the defined functions in the following order
    def deep_clean(self):
        text = self.strip_emoji(self.raw_text)
        text = self.decontract(text)
        text = self.strip_all_entities(text)
        text = self.clean_hashtags(text)
        text = self.filter_chars(text)
        text = self.remove_mult_spaces(text)
        text = self.stemmer(text)
        return text