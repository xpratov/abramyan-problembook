class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


D = int(input("D = "))

values = list(map(int, input("Queue elementlarini kiriting: ").split()))

P1 = P2 = None

for value in values:
    new_node = Node(value)

    if P1 is None:
        P1 = P2 = new_node
    else:
        P2.next = new_node
        P2 = new_node


new_node = Node(D)

if P1 is None:
    P1 = P2 = new_node
else:
    P2.next = new_node
    P2 = new_node


print("Head:", P1)
print("Tail:", P2)