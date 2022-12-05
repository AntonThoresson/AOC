with open("day5.txt") as f:
    inst = f.read()[:-1].split("\n\n")
    initStacks = inst[0].split("\n")
    stacks = [[] for _ in range(9)]

    for i in range(8):
        line = initStacks[i]
        crates = line[1::4]
        for j in range(len(crates)):
            if crates[j] != " ":
                stacks[j].append(crates[j])

stacks = [stack[::-1] for stack in stacks]

for line in inst[1].split("\n"):
    nr = line.split(" ")
    n,source,dest = map(int, [nr[2], nr[4], nr[6]])
    source -= 1 
    dest -= 1

    for _ in range(n):
        pop = stacks[source].pop()
        stacks[dest].append(pop)


top = [stack[-1] for stack in stacks]
print("".join(top))

# Part 2

for line in inst[1].split("\n"):
    nr = line.split(" ")
    n,source,dest = map(int, [nr[2], nr[4], nr[6]])
    source -= 1 
    dest -= 1
    
    stacks[dest].extend(stacks[source][-n:])
    stacks[source] = stacks[source][:-n]

top = [stack[-1] for stack in stacks]
print("".join(top))
