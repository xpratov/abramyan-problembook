path = input("To'liq fayl manzilini kiriting: ")

parts = path.split('\\')

if len(parts) > 2:
    last_directory = parts[-2]
    if last_directory == "":
        print("\\")
    else:
        print(last_directory)
else:
    print("\\")