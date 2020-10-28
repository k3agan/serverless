(_, A) = (int(input()), set(map(int, input().split())))
B = int(input())
for _ in range(B):
    (command, newSet) = (input().split()[0],set(map(int, input().split())))
    getattr(A,command)(newSet)
    # getattr(A,'function') is equivalent to A.function
    # newSet is the argument taken into the function.

print(sum(A))

