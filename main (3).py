#ТИп 5 №15974
for N in range(1,10000):
    s = bin(N)
    s = s[2:]
    s = s[:-1]
    if N % 2 !=0:
        s += '10'
    else:
        s += '01'
    R = int(s, 2)
    if R==2018:
        print(N)
        break
    