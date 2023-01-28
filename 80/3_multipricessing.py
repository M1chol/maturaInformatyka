import threading
import queue

q = queue.Queue(maxsize=100)

def czyTr():
    while True:
        global ile
        a,b,c = q.get()
        if (a + b > c) and (a + c > b) and (b + c > a):
            ile+=1
        q.task_done()

threading.Thread(target=czyTr, daemon=True).start()

with open('dane_trojkaty.txt') as dane:
    ile=0
    new_dane=[int(i.rstrip()) for i in dane]
    for i in range(500-2):
        for j in range(i+1,500-1):
            for k in range(j+1,500):
                q.put([new_dane[i], new_dane[j], new_dane[k]])
    q.join()
    print(ile)