# battleship.py

import random
SIZE = 6

def make_grid(n): 
    return [["." for _ in range(n)] for _ in range(n)]
def show(g, reveal=False):
    print("A B C D E F")
    for i, row in enumerate(g, start=1):
        vis = [c if (c != "S" or reveal) else "." for c in row]
        print(f"{i} " + " ".join(vis))

def place_ship_horiz(g, L):
    while True:
        r = random.randint(0, SIZE-1)
        c = random.randint(0, SIZE-L)  # ✅ borne OK
        if all(g[r][c+i] == "." for i in range(L)):
            for i in range(L): g[r][c+i] = "S"
            break

def place_fleet(g, sizes):
    for L in sizes: place_ship_horiz(g, L)

def parse_coord(t):
    t=t.strip().upper()
    if " " in t:
        a,b=t.split()
        if a.isdigit() and b.isdigit(): 
            return int(a)-1,int(b)-1
    return int(t[1:])-1, ord(t[0])-ord("A")

def shoot(g,r,c):
    if not (0<=r<SIZE and 0<=c<SIZE): 
        return "out"
    if g[r][c]=="S": 
        g[r][c]="X"; 
        return "hit"
    if g[r][c]==".": 
        g[r][c]="o"; 
        return "miss"
    return "repeat"

def all_sunk(g): 
    return all(cell!="S" for row in g for cell in row)

def main():
    g = make_grid(SIZE)
    place_fleet(g, [3,2,1])
    print("Flotte: 3,2,1 (anti-overlap).")
    show(g)
    score = 0
    while True:
        if all_sunk(g): 
            score+=3; 
            print("Victoire ! Score:",score); 
            show(g,True); break
        s=input("Tir: ")
        if not s.strip(): 
            print("Fin. Score:",score); 
            show(g,True); 
            break
        r,c=parse_coord(s)
        res=shoot(g,r,c)
        if res=="hit": 
            score+=2
        elif res=="miss": 
            score-=1
        print("Score:",score); 
        show(g)

if __name__ == "__main__":
    main()
