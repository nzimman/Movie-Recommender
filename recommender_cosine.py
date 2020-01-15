import pandas as pd
import math
from sklearn.metrics.pairwise import cosine_similarity
from postgres_data import create_movie_matrix_clean
import random



def calculate_cosim(db,user_input):

    #Read user input
    user_input = dict(user_input).values()
    movies = list(user_input)[0::2] #list of strings
    ratings = list(user_input)[1::2] #list of strings

    df = create_movie_matrix_clean(db)

    idlist =[]
    for m in movies:
        n = df[df['clean_title'] == m]['movieid'].iloc[0]
        idlist.append(n)

    R = df[['userid','movieid','rating']]
    R.set_index(['movieid', 'userid'])['rating']
    R = R.pivot_table(values='rating',index='userid',columns='movieid')

    #Add new userid
    new_user_id = R.index[-1]+1
    R = R.append(pd.Series(name=new_user_id))
    print(R.loc[611,1])
    # Add ratings for the given movvies
    for i,j in enumerate(idlist):
        R.loc[R.index[-1],j] = float(ratings[i])

    # Replace NaN with 3
    P = R.fillna(3.0)
    # Remove the mean
    P2 = P-3.0
    # Center
    P3 = P2/2.0

    # Calculate cosine similarity
    result = cosine_similarity(P3)
    result_new_user = result[-1]

    #Find most similar id users
    ids = result_new_user.argsort()[::-1][:n]
    most_similar_3_users = ids[0:3]

    #Find the movies they like
    recommendations = df[(df['userid']== ids[0]) & (df['rating']>4.0) & (df['movieid'].isin(idlist) == False)]['clean_title']
    moview_item = random.choices(recommendations.values, k=5)

    return moview_item
