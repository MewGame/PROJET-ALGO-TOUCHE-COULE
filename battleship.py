# battleship.py

import random

SIZE = 6

def make_grid(n): 
    return [["." for _ in range(n)] for _ in range(n)]

def show(grid, reveal=False):
    print("  A B C D E F")
    for i, row in enumerate(grid, start=1):
        cells = []
        for cell in row:
            if cell == "S" and not reveal:
                cells.append(".")
            else:
                cells.append(cell)
        print(f"{i} " + " ".join(cells))

def place_ship(grid, L):
    while True:
        horiz = random.choice([True, False])
        if horiz:
            r = random.randint(0, SIZE-1)
            c = random.randint(0, SIZE-L)
            if all(grid[r][c+i] == "." for i in range(L)):
                for i in range(L): grid[r][c+i] = "S"
                return
        else:
            r = random.randint(0, SIZE-L)
            c = random.randint(0, SIZE-1)
            if all(grid[r+i][c] == "." for i in range(L)):
                for i in range(L): grid[r+i][c] = "S"
                return

def place_fleet(grid, sizes):
    for L in sizes:
        place_ship(grid, L)

def parse_coord(t):
    t = t.strip().upper()
    if " " in t:
        a,b = t.split()
        if a.isdigit() and b.isdigit(): return int(a)-1, int(b)-1
        return None
    if len(t) >= 2 and t[0].isalpha() and t[1:].isdigit():
        return int(t[1:]) - 1, ord(t[0]) - ord("A")
    return None

def shoot(grid, r, c):
    if not (0 <= r < SIZE and 0 <= c < SIZE): 
        return "out"
    if grid[r][c] == "S": 
        grid[r][c] = "X"; 
        return "hit"
    if grid[r][c] == ".": 
        grid[r][c] = "o"; 
        return "miss"
    return "repeat"

def all_sunk(g):
    for row in g:
        for cell in row:
            if cell == "S": 
                return False
    return True

def main():
    g1 = make_grid(SIZE) 
    g2 = make_grid(SIZE)  
    place_fleet(g1, [3,2,1])
    place_fleet(g2, [3,2,1])

    score1 = 0
    score2 = 0
    turn = 1

    print("1v1 Console — Flottes 3/2/1. +2 hit, -1 miss, +3 bonus fin. Vide pour quitter.")
    while True:
        if turn == 1:
            print("\n=== Tour Joueur 1 ===")
            print("Votre grille (J1):")
            show(g1, reveal=True)
            print("Grille de l'adversaire (J2):")
            show(g2, reveal=False)
            s = input("J1 tire (ex: A1 ou '2 3'): ")
            if not s.strip():
                print("Fin. Scores — J1:", score1, " J2:", score2)
                print("Révélations:"); 
                show(g1, True); show(g2, True); 
                break
            pos = parse_coord(s)
            if pos is None: 
                print("Entrée invalide."); 
                continue
            r,c = pos
            res = shoot(g2, r, c)
            if res == "hit": 
                print("TOUCHE !"); 
                score1 += 2
            elif res == "miss": 
                print("A L'EAU."); 
                score1 -= 1
            elif res == "repeat": 
                print("Déjà visé (score inchangé)")
            else: 
                print("Hors grille (score inchangé)")
            print("Score J1:", score1)
            if all_sunk(g2):
                score1 += 3
                print("🏆 J1 gagne ! Bonus +3. Score final J1:", score1, "/ J2:", score2)
                print("Révélations:"); show(g1, True); 
                show(g2, True); 
                break
            turn = 2
        else:
            print("\n=== Tour Joueur 2 ===")
            print("Votre grille (J2):")
            show(g2, reveal=True)
            print("Grille de l'adversaire (J1):")
            show(g1, reveal=False)
            s = input("J2 tire (ex: A1 ou '2 3'): ")
            if not s.strip():
                print("Fin. Scores — J1:", score1, " J2:", score2)
                print("Révélations:"); show(g1, True); 
                show(g2, True); 
                break
            pos = parse_coord(s)
            if pos is None: 
                print("Entrée invalide."); 
                continue
            r,c = pos
            res = shoot(g1, r, c)
            if res == "hit": 
                print("TOUCHE !"); 
                score2 += 2
            elif res == "miss": 
                print("A L'EAU."); 
                score2 -= 1
            elif res == "repeat": 
                print("Déjà visé (score inchangé)")
            else: 
                print("Hors grille (score inchangé)")
            print("Score J2:", score2)
            if all_sunk(g1):
                score2 += 3
                print("🏆 J2 gagne ! Bonus +3. Score final J2:", score2, "/ J1:", score1)
                print("Révélations:"); 
                show(g1, True); show(g2, True); 
                break
            turn = 1

if __name__ == "__main__":
    main()
