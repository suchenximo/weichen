
def get_rabbit(n):
    if n < 2:
        return 1
    return get_rabbit(n - 1) + get_rabbit(n - 2)




if __name__ == '__main__':
    for n in range(10+1):
        print('%d: %10d' % (n, get_rabbit(n)))