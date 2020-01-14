# Movie-Recommender

## Synopsis
The goal of this project is to create a movie recommender with a web interface. The recommendation model is based on the MovieLens dataset (https://grouplens.org/datasets/movielens/)


## Algortihms
These (unsupervised) algorithms can be used in recommender systems

### Non-negative Matrix Factorization (NMF) Model
The starting point is a rating matrix,

![Screenshot](rating_m.png)

The goal is to describe this matrix by some hidden features (for example, a user gives higher ratings to a particular movie genre) such as the matrix (V) is factorized into two matrices (W- user features and H-movie features) that contain the inherent aspects/features.

- All three matrices have no negative elements.
- The product of W and H approximates V

![Screenshot](nmf.png)


It might be that there are empty elements (NaNs) in the matrix V with the ratings; we could replace the NaNs with: Zeros, the median of the whole matrix or the median of each movie.

Sklearn has implemented the nmf model.  

### Cosine Similarities
The idea behind this algorithm is to find the most similar users and get recommendations based on this similarity: if user1 and user2 rated movie1, movie2 and movie3 similarly but user2 has not seen movie4, this movie might be a good recommendation for user2.

By applying this algorithm, one could visualize (with a heat map) the similarity of various users,

![Screenshot](cos_sim.png)




## Web Interface
