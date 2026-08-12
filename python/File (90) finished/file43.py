s1 = input("1-fayl nomi: ")
s = input("Matn ma'lumot kiriting: ")

with open(s1, "rb") as f:
  data = f.read()

with open(s, "wb") as f:
  f.write(data)