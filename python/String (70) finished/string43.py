s = input("Matn kiriting: ")

words = s.split()
count = 0

for word in words:
  if word.count("E"):
    count +=1

print(count)