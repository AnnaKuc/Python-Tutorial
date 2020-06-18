index = 0

print("Pierwsza petla")

while index < 5:
    print(index)
    if index == 3:
        break
    index = index + 1

print("Druga petla")

while index < 10:
    print(index)
    index = index + 1
    if index == 7:
        continue
    print("Po if")

print(index)