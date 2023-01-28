#https://github.com/M1chol/pythonMatura
with open('dane_systemy1.txt') as data1, open('dane_systemy2.txt') as data2, open('dane_systemy3.txt') as data3:
    ile=1
    for num, (d1, d2, d3) in enumerate(zip(data1,data2,data3)):
        num1=int(d1.split(' ')[1], 2)
        num2=int(d2.split(' ')[1], 4)
        num3=int(d3.split(' ')[1], 8)
        if num==0:
            d1Max, d2Max, d3Max = num1, num2, num3
        temp=False
        if num1>d1Max:
            temp=True
            d1Max=num1
        if num2>d2Max:
            temp=True
            d2Max=num2
        if num3>d3Max:
            temp=True
            d3Max=num3
        if temp:
            ile+=1
    print(ile)