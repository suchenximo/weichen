import numpy as np

def get_num(num:int,min_value:int,max_value:int) -> int:
    return list(np.random.randint(min_value,max_value+1,[num]))
def make_24(numbbers):
    res = []
    for value, s in make_result(numbbers):
        if value == 24:
            res.append(s)
    return res

def make_result(numbbers):
    if len(numbbers) == 1:
        return [(numbbers[0], str(numbbers[0]))]
    result = []
    for set1, set2 in make_set(numbbers):
        result1 = make_result(set1)
        result2 = make_result(set2)
        for value1, s1 in result1:
            for value2, s2 in result2:
                result.append((value1 + value2, '(%s+%s)' % (s1, s2)))
                result.append((value2 * value1, '(%s*%s)' % (s1, s2)))
                result.append((value1 - value2, '(%s-%s)' % (s1, s2)))
                result.append((value2 - value1, '(%s-%s)' % (s2, s1)))
                if value2 != 0:
                    result.append((value1 / value2, '(%s/%s)' % (s1, s2)))
                if value1 != 0:
                    result.append((value2 / value1, '(%s/%s)' % (s2, s1)))
        return result
def make_set(numbers):
    result = []
    for i,num in enumerate(numbers):
        set1 = [num]
        set2 = numbers.copy()
        del set2[i]
        result.append((set1,set2))
    if len(numbers) < 4:
        return result
    if len(numbers) > 4:
        return result
    for i,num in enumerate(numbers):
        for j in range(i+1,len(numbers)):
            set1 = [numbers[i],numbers[j]]
            set2 = numbers.copy()
            del set2[j]
            del set2[i]
            result.append((set1,set2))
    return result
if __name__ == "__main__":
    numbbers = get_num(4,1,13)
    print(numbbers)
    answers = make_24(numbbers)
    print(answers)