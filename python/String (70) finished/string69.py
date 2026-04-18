s = input("Satrni kiriting: ")

balance = 0
error_pos = 0

for i in range(len(s)):
    char = s[i]
    
    if char == '(':
        balance += 1
    elif char == ')':
        if balance == 0:
            error_pos = i + 1
            break
        else:
            balance -= 1

if error_pos != 0:
    print(error_pos)
elif balance > 0:
    print(-1)
else:
    print(0)