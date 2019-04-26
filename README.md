# ButterflyStaxx-GameCore
Butterfly Staxx 是国外的博彩类游戏 通过python语言还原游戏核心逻辑(仅供参考)
<br>
查看游戏核心文件 [GameCore](https://github.com/ShenVi/ButterflyStaxx-GameCore/blob/master/main.py)

## 模块介绍
模块名 | 作用
------|------------
**ButterflyStaxx()** | 游戏逻辑执行入口 
GenerateMatrix() | 随机矩阵生成
**returndata()** | 格式化输出
**GenerateReward()** | 生成随机奖励
WriteReward() | 对生成的矩阵插入随机值和获奖值变成二维数组
JudgeRewardLineModule() | 数据与模型的判断器
JudgeRewardLineModule_Return_conditionResult | 返回模型与数据的条件结果(模型标识数，模型结构，判断结果，完整数据)
JudgeContinuousResult() | 判断连接数
JudgeContinuousReward() | 返回奖励结果
GamemMode() | 多游戏模式判断入口

## Json Api
```javascript
{
    "data": [
        {"index": 1, "module": [0, 0, 0, 0, 0, 1], "complete": [[0, 1], [0, 6], [1, 5], [0, 0], [1, 5]], "Continuous": 0, "ContinuousReward": 0},
        {"index": 2, "module": [1, 1, 1, 1, 1, 2], "complete": [[1, 5], [0, 2], [1, 8], [0, 6], [0, 1]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 3, "module": [2, 2, 2, 2, 2, 3], "complete": [[1, 8], [0, 1], [0, 7], [1, 5], [1, 8]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 4, "module": [3, 3, 3, 3, 3, 4], "complete": [[1, 8], [1, 5], [0, 1], [0, 6], [1, 8]], "Continuous": 2, "ContinuousReward": 0},
        {"index": 5, "module": [0, 1, 2, 1, 0, 5], "complete": [[0, 1], [0, 2], [0, 7], [0, 6], [1, 5]], "Continuous": 0, "ContinuousReward": 0},
        {"index": 6, "module": [1, 2, 3, 2, 1, 6], "complete": [[1, 5], [0, 1], [0, 1], [1, 5], [0, 1]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 7, "module": [3, 2, 1, 2, 3, 7], "complete": [[1, 8], [0, 1], [1, 8], [1, 5], [1, 8]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 8, "module": [2, 1, 0, 1, 2, 8], "complete": [[1, 8], [0, 2], [1, 5], [0, 6], [1, 8]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 9, "module": [0, 1, 2, 2, 2, 9], "complete": [[0, 1], [0, 2], [0, 7], [1, 5], [1, 8]], "Continuous": 0, "ContinuousReward": 0},
        {"index": 10, "module": [1, 2, 3, 3, 3, 10], "complete": [[1, 5], [0, 1], [0, 1], [0, 6], [1, 8]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 11, "module": [3, 2, 1, 1, 1, 11], "complete": [[1, 8], [0, 1], [1, 8], [0, 6], [0, 1]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 12, "module": [2, 1, 0, 0, 0, 12], "complete": [[1, 8], [0, 2], [1, 5], [0, 0], [1, 5]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 13, "module": [0, 1, 0, 1, 0, 13], "complete": [[0, 1], [0, 2], [1, 5], [0, 6], [1, 5]], "Continuous": 0, "ContinuousReward": 0},
        {"index": 14, "module": [1, 2, 1, 2, 1, 14], "complete": [[1, 5], [0, 1], [1, 8], [1, 5], [0, 1]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 15, "module": [2, 3, 2, 3, 2, 15], "complete": [[1, 8], [1, 5], [0, 7], [0, 6], [1, 8]], "Continuous": 2, "ContinuousReward": 0},
        {"index": 16, "module": [3, 2, 3, 2, 3, 16], "complete": [[1, 8], [0, 1], [0, 1], [1, 5], [1, 8]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 17, "module": [2, 1, 2, 1, 2, 17], "complete": [[1, 8], [0, 2], [0, 7], [0, 6], [1, 8]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 18, "module": [1, 0, 1, 0, 1, 18], "complete": [[1, 5], [0, 6], [1, 8], [0, 0], [0, 1]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 19, "module": [0, 1, 0, 0, 0, 19], "complete": [[0, 1], [0, 2], [1, 5], [0, 0], [1, 5]], "Continuous": 0, "ContinuousReward": 0},
        {"index": 20, "module": [1, 2, 1, 1, 1, 20], "complete": [[1, 5], [0, 1], [1, 8], [0, 6], [0, 1]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 21, "module": [2, 3, 2, 2, 2, 21], "complete": [[1, 8], [1, 5], [0, 7], [1, 5], [1, 8]], "Continuous": 2, "ContinuousReward": 0},
        {"index": 22, "module": [3, 2, 3, 3, 3, 22], "complete": [[1, 8], [0, 1], [0, 1], [0, 6], [1, 8]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 23, "module": [2, 1, 2, 2, 2, 23], "complete": [[1, 8], [0, 2], [0, 7], [1, 5], [1, 8]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 24, "module": [1, 0, 1, 1, 1, 24], "complete": [[1, 5], [0, 6], [1, 8], [0, 6], [0, 1]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 25, "module": [0, 0, 0, 1, 2, 25], "complete": [[0, 1], [0, 6], [1, 5], [0, 6], [1, 8]], "Continuous": 0, "ContinuousReward": 0},
        {"index": 26, "module": [1, 1, 1, 2, 3, 26], "complete": [[1, 5], [0, 2], [1, 8], [1, 5], [1, 8]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 27, "module": [3, 3, 3, 2, 1, 27], "complete": [[1, 8], [1, 5], [0, 1], [1, 5], [0, 1]], "Continuous": 2, "ContinuousReward": 0},
        {"index": 28, "module": [2, 2, 2, 1, 0, 28], "complete": [[1, 8], [0, 1], [0, 7], [0, 6], [1, 5]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 29, "module": [0, 1, 1, 1, 0, 29], "complete": [[0, 1], [0, 2], [1, 8], [0, 6], [1, 5]], "Continuous": 0, "ContinuousReward": 0},
        {"index": 30, "module": [1, 2, 2, 2, 1, 30], "complete": [[1, 5], [0, 1], [0, 7], [1, 5], [0, 1]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 31, "module": [2, 3, 3, 3, 2, 31], "complete": [[1, 8], [1, 5], [0, 1], [0, 6], [1, 8]], "Continuous": 2, "ContinuousReward": 0},
        {"index": 32, "module": [3, 2, 2, 2, 3, 32], "complete": [[1, 8], [0, 1], [0, 7], [1, 5], [1, 8]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 33, "module": [2, 1, 1, 1, 2, 33], "complete": [[1, 8], [0, 2], [1, 8], [0, 6], [1, 8]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 34, "module": [1, 0, 0, 0, 1, 34], "complete": [[1, 5], [0, 6], [1, 5], [0, 0], [0, 1]], "Continuous":1, "ContinuousReward": 0},
        {"index": 35, "module": [0, 1, 1, 0, 1, 35], "complete": [[0, 1], [0, 2], [1, 8], [0, 0], [0, 1]], "Continuous": 0, "ContinuousReward": 0},
        {"index": 36, "module": [1, 2, 2, 1, 2, 36], "complete": [[1, 5], [0, 1], [0, 7], [0, 6], [1, 8]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 37, "module": [2, 3, 3, 2, 3, 37], "complete": [[1, 8], [1, 5], [0, 1], [1, 5], [1, 8]], "Continuous": 2, "ContinuousReward": 0},
        {"index": 38, "module": [3, 2, 3, 3, 2, 38], "complete": [[1, 8], [0, 1], [0, 1], [0, 6], [1, 8]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 39, "module": [2, 1, 2, 2, 1, 39], "complete": [[1, 8], [0, 2], [0, 7], [1, 5], [0, 1]], "Continuous": 1, "ContinuousReward": 0},
        {"index": 40, "module": [1, 0, 1, 1, 0, 40], "complete": [[1, 5], [0, 6], [1, 8], [0, 6], [1, 5]], "Continuous": 1, "ContinuousReward": 0}
    ], 
    "RewardTypes": 5,
    "AllContinuousReward": 0,
    "AllContinuous": 38
}
```