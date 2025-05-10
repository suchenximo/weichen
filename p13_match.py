def match(s:str, p:str) -> bool:
    if len(p) == 0:
        return len(s) == 0
    ch = p[0]
    if ch == '?':
        return len(s) > 0 and match(s[1:], p[1:])
    if ch == '*':
        return match(s, p[1:]) or (len(s) > 0 and match(s[1:], p))
    return len(s) > 0 and ch == p[0] and match(s[1:], p[1:])

    return False
def _test(s, p):
    print('string: %s,\t pattern: %s,\tmatch:%s' % (s, p,match(s, p)))





if __name__ == '__main__':
    _test('aabbb','ab*')
    _test('aabbb','a*b')
    _test('aabbb','a*b*')
    _test('aabbb','a*b*c')
    _test('aabbb','a*b*c*')