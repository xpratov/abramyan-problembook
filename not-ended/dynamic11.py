class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class TStack:
  def __init__(self, top=None):
    self.top = top

def Push(D, S):
  new_node = Node(D, S.top)
  S.top = new_node

P1 = None
S = TStack(P1)

N = int(input("N - butun sonini kiriting: "))
numbers = list(map(int, input().split()))

for i in numbers: 
  Push(i, S)

print(id(S.top))