'''
policy iteration for jack's car rental

author@dynmiWang 

'''
import numpy as np
import matplotlib.pyplot as plt


A      = [[0 - i, i] for i in range(-5, 6)]
State  = [ [a,b] for a in range(21) for b in range(21) ] 
V      = [ [0 for i in range(21)] for j in range(21) ]
policy = [ [[] for i in range(21)] for j in range(21) ]
Gain_1 = []
Gain_2 = []
gamma  = 0.9

def get_prob(n, lamda):
    #获取lamda泊松分布下为n的概率
    res = 1.0 /pow(math.e,lamda) * pow(lamda,n)
    for i in range(1,n):
        res = res / i
    return res


# 对于租车点1，计算每个状态下的收获期望
for x in range(21):
    #早晨x辆车  晚上y辆车
    sum = 0
    for y in range(21):
        g = 0
        for p in range(max(0,x-y), min(20,20+x-y)):
            #p rent ; y-x+p return
            g    = g +10 * p * ( get_prob(p,3) * get_prob(y-x+p,3) )
        sum = sum + g 
    Gain_1.append(sum)


# 对于租车点2，计算每个状态下的收获期望
for x in range(21):
    #早晨x辆车  晚上y辆车
    sum = 0
    for y in range(21):
        g = 0
        for p in range(max(0,x-y), min(20,20+x-y)):
            #p rent ; y-x+p return
            g    = g +10 * p * ( get_prob(p,4) * get_prob(y-x+p,2) )
        sum = sum + g 
    Gain_2.append(sum)
'''
for i in range(21):
    print(Gain_1[i],Gain_2[i])
'''
#S是一个形如[2,3]的数组; a是一个形如(-3,3)的数组
def init_()->None:
    for s in State:
        for x in range(max(-5,0 - s[0],s[1]-20),min(5,s[1],20 - s[0])+1):
            policy[s[0]][s[1]].append(x)  

def get_Q(s,a):
    s_ = [s[0]+a,s[1]-a]   
    q = Gain_1[s[0]] + Gain_2[s[1]] - 2 * abs(a)
    q = q + gamma * V[ s[0]+a ][ s[1]-a ]  
    return q

def policy_evaluation() -> None:
    for s in State:
        v_ = 0
        for a in policy[s[0]][s[1]]:
               q  = get_Q(s,a)
               v_ = v_ + q
        if len( policy[s[0]][s[1]] )==0: V[s[0]][s[1]]=0
        else: V[s[0]][s[1]] = v_ / len( policy[s[0]][s[1]] )

def policy_improvement() -> None:
    for s in State:
        Q = [get_Q(s,a) for a in policy[s[0]][s[1]]]        
        A_  = []
        for iter,v in enumerate(Q):
            if v==max(Q):
                A_.append(policy[s[0]][s[1]][iter])
        policy[s[0]][s[1]] = A_
        
          
        
def show() -> None:
    xxx = [ [policy[i][j][0] for i in range(21)] for j in range(21) ]    
    plt.matshow(xxx)
    plt.show()
    plt.matshow(V)
    plt.show()       
    
if __name__ == '__main__':
    init_()
  
    for i in range(5):
        policy_evaluation()
        policy_improvement()
        print("第",i+1,"次迭代：")
        show()
        print('\n')
