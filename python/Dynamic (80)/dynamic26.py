class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class TQueue:
    def __init__(self, head=None, tail=None):
        self.Head = head
        self.Tail = tail


def Enqueue(Q, D):
    new_node = Node(D)

    if Q.Head is None:
        Q.Head = new_node
        Q.Tail = new_node
    else:
        Q.Tail.next = new_node
        Q.Tail = new_node


N = int(input())
P1, P2 = None, None

Q = TQueue(P1, P2)

numbers = list(map(int, input().split()))

for D in numbers[:N]:
    Enqueue(Q, D)

print(id(Q.Head))
print(id(Q.Tail))