class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class TStack:
    def __init__(self, top=None):
        self.top = top


def Push(D, S):
    new_node = Node(D, S.top)
    S.top = new_node


def Pop(S):
    value = S.top.data
    S.top = S.top.next
    return value


P1 = None

S = TStack(P1)

N = int(input())
numbers = list(map(int, input().split()))

for i in numbers:
    Push(i, S)

for _ in range(5):
    print(Pop(S))

if S.top is None:
    print("nil")
else:
    print(id(S.top))