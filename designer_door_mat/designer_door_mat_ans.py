N, M = map(int, input().split())

for n in range(1, N + 1):
    if n < (N + 1)//2:
        print(('.|.'*(2*n - 1)).center(M, '-'))
    elif n == (N + 1)//2:
        print('WELCOME'.center(M, '-'))
    else:
        num = (N + 1 - n)*2 - 1
        print(('.|.'*num).center(M, '-'))