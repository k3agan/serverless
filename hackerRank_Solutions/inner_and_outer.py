import numpy

arr1 = numpy.array([input().split(' ') for _ in range(2)], int)
inner = numpy.inner(arr1[0],arr1[1])
outer = numpy.outer(arr1[0],arr1[1])
print(inner)
print(outer)