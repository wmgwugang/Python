import random   # 引入 random 包

count = 5       # 定义最大尝试的次数
answer = random.randint(1, 15)    # 在指定范围内生成一个答案

while count > 0:
    temp = input('请输入一个数字：')
    guess = int(temp)

    if guess == answer:
        print('恭喜你，你猜对了。游戏结束了。。。')
        break
    else:
        if(guess < answer):
            print('小了')
        else:
            print('大了')
        count = count -1
else:
    print('游戏结束了')
