import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

def textprocessing(text):
    text = str(text).lower()
    
    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    
    # Remove square brackets and their contents
    text = re.sub(r'\[.*?\]', '', text)
    
    # Replace non-word characters with a space
    text = re.sub(r'\W', ' ', text)
    
    # Remove XML tags
    text = re.sub(r'<.*?>+', '', text)
    
    # Remove punctuation
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    
    # Remove newline characters
    text = re.sub(r'\n', '', text)
    
    # Remove alphanumeric characters
    text = re.sub(r'\w*\d\w*', '', text)


    # Remove '@' and '#' symbols
    text = re.sub(r'\@\w+|\#', " ", text)

    
    # Tokenization
    text_tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english')) - {'not','no' , 'never'}
    text_no_stopwords = [word for word in text_tokens if word not in stop_words]
    
    # Lemmatization
    lem = SnowballStemmer('english')
    text_lemmatized = [lem.stem(word) for word in text_no_stopwords]
    text_processed = " ".join(text_lemmatized)
    
    return text_processed


