# Movie-Recommender

## Synopsis
The goal of this project is to create a movie recommender with a web interface. The recommendation model is based on the MovieLens dataset (https://grouplens.org/datasets/movielens/)


## Non-negative Matrix Factorization (NMF) Model
It is an unsupervised algortihm where a matrix (the data) is factorized into two matrices that contain inherent aspects/features.
- All three matrices have no negative elements.
- The product of W and H approximates V

![Screenshot](nmf.png)



For finding these two matrices, use from sklearn.decomposition the nmf model. 

## Cosine Similarities

## Web Interface
