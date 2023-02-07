def pot(a,x, M):
    if x==0:
        return 1
    if x%2==1:
        return a*pot(a, x-1, M) % M
    temp = pot(a, x/2, M) % M
    return (temp**2) % M

# with open('liczby.txt') as dane:
#     ile=0
#     for line in dane:
#         M, a, b = map(int, line.split())
#         for i in range(M-1):
#             if pow(a, i, M) == b:
#                 ile+=1
#                 break
#     print(ile)