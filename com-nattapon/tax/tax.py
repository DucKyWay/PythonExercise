list = [0, 0, 0, 0]
i, j = 0

for i in range(4):
    list[i] = int(input(i, ': '))
    i += 1

for j in range(4):
    print(i, "=", list[i])
    i += 1