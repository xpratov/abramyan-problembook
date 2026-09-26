class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def dynamic22(N, P1, P2, P3, P4):
    count = 0

    while P1 is not None and count < N:
        current = P1

        P1 = P1.next

        current.next = None
        P4.next = current
        P4 = current

        count += 1

    if P1 is None:
        P2 = None

    return P1, P2, P3, P4