# battleship.py

import random
SIZE = 6

def make_grid(n):
    return [["." for _ in range(n)] for _ in range(n)]

def show(grid, reveal=False):
    print("  A B C D E F")
    for i, row in enumerate(grid, start=1):
        out = []
        for cell in row:
            out.append(cell if (cell != "S" or reveal) else ".")
        print(f"{i} " + " ".join(out))

def place_ship_horiz(grid, length):
    r = random.randint(0, SIZE - 1)
    c = random.randint(0, SIZE - length)
    for i in range(length):
        grid[r][c + i] = "S"

def parse_coord(text):
    t = text.strip().upper()
    col = ord(t[0]) - ord("A")
    row = int(t[1:]) - 1
    return row, col  # ✅ corrigé

def shoot(grid, r, c):
    if not (0 <= r < SIZE and 0 <= c < SIZE):
        print("Hors grille"); return
    if grid[r][c] == "S":
        grid[r][c] = "X"; print("TOUCHE")
    elif grid[r][c] == ".":
        grid[r][c] = "o"; print("A L'EAU")
    else:
        print("Déjà visé")

def main():
    g = make_grid(SIZE)
    place_ship_horiz(g, 3)
    print("A1 (ou vide pour quitter).")
    show(g)  # désormais 'S' masqués
    while True:
        s = input("Tir: ")
        if not s.strip(): print("Révélation:"); show(g, True); break
        r, c = parse_coord(s)
        shoot(g, r, c)
        show(g)

if __name__ == "__main__":
    main()
