"""
@Author: Chirag Kakad
@Description: data loader  class for the senior project demo application.
"""

basePath = "./data/"

def load_training():
#Loads the trainging data in a dict object.
    ratings = {}
    f = open("%su.data" % basePath, "r")
    data = f.readlines()
    for i in data:
        tmp = i.split('\t')
        if tmp[0] not in ratings.keys():
            ratings[tmp[0]] = {}
        ratings[tmp[0]][tmp[1]] = float(tmp[2])
    f.close()
    return ratings

def load_movies():
#Loads the movie metadata in a dict object.
    movies = {}
    f = open("%su.item" % basePath, "r")
    data = f.readlines()
    for i in data:
        tmp = i.split("|")
        tmp1 = []
        for j in range(5, len(tmp)):
            tmp1.append(int(tmp[j]))
        movies[tmp[0]] = {}
        movies[tmp[0]]['title'] = tmp[1]
        movies[tmp[0]]['genre'] = tmp1
        movies[tmp[0]]['year'] = tmp[2]
    f.close()
    return movies

def load_profile(path):
    #Function to load the user profile into a dict object.
    try:
        f = open(path, "r")
        data = f.readlines()
        end_user = {}
        for i in data:
            tmp = i.split('\t')
            end_user[tmp[0]] = float(tmp[1])
        f.close()
        return end_user
    except (IOError, OSError) as e:
        return {}
    