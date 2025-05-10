def fac(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def fac2(n):
    result = [1]
    for i in range(2, n+1):
        mul(result, i)
    return to_string(result)

def mul(result, a):
    add = 0
    for i in range(len(result)):
        mul = result[i] * a + add
        result[i] = mul % 10
        add = mul // 10
    while add > 0:
        result.append(add % 10)
        add //= 10
    return result

def to_string(result):
    result.reverse()
    return "".join(str(i) for i in result)



if __name__ == "__main__":
    for n in range(2, 100+1):
        print("%d != %s" % (n, fac2(n)))