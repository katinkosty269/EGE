#ТИп 5 №15943
for N in range(1, 10000):
    s = bin(N)[2:]
    s += s[-1]
    s += str(s.count('1') % 2)
    R = int(s, 2)
    if R > 105:
        print(R)
        break
    