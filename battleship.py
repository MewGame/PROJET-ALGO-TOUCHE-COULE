# battleship.py

import random
SIZE = 6

def make_grid(n): return [["." for _ in range(n)] for _ in range(n)]

def show(grid):
    print("  A B C D E F")
    for i, row in enumerate(grid, start=1):
        print(f"{i} " + " ".join(row))

def place_ship_horiz(grid, length):
    r = random.randint(0, SIZE-1)
    c = random.randint(0, SIZE-length)
    for i in range(length):
        grid[r][c+i] = "S"

def main():
    g = make_grid(SIZE)
    place_ship_horiz(g, 3)
    show(g)

if __name__ == "__main__":
    main()
