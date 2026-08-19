class Node: 
  def __init__(self, data, next=None):
    self.Data = data
    self.Next = next

P1 = Node(1)
P1.Next  = Node(2)
P1.Next.Next = Node(3)
P1.Next.Next.Next = Node(4)

p = P1
length = 0

while p is not None:
  print(p.Data)
  length +=1
  p = p.Next
print("Length: ", length)

last = P1
while last.Next is not None:
  last = last.Next

print("Last: ", last.Data)
