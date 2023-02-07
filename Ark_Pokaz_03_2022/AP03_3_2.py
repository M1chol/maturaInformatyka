# def potega(a, x, M):
#     w=1
#     for i in bin(x)[2:]:
#         w*=w
#         if i=='1':
#             w*=a
#     return w%M

def potega(a,x, M):
    if x==0:
        return 1
    if x%2==1:
        return a*potega(a, x-1, M) % M
    temp = potega(a, x/2, M) % M
    return (temp**2) % M

print(pow(1612, 25236, 2155))
print(potega(1612, 25236, 2155))