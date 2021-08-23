import numpy as np
import pandas as pd
from sentence_transformers import  util, SentenceTransformer

def read_data(path):
    '''
    csv file path in string
    --------------------------------
    Read CSV file
    --------------------------------
    return dataframe
    '''
    return pd.read_csv(path)

def get_sentence_embeddings(model, sentence : list ) :
    
    '''
    model = trained machine learning/ deep learning model
    -----------------------------------------------------
    convert sentence into embeddings
    -----------------------------------------------------
    return embeddings of given sentence
    '''

    return model.encode(sentence)

def get_similarity_score(model, dataframe, sentance_1 : str, sentence_2 : str):

    '''
    machine learning/ deep learning model
    --------------------------------------------------------------
    generate embeddings by using  ml model and calculate 
    similarity score of sentences to dataframe for that model
    --------------------------------------------------------------
    return Similarity Score of sentence in array
    '''

    similarity_score = []
    model = SentenceTransformer(model)
    querry_embedding = get_sentence_embeddings(model, sentance_1)
    sentence_embedding = get_sentence_embeddings(model, list(dataframe[sentence_2]))
    for  index in range(len(dataframe[sentence_2])):
        similarity_score.append(np.array(util.pytorch_cos_sim(querry_embedding, sentence_embedding[index])))                           
          
    return np.array(similarity_score).flatten()

def get_high_similarity_score_index(similarity_score):
    '''
    take similarity_score as numpy array
    --------------------------------------------------------------
    sort the array and and calcuate their corresponding index
    --------------------------------------------------------------
    return highest 4 score index 
    '''
    indices = np.argsort(similarity_score)[::-1]
    return indices[:4]

