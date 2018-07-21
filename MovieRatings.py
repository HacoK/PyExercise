'''
Download .zip file "ml-latest-small.zip" recommended for education and development from url "https://grouplens.org/datasets/movielens/".
The data are contained in the files `links.csv`, `movies.csv`, `ratings.csv` and `tags.csv`.
This dataset describes 5-star rating and free-text tagging activity.
Users were selected at random for inclusion. All selected users had rated at least 20 movies.
No demographic information is included. Each user is represented by an id, and no other information is provided.

Finish these question in problem.py using pandas library:
<1>What are the name of the movie of which movie Id is 1?
<2>How many genres for movie which movie Id is 1?
<3>What is name of the most rated movie?

return [movieNameOfMovieId1, genresCounts, movieNameOfTheMostRatedMovie]
movieNameOfMovieId1 is the answer of question (1)
genresCounts is the answer of question (2)
movieNameOfTheMostRatedMovie is the answer of question (3)

'''

#-*- coding:utf-8 -*-
import pandas as pd


class Solution():
    def solve(self):
        moviesInfo = pd.read_csv('movies.csv')
        rateInfo = pd.read_csv('ratings.csv')
        movieNameOfMovieId1Row = moviesInfo[moviesInfo.movieId == 1]
        movieNameOfMovieId1 = movieNameOfMovieId1Row.iat[0, 1]
        genresCounts = len(movieNameOfMovieId1Row.iat[0, 2].split('|'))
        movieIds = list(moviesInfo['movieId'])
        rateMovieIds = list(rateInfo['movieId'])
        rateNumList = [rateMovieIds.count(item) for item in movieIds]
        maxNum = max(rateNumList)
        index = rateNumList.index(maxNum)
        movieId = movieIds[index]
        movieNameOfTheMostRatedMovie = moviesInfo[moviesInfo.movieId == movieId].iat[0, 1]
        return [movieNameOfMovieId1, genresCounts, movieNameOfTheMostRatedMovie]
        pass