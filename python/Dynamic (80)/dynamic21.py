class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def dynamic21(P1, P2, P3, P4):
    if P1 is None:
        return P3, P4

    if P3 is None:
        P3 = P1
        P4 = P2
    else:
        P4.next = P1
        P4 = P2

    return P3, P4