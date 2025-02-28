def get_list(pokes):
    result = [pokes]
    for p in range(pokes-1,0,-1):
        for _ in range(p):
            flip(result)
        result.insert(0,p)
    return result
def flip(result):
    poke = result[-1]
    del result[-1]
    result.insert(0, poke)


if __name__ == "__main__":
    print(get_list(20))