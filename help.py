from funkcje import *

x=0
y=1
gdzie = '0'
rom = []
mapa(rom)
while(True):
    ulozenie(x, y, rom)
    wyswietl(rom)
    gdzie = input("Ktoredy ? :")
    rom[y][x] = "O"
    x = ruchx(x, gdzie)
    y = ruchy(y, gdzie)


