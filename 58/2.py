#https://github.com/M1chol/pythonMatura
with open('dane_systemy1.txt') as data1, open('dane_systemy2.txt') as data2, open('dane_systemy3.txt') as data3:
    ile=0
    for num, (d1, d2, d3) in enumerate(zip(data1,data2,data3)):
        num1=int(d1.split(' ')[0], 2)-12
        num2=int(d2.split(' ')[0], 4)-12
        num3=int(d3.split(' ')[0], 8)-12
        if num1%24!=0 and num2%24!=0 and num3%24!=0:
            ile+=1

    print(ile)