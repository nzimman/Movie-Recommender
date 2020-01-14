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

## Web Interface
