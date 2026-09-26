class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def dynamic24(P1, P2, P3, P4):

    new_head = P1

    P1 = P1.next

    new_tail = new_head

    while P1 is not None:

        current1 = P1
        P1 = P1.next

        current2 = P3
        P3 = P3.next

        new_tail.next = current1
        new_tail = current1

        new_tail.next = current2
        new_tail = current2

    return new_head, new_tail