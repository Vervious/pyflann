from pyflann import *
import numpy as np

dataset = np.array(
    [[1., 1, 1, 2, 3],
     [10, 10, 10, 3, 2],
     [100, 100, 2, 30, 1]
     ])
moreset = np.array(
    [[2., 3, 4, 2, 3]
     ])
testset = np.array(
    [[1., 1, 1, 1, 1],
     [90, 90, 10, 10, 1]
     ])
# flann = FLANN()
# result, dists = flann.nn(
#     dataset, testset, 2, algorithm="kmeans", branching=32, iterations=7, checks=16)
# print result
# print dists

flann = FLANN()
# params = flann.build_index(dataset, algorithm="kmeans", branching=32, iterations=7)
params = flann.build_index(dataset, algorithm="autotuned", target_precision=0.9, log_level = "info")
# print params
# result, dists = flann.nn_index(testset, 2, checks=16)
# print result
# print dists
# add more points
flann.add_points(moreset)
result, dists = flann.nn_index(testset, 2, checks=16)
print result
print dists

# dataset = np.random.rand(10000, 128)
# testset = np.random.rand(1000, 128)
# flann = FLANN()
# result, dists = flann.nn(
#     dataset, testset, 5, algorithm="kmeans", branching=32, iterations=7, checks=16)
# print result
# print dists
