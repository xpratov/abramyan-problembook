class Node:
    def __init__(self, value):
        self.Data = value
        self.Next = None


def dynamic25(P1, P2, P3, P4):

    if P1.Data <= P3.Data:
        new_head = P1
        P1 = P1.Next
    else:
        new_head = P3
        P3 = P3.Next

    new_tail = new_head

    while P1 is not None and P3 is not None:

        if P1.Data <= P3.Data:
            new_tail.Next = P1
            new_tail = P1
            P1 = P1.Next
        else:
            new_tail.Next = P3
            new_tail = P3
            P3 = P3.Next

    if P1 is not None:
        new_tail.Next = P1
        new_tail = P2

    elif P3 is not None:
        new_tail.Next = P3
        new_tail = P4

    return new_head, new_tail