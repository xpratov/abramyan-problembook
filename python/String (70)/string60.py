s = input("To'liq yo'lni kiriting: ")

first_slash = s.find("\\")
second_slash = s.find("\\", first_slash + 1)

if second_slash != -1:
    first_dir = s[first_slash + 1 : second_slash]
    print(first_dir)
else:
    print("\\")