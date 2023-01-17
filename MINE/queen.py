M = int(input())

K = 2
N = 2
SUM = 0
#repeat:
while True:
    K = K + N
    print(N)
    if N == M:
        break
    #print(K)
    N = N + 1
print(K)
#until N = M