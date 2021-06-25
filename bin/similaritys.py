"""
@Author: Chirag Kakad
@Description: Implementation of similarity functions for the senior project demo application.
"""

from math import *

def cosine_similarity(p1, p2):
    mu = {}
    for i in p1:
        if i in p2:
            mu[i] = 1
    if len(mu) == 0: return 0
    numerator = 0.0
    denominator0 = 0.0
    denominator1 = 0.0
    for i in mu:
        numerator += p1[i] * p2[i]
    for i in p1: denominator0 += p1[i]
    for i in p2: denominator1 += p2[i]
    denominator = sqrt(denominator0) * sqrt(denominator1)
    return numerator/float(denominator)

def euclidean(p1, p2):
    mu = {}
    for i in p1:
        if i in p2: mu[i] = 1
    if len(mu) == 0: return 0
    sum_of_squares=sum([pow(p1[item]-p2[item],2) for item in mu])
    return 1/(1+sqrt(sum_of_squares))

