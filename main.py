import random
import json

#游戏线条模型
GameLineModule = [
        [0,0,0,0,0,1],[1,1,1,1,1,2],[2,2,2,2,2,3],[3,3,3,3,3,4],[0,1,2,1,0,5],[1,2,3,2,1,6],[3,2,1,2,3,7],[2,1,0,1,2,8],[0,1,2,2,2,9],[1,2,3,3,3,10],
        [3,2,1,1,1,11],[2,1,0,0,0,12],[0,1,0,1,0,13],[1,2,1,2,1,14],[2,3,2,3,2,15],[3,2,3,2,3,16],[2,1,2,1,2,17],[1,0,1,0,1,18],[0,1,0,0,0,19],[1,2,1,1,1,20],
        [2,3,2,2,2,21],[3,2,3,3,3,22],[2,1,2,2,2,23],[1,0,1,1,1,24],[0,0,0,1,2,25],[1,1,1,2,3,26],[3,3,3,2,1,27],[2,2,2,1,0,28],[0,1,1,1,0,29],[1,2,2,2,1,30],
        [2,3,3,3,2,31],[3,2,2,2,3,32],[2,1,1,1,2,33],[1,0,0,0,1,34],[0,1,1,0,1,35],[1,2,2,1,2,36],[2,3,3,2,3,37],[3,2,3,3,2,38],[2,1,2,2,1,39],[1,0,1,1,0,40],
    ]

#特殊游戏设置
wildid = 8 #野生id

def ButterflyStaxx(bet):
    '''游戏入口'''

    Betdata = int(bet)

    #生成矩阵并返回矩阵
    Matrix = GenerateMatrix()

    if GamemMode(Matrix) == False:

        #根据矩阵判断线条模型 并插入中奖的值和不符合中奖的值 #Reward生成的中奖值
        data, RewardTypes = WriteReward(Matrix)


    #判断符合规则的线条模型 返回
    dict, RewardTypes, AllContinuousReward, AllContinuous = JudgeRewardLineModule(data,RewardTypes,Bet(Betdata))
    '''
        {"index":索引,"module":模型,"complete":完整数据,"Continuous":连接数,"RewardTypes":奖励ico类型,"ContinuousReward":连接奖励数}
    '''

    return returndata(dict, RewardTypes, AllContinuousReward, AllContinuous, Matrix)

def returndata(dict, RewardTypes, AllContinuousReward, AllContinuous, Matrix):
    return {
        "matrix":Matrix,
        "data":dict,
        "RewardTypes":RewardTypes,
        "AllContinuousReward":AllContinuousReward,
        "AllContinuous":AllContinuous
    }


def Bet(Bet):
    if Bet == 0 or Bet == 1:
        outBet = Bet + 1
    else:
        outBet = Bet
    return outBet


def GenerateReward():
    '''生成奖励'''

    AllReward = [0,1,2,3,4,5,6,7] #全部奖励值
    Reward = random.randint(0,7)  #选中的奖励值

    AllReward.remove(int(Reward)) #在全部奖励值里面剔除被选中的奖励值

    #print("中奖值:",Reward,"没中奖的值:",AllReward)
    return Reward, AllReward


def GenerateMatrix():
    '''生成矩阵'''

    list = [[],[],[],[],[]] #定义一个空列表

    #执行五次循环
    for i in range(5):

        #执行4次插入列表
        for e in range(4):

            probability = random.choice([0,1])  #概率生成值
            list[i].append([probability])       #插入数组

    return list


def WriteReward(data):
    '''写入0 或 1的奖值'''

    #获取中奖值和非中奖值(被选中的值，去除选中以后剩余的非中奖值)
    RewardTypes, FalseReward = GenerateReward()

    #循环五次取出五个数据列表
    for i in range(5):
        #print(i) #打印当前循环的列表排序

        for d in data[i]: #循环d = data[1 ~ 5]的值
            print(i," - ",d)

            if d[0] == 1:
                d.append(random.choice([RewardTypes,wildid]))    #Reward获奖值, wildid野生值
            else:
                d.append(random.choice(FalseReward))        #FalseReward非中奖值
            
    print(data)
    return data, RewardTypes


def JudgeRewardLineModule(data,Reward,Bet):
    '''判断module是否符合'''

    AllContinuousReward = 0
    AllContinuous = 0

    dict = []
    for i in range(40):
        #返回数据与模型的条件(模型标识数，模型结构，判断结果，完整数据)
        index, module, result, complete = JudgeRewardLineModule_Return_conditionResult(data,GameLineModule[i])

        #判断该数据与模型产生多少连接数
        Continuous = JudgeContinuousResult(complete)

        #返回奖励结果
        ContinuousReward = JudgeContinuousReward(Continuous, Reward)
        #print(index, module, result, complete, Continuous, Reward, ContinuousReward) #模型与数据的条件结果

        dict.append({
            "index":index,
            "module":module,
            "complete":complete,
            "ContinuousData":result,
            "Continuous":Continuous,
            "ContinuousReward":ContinuousReward,
            "BetContinuousReward": ContinuousReward * int(Bet)
        })

        AllContinuousReward = AllContinuousReward + ContinuousReward
        AllContinuous = AllContinuous + Continuous

    return dict, Reward, AllContinuousReward, AllContinuous


def JudgeRewardLineModule_Return_conditionResult(data,module):
    '''返回模型与数据的条件结果'''

    outresult = [] #设置单次判断返回结果用的数组
    out = []

    for i in range(5):

        #print("数据的第",i,"列",data[i])JudgeRewardLineModule
        #print("数据的第",i,"列","第",e,"个",data[i][e])
        #print(module[i])

        cursor = data[i][0 + module[i]] #创建数据游标
        if cursor[0] == 1: #判断module位置[1~4]的data[1~4] 是否 == 1
            outresult.append(1)
            out.append([1,cursor[1]])
        else:
            outresult.append(0)
            out.append([0,cursor[1]])

    return module[5], module, outresult, out#模型标识数，模型结构，判断结果，完整数据
            

def JudgeContinuousResult(data):
    '''判断连接数 = 1保持循环 = 0跳出循环'''
    iflist = []
    for i in data:
        iflist.append(i[0])

    if iflist[0] + iflist[1] + iflist[2] + iflist[3] + iflist[4] == 5:
        return 5

    elif iflist[0] + iflist[1] + iflist[2] + iflist[3] == 4:
        return 4

    elif iflist[0] + iflist[1] + iflist[2]  == 3:
        return 3

    else:
        return 0



def JudgeContinuousReward(continuous,types):
    '''返回奖励结果 什么类型 满足多少条件 返回多少获奖'''
    if types == 0 or types == 1 or types == 2 or types == 3 or types == 8:   #0 1 2 3
        if continuous == 3:
            return 5
        elif continuous == 4:
            return 10
        elif continuous == 5:
            return 20
        else:
            return 0

    elif types == 4 or types == 8:                #4
        if continuous == 3:
            return 15
        elif continuous == 4:
            return 30
        elif continuous == 5:
            return 60
        else:
            return 0

    elif types == 5 or types == 6 or types == 7 or types == 8:      #5 6 7 
        if continuous == 3:
            return 10
        elif continuous == 4:
            return 20
        elif continuous == 5:
            return 40
        else:
            return 0
    else:
        return 0

    
def GamemMode(data):
    '''游戏模式触发机制'''

    #判断游戏模式入口

    return False

ButterflyStaxx(0)