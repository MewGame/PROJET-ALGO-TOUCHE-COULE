# battleship.py

import random
SIZE = 6

def make_grid(n): 
    return [["." for _ in range(n)] for _ in range(n)]

def show(grid, reveal=False):
    print("  A B C D E F")
    for i, row in enumerate(grid, start=1):
        vis = [c if (c != "S" or reveal) else "." for c in row]
        print(f"{i} " + " ".join(vis))

def place_ship_horiz(grid, L):
    r = random.randint(0, SIZE-1)
    c = random.randint(0, SIZE-L)
    for i in range(L): 
        grid[r][c+i] = "S"

def parse_coord(t):
    t = t.strip().upper()
    if " " in t:
        a, b = t.split()
        if a.isdigit() and b.isdigit(): return int(a)-1, int(b)-1
    col = ord(t[0]) - ord("A")
    row = int(t[1:]) - 1
    return row, col

def shoot(g, r, c):
    if not (0 <= r < SIZE and 0 <= c < SIZE): print("Hors grille"); return
    if g[r][c] == "S": 
        g[r][c] = "X"; print("TOUCHE")
    elif g[r][c] == ".": 
        g[r][c] = "o"; print("A L'EAU")
    else: print("Déjà visé")

def main():
    g = make_grid(SIZE)
    place_ship_horiz(g, 3)
    print("Formats: A1 ou '2 3'. Vide = quitter.")
    show(g)
    while True:
        s = input("Tir: ")
        if not s.strip(): 
            print("Révélation:"); show(g, True); break
        r, c = parse_coord(s)
        shoot(g, r, c)
        show(g)

if __name__ == "__main__":
    main()
