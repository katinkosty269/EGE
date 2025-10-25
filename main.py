#ТИп 5 №15846
for N in range(1, 10000):
    s = bin(N)[2:]
    if s.count('1') % 2 == 0:
        s += '00'
    else:
        s += '11'
    R = int(s, 2)
    if R > 115:
        print(N)
        break
    