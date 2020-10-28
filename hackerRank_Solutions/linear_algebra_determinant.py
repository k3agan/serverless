import numpy
n = int(input())

arr1 = numpy.array([input().split() for _ in range(n)], float)

print(round(numpy.linalg.det(arr1),2))