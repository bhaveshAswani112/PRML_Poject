import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

def textprocessing(text):
    # Convert to lowercase
    text_lower = str(text).lower()
    
    # Remove URLs
    text_no_urls = re.sub(r"https\S+|www\S+|https\S+"," ", text_lower, flags=re.MULTILINE)
    
    # Remove non-alphanumeric characters
    text_no_nonalpha = re.sub("(\\d|\\W)+", " ", text_no_urls)
    
    # Remove '@' and '#' symbols
    text_no_symbols = re.sub(r'\@\w+|\#', " ", text_no_nonalpha)
    
    # Tokenization
    text_tokens = word_tokenize(text_no_symbols)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english')) - {'not','no' , 'never'}
    text_no_stopwords = [word for word in text_tokens if word not in stop_words]
    
    # Lemmatization
    # lem = WordNetLemmatizer()
    # text_lemmatized = [lem.lemmatize(word) for word in text_no_stopwords]
    stemer = SnowballStemmer()
    text_stemmed = [stemer.stem(word) for word in text_no_stopwords]
    
    # Join tokens back into a string
    # text_processed = " ".join(text_lemmatized)
    text_processed = " ".join(text_stemmed)
    
    return text_processed
