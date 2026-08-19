class Node:
    def __init__(self, data, next=None):
        self.Data = data
        self.Next = next


P1 = Node(10)
P1.Next = Node(7)
P1.Next.Next = Node(4)
P1.Next.Next.Next = Node(9)
P1.Next.Next.Next.Next = Node(6)


P_even = None
P_odd = None


while P1 is not None:

    temp = P1.Next

    if P1.Data % 2 == 0:
        P1.Next = P_even
        P_even = P1
    else:
        P1.Next = P_odd
        P_odd = P1

    P1 = temp


print("Even top:", P_even.Data if P_even is not None else None)
print("Odd top:", P_odd.Data if P_odd is not None else None)