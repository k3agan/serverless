# the question asks to take some input commands and apply them to a list.

# first pass
N = int(input())
l = []
for _ in range(N):
    s = input().split()
    command = s[0]
    arguments = s[1:]
    if(command.strip() != 'print'):
        getattr(l,str(command))(*(map(int,arguments)))
    else:
        print(l)

# condensed
    l = []
    for _ in range(int(input())):
        s = input().split()
        getattr(l,str(s[0]))(*(map(int,s[1:]))) if(s[0].strip() != 'print') else print(l)
