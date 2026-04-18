s = input("Satrni kiriting: ")

stack = []
pairs = {')': '(', ']': '[', '}': '{'}
error_pos = 0

for i in range(len(s)):
    char = s[i]
    
    if char in '([{':
        stack.append(char)
    
    elif char in ')]}':
        if not stack or stack[-1] != pairs[char]:
            error_pos = i + 1
            break
        else:
            stack.pop()

if error_pos != 0:
    print(error_pos)
elif stack:
    print(-1)
else:
    print(0)