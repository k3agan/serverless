# first pass was: 

k = int(input())
rooms = list(map(int,input().split()))
newSet = set(rooms)

for i in newSet:
    if rooms.count(i) == 1:
        print(i)

# time complexity here is too long here because it passes through the list k+1 times.
# So I found something better

k, rooms, single, multiple = input(), list(map(int, input().split())),set(),set()
for room in rooms: single.add(room) if room not in single else multiple.add(room)
print(single.difference(multiple).pop())

# this version only passes the list once, then compares 2 sets of length k and k+1
# I think this is a good solution, although there might be a way to solve this mathematically..