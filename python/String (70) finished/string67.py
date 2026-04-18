s = input("Shifrlangan matnni kiriting: ")
n = len(s)

mid = n // 2
even_part = s[:mid]
odd_part_rev = s[mid:]     

odd_part = odd_part_rev[::-1]

result = ""
for i in range(len(odd_part)):
    result += odd_part[i]  
    if i < len(even_part):
        result += even_part[i] 

print("Deshifrlangan matn:", result)