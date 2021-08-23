
from nltk.corpus import stopwords
import nltk
import re


def clean_sentences(sentence : str):
    '''
    get raw senteces as  input 
    ------------------------------------
    remove stop words and make lowe case 
    ------------------------------------
    Return Clean Sentences 
    '''
    sentence = re.sub(r'[0-9]', ' ', sentence)    
    stop_words = set(stopwords.words("english"))
    get_words = sentence.lower().split()
    cleaned_sentence = list(set([word for word in get_words if word not in stop_words]))
    cleaned_sentence = [" ".join(cleaned_sentence[::-1])]

    return cleaned_sentence

def get_clean_dataframe(dataframe, sentence : str):
    '''
    get dataframe with raw sentences as input 
    -------------------------------------------------
    remove stop words and make lowe case 
    -------------------------------------------------
    Return Clean Sentences in new column in dataframe
    '''
    cleaned_sentence = []
    for index in range(len(dataframe[sentence])):
        uncleaned_text = dataframe[sentence][index]
        cleaned_text = clean_sentences(uncleaned_text)
        cleaned_sentence.append(cleaned_text[0])
    dataframe['cleaned_sentence'] = cleaned_sentence

    return dataframe