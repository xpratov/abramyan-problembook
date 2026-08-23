class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


N = int(input("N = "))
values = list(map(int, input("Queue qiymatlarini kiriting: ").split()))

head = tail = None

for value in values:
    new_node = Node(value)

    if head is None:
        head = tail = new_node
    else:
        tail.next = new_node
        tail = new_node


count = 0

while head is not None and count < N:
    removed_node = head
    print(removed_node.data)

    head = head.next
    del removed_node

    count += 1


if head is None:
    tail = None


print("Head:", head)
print("Tail:", tail)