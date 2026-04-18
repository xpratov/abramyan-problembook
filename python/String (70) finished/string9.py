n = int(input("N - juft sonini kiriting: "))
c1, c2 = map(str, input("C1, C2 - harflarni kiriting: ").split())

result = ""
for i in range(n//2):
  result += c1
  result += c2

print(result)