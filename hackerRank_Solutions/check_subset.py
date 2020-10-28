# First pass

T = int(input())

for _ in range(T):
    (_,A) = (input(), set(map(int,input().split())))
    (_,B) = (input(), set(map(int,input().split())))
    print(A.issubset(B))

# Condensed version

for _ in range(int(input())):
    (_,A,_,B) = (input(), set(map(int,input().split())),input(),set(map(int,input().split())))
    print(A.issubset(B))