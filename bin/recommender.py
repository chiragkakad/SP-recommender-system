"""
@Author: Chirag Kakad
@Description: recommender  class for the senior project demo application.
"""

from math import *

class recommender:
    """
A class use for making recommendations.
Uses user - user collaborative filtering with cosine similarity.
    """
    def __init__(self, ratings, similarity, neighbor = 20):
        """
        ratings is the dict object of all ratings by movielence users.
        similarity is the similarity function to use.
        neighbor is the neighborhood size to use.
        """
        self.ratings = ratings
        self.neighbor = neighbor
        self.similarity = similarity
        self.avg = self.avg_all(self.ratings)
    
    def avg_all(self, pref):
    #gets the average for all users.
        avg1 = {}
        for i in pref.keys():
            avg1[i] = 0.0
            for j in pref[i].keys():
                avg1[i] += pref[i][j]
            avg1[i] /= float(len(pref[i]))
        return avg1
    
    def topN(self, target):
    #Gets the top N similar users to the target user .
        top = []
        for i in self.ratings.keys():
            s = self.similarity(target, self.ratings[i])
            if s > 0.0: top.append([i, s])
        top.sort(key= lambda a: a[1], reverse=True)
        return top[:self.neighbor]

    def recommend(self, target):
    #Gets recommendations for the target user by using N neighbors.
    #N is the neighborhood size.
    #num is the number of recommendations
        total = {}
        avg_target = 0.0
        for i in target.keys(): avg_target += target[i]
        avg_target /= len(target)
        ss = 0.0
        #Gets top N similar users
        top = self.topN(target)
        #Calculates the predicted rating for all the unseen items.
        for i in top:
            for (key, val) in self.ratings[i[0]].iteritems():
                if key in target: continue
                if key not in total:
                    total[key] = 0.0
                total[key] += ((val - self.avg[i[0]]) * i[1])
                ss += i[1]
            #Converts the dictionary to list.
        rank = []
        for key, val in total.iteritems():
            rank.append([key, (avg_target + (val / float(ss) ))])
        rank.sort(key= lambda a: a[1], reverse=True)
        return rank

