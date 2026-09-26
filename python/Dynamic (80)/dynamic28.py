class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class TQueue:
    def __init__(self, head=None, tail=None):
        self.Head = head
        self.Tail = tail


def Dequeue(Q):
    value = Q.Head.data

    old_head = Q.Head
    Q.Head = Q.Head.next

    if Q.Head is None:
        Q.Tail = None

    del old_head

    return value


def QueueIsEmpty(Q):
    return Q.Head is None


N = int(input())
numbers = list(map(int, input().split()))

Q = TQueue()

for value in numbers:
    new_node = Node(value)

    if Q.Head is None:
        Q.Head = new_node
        Q.Tail = new_node
    else:
        Q.Tail.next = new_node
        Q.Tail = new_node


count = min(5, N)

for _ in range(count):
    print(Dequeue(Q))


print(QueueIsEmpty(Q))


if QueueIsEmpty(Q):
    print("nil")
    print("nil")
else:
    print(id(Q.Head))
    print(id(Q.Tail))