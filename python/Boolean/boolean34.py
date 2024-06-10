x, y = map(int, input("Shaxmat doskasidagi istalgan katakning kordinatasini kiriting (x, y): ").split())

print(f"{x, y} katak oq rangda?")
if x%2==1 and y%2==1 or x%2==0 and y%2==0:
  print(False)
else:
  print(True)