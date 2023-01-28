with open('liczby2.txt') as dane:
    dane2=[int(i) for i in dane]
    temp=0
    ile=1
    maxile=0
    maxtemp=0
    for i in range(len(dane2)-1):
        if dane2[i+1]<dane2[i]:
            ile=1
            temp=i+1
        else:
            ile+=1
            if ile>maxile:
                maxile=ile
                maxtemp=temp
print(dane2[maxtemp],maxile)