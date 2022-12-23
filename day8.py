import numpy as np

data = open("day8.txt").read().strip().split()


grid = [list(map(int, list(line))) for line in data]

rows = len(grid)
cols = len(grid[0])

grid = np.array(grid)

ans = 0
for row in range(rows):
    for col in range(cols):
        height = grid[row, col]

        if col == 0 or np.amax(grid[row, :col]) < height:
            ans += 1
        elif col == cols-1 or np.amax(grid[row, (col+1):]) < height:
            ans += 1
        elif row == 0 or np.amax(grid[:row, col]) < height:
            ans += 1
        elif row == rows-1 or np.amax(grid[(row+1):, col]) < height:
            ans += 1

print(ans)

# PART 2

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
ans2 = 0
for row in range(rows):
    for col in range(cols):
        height = grid[row, col]
        score = 1

        for dr, dc in directions:
            rr, cc, = row + dr, col + dc
            dist = 0


            while (0 <= rr < rows and 0 <= cc < cols) and grid[rr, cc] < height:
                dist += 1 
                rr += dr
                cc += dc

                if (0 <= rr < rows and 0 <= cc < cols) and grid[rr, cc] >= height:
                    dist += 1

            score *= dist
        
        ans2 = max(ans2, score)

print(ans2)
