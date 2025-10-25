#ТИп 5 №15974
for N in range(256):
    s = bin(N)
    s = s[2:]
    if len(s) < 8:
        s = '0' * (8 - len(s)) + s
    s = s.replace('0', '*')
    s = s.replace('1', '0')
    s = s.replace('*', '1')
    
    R = int(s, 2)
    if R-N==133:
        print(N)

    