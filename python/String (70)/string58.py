s = input("Matn kiriting: ")

slash = s.rfind("/")
dot = s.rfind('.')

file_name = s[slash+1:dot]

print(file_name)