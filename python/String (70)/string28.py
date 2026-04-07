c = input("C - belgini kiriting: ")
s = input("S - satrini kiriting: ")

result = ""

for i in s:
  if i==c:
    result += 2*i
  else:
    result += i

print(result)