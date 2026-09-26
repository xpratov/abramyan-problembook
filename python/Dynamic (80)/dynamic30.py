class Node:
  def __init__(self, data):
    self.Data = data
    self.Next = None
    self.Prev = None
  

current = P1
previous = None

while current is not None:
  current.Prev = previous
  previous = current
  current = current.Next

P_last = previous

print(id(P_last))