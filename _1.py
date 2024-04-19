import random
c = []
d = []
for i in range(1,20):
    c.append(random.randint(1,1000))
# print(c,c.index(min(c)),min(c))
print(c,min(c),c.index(min(c)))
b = c[c.index(min(c)):]
d = [x for x in b if (b.index(x)+1)%2!=0]
print(b,d)