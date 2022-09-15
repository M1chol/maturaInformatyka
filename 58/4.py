import math
with open("dane_systemy1.txt") as dane:
    temp=[int(t.split(' ')[1],2) for t in dane]
maxSkok=0
for i in range(len(temp)):
    for j in range(i+1, len(temp)):
        ti=temp[i]
        tj=temp[j]
        rij=(ti-tj)**2
        if rij!=0:
            skok=math.ceil(rij/abs(i-j))
            if skok>maxSkok: maxSkok=skok
print(maxSkok)