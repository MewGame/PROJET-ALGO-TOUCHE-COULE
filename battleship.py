# battleship.py

import random
SIZE = 6

def make_grid(n):
    return [["." for _ in range(n)] for _ in range(n)]

def show(g, reveal=False):
    print("A B C D E F")
    for i, row in enumerate(g, start=1):
        print(f"{i} " + " ".join([cell if (cell != "S" or reveal) else "." for cell in row]))

def place_ship(g, L):
    while True:
        horiz = random.choice([True, False])
        if horiz:
            r = random.randint(0, SIZE-1)
            c = random.randint(0, SIZE-L)
            if all(g[r][c+i] == "." for i in range(L)):
                for i in range(L):
                    g[r][c+i] = "S"
                return
        else:
            r = random.randint(0, SIZE-L)
            c = random.randint(0, SIZE-1)
            if all(g[r+i][c] == "." for i in range(L)):
                for i in range(L):
                    g[r+i][c] = "S"
                return

def place_fleet(g, sizes):
    for L in sizes:
        place_ship(g, L)

def parse_coord(t):
    t = t.strip().upper()
    if " " in t:
        a, b = t.split()
        if a.isdigit() and b.isdigit():
            return int(a)-1, int(b)-1
        return None
    if len(t) >= 2 and t[0].isalpha() and t[1:].isdigit():
        return int(t[1:]) - 1, ord(t[0]) - ord("A")
    return None

def shoot(g, r, c):
    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return "out"
    if g[r][c] == "S":
        g[r][c] = "X"
        return "hit"
    if g[r][c] == ".":
        g[r][c] = "o"
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
    s1 = 0
    s2 = 0
    turn = 1
    print("1v1 Console — A1 ou '2 3'. +2 hit, -1 miss, +3 bonus fin. Entrée vide: quitter.")
    while True:
        if turn == 1:
            print("\n--- Tour J1 ---")
            print("J1 (vos bateaux) :")
            show(g1, True)
            print("J2 (caché) :")
            show(g2, False)
            s = input("J1 tire: ")
            if not s.strip():
                print("Fin. J1:", s1, " J2:", s2)
                show(g1, True)
                show(g2, True)
                break
            pos = parse_coord(s)
            if pos is None:
                print("⛔ Entrée invalide, rejouez.")
                continue
            r, c = pos
            res = shoot(g2, r, c)
            if res == "hit":
                print("🎯 TOUCHE !")
                s1 += 2
                turn = 2
            elif res == "miss":
                print("💧 A L'EAU.")
                s1 -= 1
                turn = 2
            elif res == "repeat":
                print("⚠️ Déjà visé, rejouez.")
                continue
            else:
                print("⛔ Hors grille, rejouez.")
                continue
            print("Score J1:", s1)
            if all_sunk(g2):
                s1 += 3
                print("🏆 J1 gagne ! Bonus +3. J1:", s1, " J2:", s2)
                show(g1, True)
                show(g2, True)
                break
        else:
            print("\n--- Tour J2 ---")
            print("J2 (vos bateaux) :")
            show(g2, True)
            print("J1 (caché) :")
            show(g1, False)
            s = input("J2 tire: ")
            if not s.strip():
                print("Fin. J1:", s1, " J2:", s2)
                show(g1, True)
                show(g2, True)
                break
            pos = parse_coord(s)
            if pos is None:
                print("⛔ Entrée invalide, rejouez.")
                continue
            r, c = pos
            res = shoot(g1, r, c)
            if res == "hit":
                print("🎯 TOUCHE !")
                s2 += 2
                turn = 1
            elif res == "miss":
                print("💧 A L'EAU.")
                s2 -= 1
                turn = 1
            elif res == "repeat":
                print("⚠️ Déjà visé, rejouez.")
                continue
            else:
                print("⛔ Hors grille, rejouez.")
                continue
            print("Score J2:", s2)
            if all_sunk(g1):
                s2 += 3
                print("🏆 J2 gagne ! Bonus +3. J2:", s2, " J1:", s1)
                show(g1, True)
                show(g2, True)
                break

if __name__ == "__main__":
    main()
