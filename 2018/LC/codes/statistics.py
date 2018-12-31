# -*- coding: utf-8 -*-
# title: statistics.py
# course: Language and Computer
# author(s): Suzi Park
# date created: 2018-11-02
# description: basic statistics (with SciPy)

# Original code: ch05_statistics.py (without SciPy)
# https://github.com/insightbook/Data-Science-from-Scratch/blob/master/code/ch05_statistics.py

import matplotlib.pyplot as plt # 그림 그리기
from collections import Counter # 빈도 세기

# import numpy as np
# import scipy
# import scipy.stats

# 5.1 데이터셋 설명하기 -- 한 종류의 데이터

# 데이터
num_friends = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

# 히스토그램
friend_counts = Counter(num_friends) # 빈도표
# friend_counts[17] # no KeyError
plt.bar(friend_counts.keys(), friend_counts.values()) # 막대그래프
plt.show()

# 통계치
num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)

# 5.1.1 중심 경향성(central tendency)
# 통계치: 평균, 중위수, 최빈값
# (1) 평균(mean)
def mean(x):
    return sum(x) / len(x)

mean(num_friends)
# scipy.mean(num_friends)

# (2) 중위수(median)
def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    midpoint = n // 2
    sorted_v = sorted(v)
    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        return mean(sorted_v[midpoint-1:midpoint+1])

median(num_friends)
# scipy.median(num_friends)

# (3) 최빈값(mode)
def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]

mode(num_friends)
# scipy.stats.mode(num_friends)

# 분위
def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

quantile(num_friends, 0.10)
quantile(num_friends, 0.25)
quantile(num_friends, 0.75)
quantile(num_friends, 0.90)
# scipy.quantile(num_friends, 0.10)
# scipy.quantile(num_friends, 0.25)
# scipy.quantile(num_friends, 0.75)
# scipy.quantile(num_friends, 0.90)

# 5.1.2 산포도(dispersion) "퍼짐 경향성"
# 통계치: 범위, 분산, 표준편차
# (1) 범위
# "range" already means something in Python, so we'll use a different name
def data_range(x):
    return max(x) - min(x)

data_range(num_friends)
# np.ptp(num_friends)


# (2) 분산, 표준편차
def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

de_mean(num_friends)
# np.array(num_friends) - np.mean(num_friends)

# from vectors import sum_of_squares
def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

variance(num_friends)
# scipy.var(num_friends, ddof=1)


def standard_deviation(x):
    return variance(x) ** (1/2)

standard_deviation(num_friends)
# scipy.std(num_friends, ddof=1)


# (3) 사분위범위
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

interquartile_range(num_friends)
# scipy.stats.iqr(num_friends)


# 5.2 상관관계 --- 두 종류의 데이터
daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]


# 공분산
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

covariance(num_friends, daily_minutes)
# scipy.cov(num_friends, daily_minutes)[0,1]


# 상관계수
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero

correlation(num_friends, daily_minutes)
# scipy.corrcoef(num_friends, daily_minutes)[0,1]


# 산점도 
plt.scatter(num_friends, daily_minutes)
plt.show()

# 이상치 제거
outlier = num_friends.index(100) # index of outlier

num_friends_good = [x 
                    for i, x in enumerate(num_friends) 
                    if i != outlier]

daily_minutes_good = [x 
                      for i, x in enumerate(daily_minutes) 
                      if i != outlier]

correlation(num_friends_good, daily_minutes_good)
plt.scatter(num_friends_good, daily_minutes_good)
plt.show()
