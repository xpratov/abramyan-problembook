class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def dynamic23(P1, P2, P3, P4):

    while P1 is not None and P1.value % 2 != 0:
        
        current = P1

        P1 = P1.next

        current.next = None
        P4.next = current
        P4 = current

    if P1 is None:
        P2 = None

    return P1, P2, P3, P4