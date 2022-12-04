f = [l.strip() for l in open("day1.txt")]

Q = []
for i in ("\n".join(f)).split("\n\n"):
    q = 0
    for j in i.split("\n"):
        q += int(j)
    Q.append(q)

s = sorted(Q)
print(s)
print(s[-1] + s[-2] + s[-3])
print(max(Q))
