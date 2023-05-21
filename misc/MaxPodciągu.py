t=list(range(20)) # [0,1,2,3,4...]
maxx=0
max_pocz=0
max_kon=0
for i in range(len(t)): #0 ... len(t)
    for j in range(i+1,len(t)+1): # 1, 2, 3, 4,
        if maxx > sum(t[i:j]):
            maxx = sum(t[i:j])
            max_pocz = i
            max_kon = j
print(maxx, max_pocz, max_kon)