from itertools import combinations

def p1_gen(k,m,n):
    hD = [('A','A') for i in range(k)] 
    hz = [('A','a') for i in range(m)] 
    hR = [('a','a') for i in range(n)]
    return hD+hz+hR

def mate(p1,p2):
    f1 = []
    for i in p1:
        for j in p2:
            f1.append((i,j))
    return sorted(f1)

def prob_dom(p1_gen):
    outcomes = []
    for i in combinations(p1_gen,2):
        outcomes.append((mate(i[0],i[1])))
    dom = 0
    total = 0
    for i in outcomes:
        for j in i:
            if 'A' in j:
                dom += 1
                total+= 1
            else:
                total +=1
    
    return dom/total

#example call
prob_dom(p1_gen(19,19,25))

