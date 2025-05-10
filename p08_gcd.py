
def gcd(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b

    if a < b:
        a, b = b, a

    while b > 0:
        a, b = b, a % b
    return a




if __name__ == '__main__':
    for a in range(1, 20+1):
        for b in range(1, 20+1):
            print('gcd(%d, %d) = %d' % (a, b, gcd(a, b)))