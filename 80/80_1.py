with open('dane_trojkaty.txt') as dane:
    stack=[]
    for i in range(500):
        stack.append(int(dane.readline().rstrip()))
        if len(stack)<3: continue
        new=sorted(stack)
        if new[0]**2+new[1]**2==new[2]**2:
            print(new)
        stack.pop(0)
