
from nltk.corpus import stopwords
import re


def clean_sentence(sentence : str):
    '''
    '''
    sentence = re.sub(r"\[![0-9]&)-^$#+*\]", " ", sentence) 
    sentence = re.sub(r"\s+", " ", sentence)     
    stop_words = set(stopwords.words("english"))
    get_words = sentence.lower().split()
    cleaned_sentence = list(set([word for word in get_words if word not in stop_words]))
    cleaned_sentence = [" ".join(cleaned_sentence[::])]

    return cleaned_sentence

def get_clean_dataframe(dataframe, sentence : str):
    '''
    '''
    cleaned_sentence = []
    for index in range(len(dataframe[sentence])):
        uncleaned_text = dataframe[sentence][index]
        cleaned_text = clean_sentence(uncleaned_text)
        cleaned_sentence.append(cleaned_text[0])
    dataframe['cleaned_sentence'] = cleaned_sentence

    return dataframe