a, b, c = map(int, input().split())
conj = []
conj.append(a)
conj.append(b)
conj.append(c)
for i in sorted(conj):
    print(i)
print()
for i in conj:
    print(i)