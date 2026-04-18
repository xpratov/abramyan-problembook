s = input("S - satrni kiriting: ")
s1 = input("S1 - satrni kiriting: ")
s2 = input("S2 - satrni kiriting: ")

if s.count(s1)==0:
  print(s)
else: 
  left_index = s.rfind(s1)
  left_substring = s[:left_index]
  result = left_substring + s2 + s[left_index+len(s1):]
  print(result)