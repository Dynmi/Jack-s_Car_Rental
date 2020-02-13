'''
policy iteration for jack's car rental

author@dynmiWang 

'''
import math

A      = [[0 - i, i] for i in range(-5, 6)]
Gain_1 = []
Gain_2 = []

def get_prob(n, lamda):
    #获取lamda泊松分布下为n的概率
    res = 1.0 /pow(math.e,lamda) * pow(lamda,n)
    for i in range(n):
        res = res / i
    return res


# 对于租车点1，计算每个状态下的收获期望
for x in range(21):
    #早晨x辆车  晚上y辆车
    sum = 0
    for y in range(21):
        g     = 0
        prob_ = 0
        for p in range(x, 20):
            #p out ; 20-p in
            g = g +10 * p * ( get_prob(p,3) * get_prob(20-p,3) )
            prob = prob + get_prob(p,3)*get_prob(20-p,3)
        sum = sum + g/prob
    Gain_1.append(sum)


# 对于租车点2，计算每个状态下的收获期望
for x in range(21):
    #早晨x辆车  晚上y辆车
    sum = 0
    for y in range(21):
        g     = 0
        prob_ = 0
        for p in range(x, x-y):
            #p out ; 20-p in
            g    = g +10 * p * ( get_prob(p,4) * get_prob(20-p,2) )
            prob = prob + get_prob(p,4)*get_prob(20-p,2)
            g    = g/prob
        sum = sum + g 
    Gain_2.append(sum)


def get_Q(S, a):
    
    

def policy_evaluation() -> None:
    while True:
        Action_prob = []
        for a in Action_prob:
            q     = get_Q(S, a)
            V[][] = get_Q(S,a)



def policy_improvement() -> None:
    