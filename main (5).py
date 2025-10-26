#ТИп 5 №18785
for N in range(1,10000):
    s = bin(N)[2:]
    if N % 2 == 0:
        s = '1' + s + '0'
    else:
        s = '11' + s + '11'
    R = int(s, 2)
    if R>52:
        print(N)
        break
 
