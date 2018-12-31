# -*- coding: utf-8 -*-
# title: vectors.py
# course: Language and Computer
# author(s): Suzi Park
# date created: 2018-11-02
# description: vector and matrix arithmetic (in NumPy)

# Original code: ch04_linear_algebra.py (without NumPy)
# https://github.com/insightbook/Data-Science-from-Scratch/blob/master/code/ch04_linear_algebra.py

# import numpy as np
# from numpy import linalg as LA

height_weight_age = [70,   # inches
                     170,  # pounds
                     40]   # years

grades = [95, # Test1
          85, # Test2
          75, # Test3
          72] # Test4
# 
# functions for working with vectors
#

# two 4-dimemsional vectors
v = [1, 7, 8, 3]
w = [3, 4, 3, 9]
u = [0, 9, 2, 5]

def vector_add(v, w):
    """adds two vectors componentwise"""
    return [v_i + w_i for v_i, w_i in zip(v,w)]

vector_add(v, w)
# np.add(v, w)


def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return [v_i - w_i for v_i, w_i in zip(v,w)]

vector_subtract(v, w)
# np.subtract(v, w)


def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

vector_sum([v, w, u])
# np.sum([v, w, u], axis=0)


def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

scalar_multiply(-2, v)
# np.multiply(-2, v)


def vector_mean(vectors):
    """compute the vector whose i-th element is the mean of the
    i-th elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

vector_mean([v, w, u])
# np.mean([v, w, u], axis=0)


def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

dot(v, w)
# np.dot(v, w)


def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

sum_of_squares(v)
# np.sum(np.square(v))


def magnitude(v):
    return sum_of_squares(v) ** (1 / 2)

magnitude(v)
# LA.norm(v, 2)


def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

squared_distance(v, w)
# np.sum(np.square(np.subtract(v, w)))


def distance(v, w):
   return squared_distance(v, w) ** (1/2)

distance(v, w)
# LA.norm(np.subtract(v, w), 2)

# from scipy.spatial import distance
# distance.euclidean(v, w)


# Use NumPy!
# BEFORE NumPy
v + w # concatenation not sum
-2 * v # reperition not multiplication
[v, w, u] # "matrix"

# AFTER NumPy
import numpy as np
# Arrays
# v, w, u = np.array(v), np.array(w), np.array(u)
v, w, u = map(np.array, [v, w, u])

v + w
-2 * v
v.dot(w)
v.dot(v)

# Matrices
A = np.array([v, w, u])
A.shape # 3-by-4 matrix
print(A)

# matrix multiplication
B = np.random.randint(-2, 3, size=(4, 2))
print(B)
np.dot(A, B) # 3-by-2 matrix

# identity matrix of size 4
I = np.identity(4, dtype=int)
A.dot(I)

A[1, 2] # (1,2) component
A[2, :] # 2nd row
A[:, 0] # 0th column

np.zeros((4, 2), dtype=int) # zero matrix
np.ones((4, 2), dtype=int) # one matrix

C = np.zeros((4, 2), dtype=int)
C[2,1] = 1
C[3,:] = 2
print(C)
