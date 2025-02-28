
def perms(m:int, n:int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return m
    result = n * perms(m - 1, n - 1)           #包含1号球
    if m > n:
        result += perms(m - 1, n)          #不包含1号球
    return result

if __name__ == '__main__':
    for m in range(1,10+1):
        for n in range(1,m+1):
            print('Comb(%d,%d) = %d' % (m, n, perms(m, n)))
