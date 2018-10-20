def mapa(rom):
    for i in range(0, 8):
        rom.append(["O"] * 8)

def wyswietl(rom):
    for i in rom:
        print(" ".join(i))

def ulozenie(x, y, rom):
    rom[y][x] = "X"
    return rom

def ruchx(x, gdzie):
    if gdzie == "f":
        return x+1
    elif gdzie == "s":
        return x-1
    else:
        return x
def ruchy(y, gdzie):
    if gdzie == "e":
        return y-1
    elif gdzie == "d":
        return y+1
    else:
        return y