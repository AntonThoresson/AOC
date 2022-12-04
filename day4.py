f = open("day4.txt").read().strip()
lines = [x.strip() for x in f.split("\n")]
ans = 0
for line in lines:
    one,two = line.split(",")
    s1,e1 = one.split("-")
    s2,e2 = two.split("-")
    s1,e1,s2,e2 = [int(x) for x in [s1,e1,s2,e2]]
    if s1<=s2 and e2<=e1 or s2<=s1 and e1<=e2:
        ans+=1

print(ans)

ans2 = 0
for line in lines:
    one,two = line.split(",")
    s1,e1 = one.split("-")
    s2,e2 = two.split("-")
    s1,e1,s2,e2 = [int(x) for x in [s1,e1,s2,e2]]
    if not (e1 < s2 or e2 < s1):
        ans2+=1
print(ans2)
