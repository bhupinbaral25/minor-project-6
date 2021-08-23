import re

import nltk
from nltk.corpus import stopwords


def clean_sentence(sentence):

    sentence = re.sub(r"\[![0-9]&)-^$#+*\]", " ", sentence)     
    get_words = sentence.lower().split()
    stop_words= set(stopwords.words("english"))
    cleaned_sentence = list(set([word for word in get_words if word not in stop_words]))
    cleaned_sentence = [" ".join(cleaned_sentence[::])]

    return cleaned_sentence

def clean_data(dataframe, sentence):

    """
        
    """
    cleaned_text = []
    for index in range(len(dataframe[sentence])):
        uncleaned_text = dataframe[sentence][index]
        cleaned_words = clean_sentence(uncleaned_text)
        cleaned_text.append(cleaned_words[0])
    dataframe['cleaned_title'] = cleaned_text

    return dataframe