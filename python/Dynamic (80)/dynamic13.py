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


def StackIsEmpty(S):
    return S.top is None


def Peek(S):
    return S.top.data


P1 = None
S = TStack(P1)

N = int(input())
numbers = list(map(int, input().split()))

for i in numbers:
    Push(i, S)


count = 0

while count < 5 and not StackIsEmpty(S):
    print(Pop(S))
    count += 1


print(StackIsEmpty(S))


if not StackIsEmpty(S):
    print(Peek(S))
    print(id(S.top))