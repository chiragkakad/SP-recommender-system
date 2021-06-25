"""
@Author: Chirag Kakad
@Description: Entry point for the senior project demo application.
"""

from bin import *
import operator

genres_map = map_genres()



def selectFile():
    #Function to select user profile.
    global profile
    while True:
        file = raw_input("Enter the file name with path: ")
        profile = load_profile(file)
        if len(profile) != 0: break
        else: print "Error, try again."

def searchGenres():
    #Function to show all movies in a genre.
    while True:
        print "Enter a genre ID to search."
        print "If you would like to search by multiple genres, please enter the corresponding value and separate it by a space."
        print "Enter 0 to go back."
        tmp = sorted(genres_map.items(), key=operator.itemgetter(1))
        for i in tmp:
            print "%d\t%s" % (i[1]+1, i[0])
        ch = raw_input("Select: ")
        if ch == '0': return []
        ch = ch.split(' ')
        for j in movies.keys():
            tmp = movies[j]['genre']
            add = True
            for k in ch:
                if tmp[int(k)-1] != 1: add = False
            if add: print "%s\t%s\t%s" %(j, movies[j]['title'], getGenres(j))
    
def searchTitle():
    #Function to search the movie by title.
    title = raw_input("Enter the movie title to search for: ")
    for i in movies.keys():
        if title.lower() in movies[i]['title'].lower(): print "%s\t%s\t%s" %(i, movies[i]['title'], getGenres(i))

def getGenres(m):
#get the list of genres as string for the given movie.
    st = ''
    tmp = movies[m]['genre']
    for i in genres_map.keys():
        if tmp[genres_map[i]] > 0: st += '%s\t' % (i)
    return st

def show_movies(r, num = None):
    #function to display the recommended movies.
    count = 0
    for i in r:
        if num and count == num: break
        st = "%s\t%s\t%s%r" % (i[0], movies[i[0]]["title"], getGenres(i[0]), round(i[1], 3))
        print st
        count += 1

def build_filter():
    #function to build the filter list to block the unwanted movies from the recommendation list.
    print "Select the genres in which you are not interested by entering the corresponding number."
    print "If you would like to blacklist multiple genres, please enter the corresponding value and separate it by a space."
    print "Enter 0 to go back without blacklisting.\n"
    tmp = sorted(genres_map.items(), key=operator.itemgetter(1))
    for i in tmp:
        print "%d\t%s" % (i[1]+1, i[0])
    print "20 to clear the list"
    ch = raw_input("Select: ")
    if ch == '0': return filt
    if ch == '20': return []
    ch = ch.split(' ')
    return [int(i)-1 for i in ch if int(i) < 20]

def filter(filterList, rec):
    #function to filter movie by genre.
    r = []
    for i in rec:
        add = True
        tmp = movies[i[0]]['genre']
        for j in filterList:
            if tmp[j] == 1:
                add = False
                break
        if add: r.append(i)
    return r

rec = recommender(load_training(), cosine_similarity, 10)
movies = load_movies()
profile = {}
filt = []
ch = -1
while True:
    print "Enter: "
    print "1 to get recommendations."
    print "2 to select input preference file."
    print "3 to blacklist genres."
    print "4 to search movie by title."
    print "5 to search movie by genres."
    print "6 to show the movies in the preference file."
    print "0 to exit."
    ch = int(raw_input("Select: "))
    if ch == 0: break
    if ch == 1:
        if len(profile) == 0: selectFile()
        r = rec.recommend(profile)
        show_movies(filter(filt, r), 10)
    if ch == 2: selectFile()
    if ch == 3: filt = build_filter()
    if ch == 4: searchTitle()
    if ch == 5: searchGenres()
    if ch == 6:
        print "Movies: "
        show_movies([[i, profile[i]] for i in profile.keys()])
