# Dynamic programming

def dynamic(word_a, word_b):
    grid = []
    for i in range(0, len(word_a)):
        grid.append([])
        for j in range(0, len(word_b)):
            print(word_a[i] + " " + word_b[j], end=" ")
            if i == 0 or j == 0:
                if word_a[i] == word_b[j]:
                    print("MATCH")
                    grid[i].append(1)
                else:
                    print("")
                    grid[i].append(0)
            else:
                if word_a[i] == word_b[j]:
                    print("MATCH")
                    grid[i].append(grid[i-1][j-1] + 1)
                else:
                    print("")
                    grid[i].append(max(grid[i-1][j], grid[i][j-1]))

    # Show the grid.
    for row in grid:
        print(str(row))

word_a = input("Word A: ")
word_b = input("Word B: ")
dynamic(word_a, word_a)
