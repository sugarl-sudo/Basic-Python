class Dice:
    def __init__(self, surfaces):
        self.sur = [0] * 6
        for i in range(6):
            self.sur[i] = surfaces[i]

    def move(self, command):
        if command == "N":
            self.sur[0], self.sur[5], self.sur[4], self.sur[1] = self.sur[1], self.sur[4], self.sur[0], self.sur[5]
        elif command == "E":
            self.sur[0], self.sur[5], self.sur[2], self.sur[3] = self.sur[3], self.sur[2], self.sur[0], self.sur[5]
        elif command == "S":
            self.sur[0], self.sur[5], self.sur[4], self.sur[1] = self.sur[4], self.sur[1], self.sur[5], self.sur[0]
        else:
            self.sur[0], self.sur[5], self.sur[2], self.sur[3] = self.sur[2], self.sur[3], self.sur[5], self.sur[0]

    def same_judge(self, dice):
        move_command = 'NNNNWNNNWNNNENNNENNNWNNN'
        flag = False
        for com in move_command:
            self.move(com)
            tmp_flag = True
            for i in range(6):
                if self.sur[i] != dice.sur[i]:
                    tmp_flag = False
                    break

            if tmp_flag:
                return True

        return flag


n = int(input())
dice_list = [Dice(list(map(int, input().split()))) for _ in range(n)]
flag = True
for i in range(n - 1):
    for j in range(i + 1, n):
        dice_1 = dice_list[i]
        dice_2 = dice_list[j]
        if dice_1.same_judge(dice_2):
            flag = False
            break

if flag:
    print("Yes")
else:
    print("No")
