with open('ciagi.txt') as dane:
    for ciag in dane:
        ciag=ciag.rstrip()
        if len(ciag)%2==0:
            if ciag[:len(ciag)//2]==ciag[len(ciag)//2:]:
                print(ciag)