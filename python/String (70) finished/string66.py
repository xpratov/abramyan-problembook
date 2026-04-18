s = input("Satrni kiriting: ")

even_pos = s[1::2]

odd_pos = s[::2]

odd_pos_reversed = odd_pos[::-1]

result = even_pos + odd_pos_reversed

print("Shifrlangan matn:", result)