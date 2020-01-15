import pandas as pd
import random

def deep_recommender(num, movie_list,ratings_list):
    """
    Here is where we take the user input (movie_lis, ratings_list)
    and process as inputs to the model
    """
    #Pseudo code
    user_vector = process_user_input(movie_list,ratings_list)
    nmf_model = load_trained_model('model.h5')
    user_profile = nmf_model.transform(user_vector)
    user_results = np.dot(user_profile,nmf_model.components_)
    user_results_final = convert_to_mames(user_results)
    #Pseudo code

    movies = pd.read_csv('movies.csv',header=None)[0].tolist()
    random.shuffle(movies)
    #return movies[:num]
    return user_results_final
