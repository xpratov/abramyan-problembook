n = int(input("N: "))
array = list(map(float, input(f"{n} ta son: ").split()))

wrong_index = -1
for i in range(n - 1):
    if array[i] < array[i+1]:
        if i + 2 < n and array[i] < array[i+2]:
            wrong_index = i
        else:
            wrong_index = i + 1
        break

if wrong_index != -1:
    element = array.pop(wrong_index)
    placed = False

    for i in range(len(array)):
        if array[i] < element:
            array.insert(i, element)
            placed = True
            break

    if not placed:
        array.append(element)

print(array)