x_l, y_l = [], []
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break

    if x > y:
        tmp = x
        x = y
        y = tmp

    x_l.append(x)
    y_l.append(y)

for x, y in zip(x_l, y_l):
    print(x, y)
