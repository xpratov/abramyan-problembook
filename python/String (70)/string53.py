s = input("Matn kiriting: ")
punctuations = ".,!?;:-()\"'"
count = 0

for char in s:
    if char in punctuations:
        count += 1

print("Tinish belgilari soni:", count)