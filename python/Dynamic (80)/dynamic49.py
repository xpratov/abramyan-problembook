class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


P1 = Node(10)
P2 = Node(20)
P3 = Node(30)
P4 = Node(40)
P5 = Node(50)
P6 = Node(60)

P1.next = P2

P2.prev = P1
P2.next = P3

P3.prev = P2
P3.next = P4

P4.prev = P3
P4.next = P5

P5.prev = P4
P5.next = P6

P6.prev = P5



P = P1
first_even = None
last_even = None
first_odd = None
last_odd = None

order = 1

while P is not None:
    next_node = P.next

    if order % 2 == 0:
        P.prev = last_even

        if last_even is not None:
            last_even.next = P
        else:
            first_even = P

        last_even = P

    else:
        P.prev = last_odd

        if last_odd is not None:
            last_odd.next = P
        else:
            first_odd = P

        last_odd = P

    P = next_node
    order += 1



if last_even is not None:
    last_even.next = first_odd

if first_odd is not None:
    first_odd.prev = last_even

if last_odd is not None:
    last_odd.next = None


P1 = first_even if first_even is not None else first_odd


P = P1

while P is not None:
    print(P.data, end=" ")
    P = P.next