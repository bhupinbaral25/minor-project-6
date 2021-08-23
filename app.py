
from src import clean_sentence as cs
from src import utils

from sentence_transformers import SentenceTransformer

if __name__ == '__main__':
    #import pretrain model
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    data_set = './data/abcnews-date-text.csv'
    news_data = utils.read_data(data_set)
    #Take input from user 
    user_query = input('Enter the sentence to search in the headlines')

    clean_query = cs.clean_sentences(user_query)
    clean_dataset = cs.get_clean_dataframe(news_data, 'headline_text')

    #Calculate Similarity score of given sentence to other sentence in datasets
    similarity_score = utils.get_similarity_score(model, clean_dataset, clean_query, 'cleaned_sentence')

    high_similarity_score_index = utils.get_high_similarity_score_index(similarity_score)
    print("\nSimilar sentences to your questions are as follows:\n")
    for index in high_similarity_score_index:
        print(news_data['headline_text'][index])




