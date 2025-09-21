SIZE = 6  

def make_grid(n):
    return [["." for _ in range(n)] for _ in range(n)]

def show(grid, reveal=False):
    print("  A B C D E F")
    for i, row in enumerate(grid, start=1):
        print(f"{i} " + " ".join(row))

def main():
    g = make_grid(SIZE)
    show(g)

if __name__ == "__main__":
    main()
