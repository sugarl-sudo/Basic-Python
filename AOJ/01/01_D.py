s = int(input())
a = s // (60 * 60)
b = (s - a * 60 * 60) // 60
c = (s - a * 60 * 60 - b * 60)
print(f'{a}:{b}:{c}')
