import numpy

n = int(input())

arr1 = numpy.array([input().split(' ') for _ in range(n)],int)
arr2 = numpy.array([input().split(' ') for _ in range(n)],int)

print(arr1 @ arr2) #finds the dot product of (n x n) matrix. (sidenote: the "@" operator for finding dot product requires the numpy library)