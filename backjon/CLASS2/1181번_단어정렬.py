k = int(input())
b= [input() for _ in range(k)]
a = sorted(set(b), key=lambda x: (len(x),x))
for i in a:
    print(i)