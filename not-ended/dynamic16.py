class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


values = list(map(int, input("10 ta butun son kiriting: ").split()))

head1 = tail1 = None
head2 = tail2 = None

for value in values:
    new_node = Node(value)

    if value % 2 != 0:
        if head1 is None:
            head1 = new_node
            tail1 = new_node
        else:
            tail1.next = new_node
            tail1 = new_node

    else:
        if head2 is None:
            head2 = new_node
            tail2 = new_node
        else:
            tail2.next = new_node
            tail2 = new_node

print(head1, tail1)
print(head2, tail2)