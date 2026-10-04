class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None
        self.Prev = None


class TList:
    def __init__(self, first=None, last=None, current=None):
        self.First = first
        self.Last = last
        self.Current = current


def InsertFirst(L, D):
    new_node = Node(D)

    if L.First is None:
        L.First = new_node
        L.Last = new_node

    else:
        new_node.Next = L.First
        L.First.Prev = new_node
        L.First = new_node

    L.Current = new_node


P1 = Node(10)
P1.Next = Node(20)
P1.Next.Prev = P1
P1.Next.Next = Node(30)
P1.Next.Next.Prev = P1.Next

P2 = P1.Next.Next
P3 = P1.Next

L = TList(P1, P2, P3)

N = 3
A = [40, 50, 60]

for x in A:
    InsertFirst(L, x)

print(L.First.Data)
print(L.Last.Data)
print(L.Current.Data)