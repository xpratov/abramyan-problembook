s = input("S - satrni kiriting: ")

if s.count()==1:
  print("")
else:
  first_index = s.find(" ")
  second_index = s.find(" ", first_index)
  print(s[first_index, second_index])