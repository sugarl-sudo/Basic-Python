n = int(input())
in_datas = [list(map(int, input().split())) for _ in range(n)]
all_info = [[' '] * 20] * 15
for count in range(1, 16):
    if count % 4 == 0:
        all_info[count - 1] = ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    else:
        for p_count in range(1, 21):
            if p_count % 2 == 0:
                all_info[count - 1][p_count - 1] = "0"

for in_data in in_datas:
    i = 4 * (in_data[0] - 1) + (in_data[1] - 1)
    j = 2 * in_data[2] - 1
    all_info[i][j] = str(in_data[3] + int(all_info[i][j]))

for info in all_info:
    print(*info)
