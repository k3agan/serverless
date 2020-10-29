# first pass

(A,ans) = (set(input().split()), True)
for _ in range(int(input())):
    if(not A > set(input().split())):
        ans = False
print(ans)


# condensed version

a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))
