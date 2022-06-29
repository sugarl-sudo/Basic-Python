class Dice:
    def __init__(self, surface):
        self.top = surface[0]
        self.bot = surface[5]
        self.N = surface[4]
        self.E = surface[2]
        self.S = surface[1]
        self.W = surface[3]

    def move_n(self):
        self.top, self.bot, self.N, self.S = self.S, self.N, self.top, self.bot

    def move_e(self):
        self.top, self.bot, self.E, self.W = self.W, self.E, self.top, self.bot

    def move_s(self):
        self.top, self.bot, self.N, self.S = self.N, self.S, self.bot, self.top

    def move_w(self):
        self.top, self.bot, self.E, self.W = self.E, self.W, self.bot, self.top

    def same_judge(self, dice):
        move_command = 'NNNNWNNNWNNNENNNENNNWNNN'
        flag = False
        for com in move_command:
            if com == "N":
                self.move_n()
            elif com == "E":
                self.move_e()
            elif com == "S":
                self.move_s()
            else:
                self.move_w()

            tmp_flag = True
            for i in range(6):
                if self.top != dice.top:
                    tmp_flag = False
                    break
                if self.bot != dice.bot:
                    tmp_flag = False
                    break
                if self.N != dice.N:
                    tmp_flag = False
                    break
                if self.S != dice.S:
                    tmp_flag = False
                    break
                if self.E != dice.E:
                    tmp_flag = False
                    break
                if self.W != dice.W:
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
