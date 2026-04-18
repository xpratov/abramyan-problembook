s = input("S - satrni kiriting: ")

if s.count()==1:
  print("")
else:
  first_index = s.find(" ")
  last_index = s.rfind(" ")
  print(s[first_index, last_index])