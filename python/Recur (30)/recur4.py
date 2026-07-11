count = 0

def Fib1(n):
    global count
    count += 1

    if n == 1 or n == 2:
        return 1

    return Fib1(n - 1) + Fib1(n - 2)


numbers = list(map(int, input("5 ta N kiriting: ").split()))

for n in numbers:
    count = 0          
    fib = Fib1(n)
    print(f"F({n}) = {fib}, Function calls = {count}")