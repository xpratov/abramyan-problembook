s = input("Satr kiriting: ")

count = 0
for i in s: 
  if i.isupper() or i.islower():
    count+=1

print(count)