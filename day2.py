# Rock = X - 1, Paper = Y - 2, Sicssor = Z - 3 -- 3 if draw -- 6 if win
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

with open("day2.txt") as f:
    d = [l for l in f.read().strip().split("\n")]

s = 0
s2 = 0
scores = {"A X":4, "A Y":8, "A Z":3,
        "B X":1, "B Y":5, "B Z":9,
        "C X":7, "C Y":2, "C Z": 6
        }

scores2 = {"A X":3, "A Y":4, "A Z":8,
        "B X":1, "B Y":5, "B Z":9,
        "C X":2, "C Y":6, "C Z":7 
        }

for i in d:
    s += scores[i]
    s2 += scores2[i]

print(s)
print(s2)
