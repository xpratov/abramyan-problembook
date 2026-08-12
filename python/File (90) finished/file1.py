def create_file(s):
  try:
    with open(s, "x"):
      pass
    return True
  except:
    return False

s = input("File nomini kiriting: ")
print(create_file(s))