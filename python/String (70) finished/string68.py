s = input("Satrni kiriting: ")

last_letter = ""  
error_pos = 0     

for i in range(len(s)):
    char = s[i]
    
    if 'a' <= char <= 'z':
        if last_letter == "":
            last_letter = char
        else:
            if char < last_letter:
                error_pos = i + 1  
                break
            else:
                last_letter = char

print(error_pos)