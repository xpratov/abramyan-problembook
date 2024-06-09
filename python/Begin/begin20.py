x1, y1 = map(int, input("A nuqtaning kordinatalarini kiriting: ").split())
x2, y2 = map(int, input("B nuqtaning kordinatalarini kiriting: ").split())

distance = ((x2-x1)**2+(y2-y1)**2)**(1/2)
print("Nuqtalar orasidagi masofa: ", distance)