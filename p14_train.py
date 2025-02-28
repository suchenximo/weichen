def get_num(n: int,m:int = 0) -> int:
    if n == 0:
        return 1

    result = 0
    if n > 0:
        result = get_num(n-1,m+1)

    if m > 0:
        result += get_num(n,m-1)
    return result





if __name__ == '__main__':
    for n in range(10+1):
        print('train:%d,num:%d' % (n, get_num(n)))