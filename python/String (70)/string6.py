c = input("C - belgisini kiriting: ")

if c.islower():
  print("small")
elif c.isupper():
  print("capital")
elif c.isdigit():
  print("digit")