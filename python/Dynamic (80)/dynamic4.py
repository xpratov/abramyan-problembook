class Node:
  def __init__(self, data, next = None):
    self.Data = data
    self.Next = next

N = int(input("N - butun sonini kiriting: "))
numbers = list(map(int, input(f"{N} ta butun son kiriting: " ).split()))

P1 = Node(numbers[0])
for i in range(1, N):
  P2 = Node(numbers[i])
  P2.Next = P1
  P1 = P2

print(P1.Data)

