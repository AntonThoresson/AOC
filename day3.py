ans2 = 0
def score(c):
    if 'a'<=c<='z':
        return ord(c)-ord('a')+1
    else:
        return ord(c)-ord('A')+27
f = [line for line in open("day3.txt")]
i = 0
while i < len(f):
    for c in f[i]:
        if c in f[i+1] and c in f[i+2]:
            ans2+=score(c)
            break
    i+=3
print(ans2)

ans = 0
for line in open("day3.txt"):
    x = line.strip()
    y,z = x[:len(x)//2], x[len(x)//2:]
    for c in y:
        if c in z:
            if 'a'<=c<='z':
                ans+=ord(c)-ord('a')+1
            else:
                ans+=ord(c)-ord('A')+27
            break

print(ans)
