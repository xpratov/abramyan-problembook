s = input("Matn kiriting: ")
vowels = "aieouAIEOU"
count = 0

for char in s:
    if char in vowels:
        count += 1

print("Unlilar soni:", count)