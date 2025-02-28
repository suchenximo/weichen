def get_peachs(monkeys):
    n = 1
    while not dividable(n,monkeys):
        n += 1
    return n
def dividable(num,monkeys):
    for i in range(monkeys):
        num = divide(num,monkeys)
        if num is None:
            return False
    return True
def divide(num,monkeys):
    num -= 1
    if num % monkeys != 0:
        return None
    return (num // monkeys) * (monkeys - 1)




if __name__ == "__main__":
    print(get_peachs(6))