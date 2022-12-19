from random import randint
import time,sys

# 玩家
class Player:

    def __init__(self,stoneNumber):
        self.stoneNumber = stoneNumber # 灵石数量
        self.warriors = {}  # 拥有的战士，包括弓箭兵和斧头兵

# 鹰妖
class Eagle():
    typeName = '鹰妖'

# 狼妖
class Wolf():
    typeName = '狼妖'


# 战士
class Warrior:

    # 初始化参数是生命值
    def __init__(self, strength):
        self.strength = strength

    # 用灵石疗伤
    def healing(self, stoneCount):
        # 如果已经到达最大生命值，灵石不起作用，浪费了
        if self.strength == self.maxStrength:
            return

        self.strength += stoneCount

        # 不能超过最大生命值
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength


# 弓箭兵 是 战士的子类
class Archer(Warrior):
    # 种类名称
    typeName = '弓箭兵'

    # 雇佣价 100灵石，属于静态属性
    price = 100

    # 最大生命值 ，属于静态属性
    maxStrength = 100


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 20
        elif monster.typeName== '狼妖':
            self.strength -= 80
        else:
            print('未知类型的妖怪！！！')



# 斧头兵 是 战士的子类
class Axeman(Warrior):
    # 种类名称
    typeName = '斧头兵'

    # 雇佣价 120灵石
    price = 120

    # 最大生命值
    maxStrength = 120


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 80
        elif monster.typeName== '狼妖':
            self.strength -= 20
        else:
            print('未知类型的妖怪！！！')



# 森林
class Forest():
    def __init__(self,monster):
        # 该森林里面的妖怪
        self.monster = monster

def hirworrior(arrow_num,axe_num,player):
    for i in range(1,int(arrow_num )+ 1):
        arrow_name  = f'arrow{i}'
        player.warriors[arrow_name] = Archer(arrow_name)
        player.stoneNumber -= 100

    for j in range(1,int(axe_num) + 1):
        axe_name = f'axe{j}'
        player.warriors[axe_name] = Axeman(axe_name)
        player.stoneNumber -= 120 


print('''
***************************************
****           游戏开始             ****
***************************************

'''
)

# 森林数量
forest_num = 7

# 森林 列表
forestList = []

# 为每座森林随机产生 鹰妖或者 狼妖
notification = '前方森林里的妖怪是：'  # 显示在屏幕上的内容
for i in range(forest_num):
    typeName = randint(0,1)
    if typeName == 0:
        forestList.append( Forest(Eagle()) )
    else:
        forestList.append( Forest(Wolf()) )

    notification += \
         f'第{i+1}座森林里面是 {forestList[i].monster.typeName}  '

# 显示 妖怪信息
print(notification,'\n')
for i in range(1,15):
    time.sleep(1)
    print('\n')




player = Player(1000)
 #购买士兵
while True:
    print('现在你有1000颗灵石，请根据需要购买士兵\n弓箭兵雇佣价： 100灵石  最大生命值： 100\n杀死鹰妖损耗生命值20\n杀死狼妖损耗生命值80\n斧头兵雇佣价： 120灵石  最大生命值： 120\n杀死鹰妖损耗生命值80\n杀死狼妖损耗生命值20\n')
    arrow_num = (input('请输入需要雇佣的弓箭兵数量：'))
    axe_num = (input('请输入需要雇佣的斧头兵数量：'))
    if int(player.stoneNumber) - (100 * int(arrow_num) + 120 * int(axe_num)) < 0:
        print('对不起，你的灵石不足以购买这些士兵，请重新输入')
        continue
    else:
        hirworrior(arrow_num,axe_num,player)
        break

pass_forest = 0
for round in range(forest_num):
    #没有可用士兵，退出
    if not player.warriors:
        break
    while True:
        w_name = input(f'当前为第{round+1}座森林，请输入你要派遣的士兵的名字{player.warriors.keys()}:')
        w = player.warriors[w_name]
        w.fightWithMonster(forestList[round].monster.typeName)
        print(w.strength)
        if w.strength > 0:
            print(f'第{round + 1}座森林通过')
            pass_forest +=  1
            if player.stoneNumber > 0:
                stoneCount = input('是否给士兵补充灵石？若需要则输入补充个数，不需要则输入0：')
                if stoneCount.isdigit() and int(stoneCount) < player.stoneNumber:
                    w.healing(int(stoneCount))
                    player.stoneNumber -= int(stoneCount)
                else:
                    print('输入灵石个数超范围或格式错误')
            else:
                print('灵石不足，无法给士兵补给！')
            break
        elif w.strength == 0:
            print(f'第{round + 1}座森林通过，但是所派出的士兵已死')
            del w
            break
        else:
            del w 
            continue

if pass_forest == 7 and player.stoneNumber > 0:
    print('通关！')
