with open('ciagi.txt') as dane:
    ile=0
    for ciag in dane:
        ciag=ciag.rstrip()
        if '11' not in ciag:
            ile+=1
    print(ile)