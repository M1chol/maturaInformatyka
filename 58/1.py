#https://github.com/M1chol/pythonMatura
with open('dane_systemy1.txt') as data1, open('dane_systemy2.txt') as data2, open('dane_systemy3.txt') as data3:

    for num, (d1, d2, d3) in enumerate(zip(data1,data2,data3)):
        num1=int(d1.split(' ')[1], 2)
        num2=int(d2.split(' ')[1], 4)
        num3=int(d3.split(' ')[1], 8)
        if num==0:
            d1Min, d2Min, d3Min= num1, num2, num3
        if num1<d1Min: d1Min=num1
        if num2<d2Min: d2Min=num2
        if num3<d3Min: d3Min=num3
    print(bin(d1Min), bin(d2Min), bin(d3Min))