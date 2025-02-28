import math
NAME= "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张黄"

def get_pages(names):
    num = 1 + int(math.log(len(names),2))
    result = [""for _ in range(num)]
    for i in range(len(names)):
        code = i +1
        for j in range(num):
            if code % 2 == 0:
                result[j] += names[i] + ", "
                code = code // 2
    return result

def get_name(names,answer):
    result = 0
    for answer in reversed(answer):
        result = result + int(answer)
    return names[result-1]



if __name__ == "__main__":
    pages = get_pages(NAME)
    result = []
    for page in pages:
        print(page)
        answer = input("is your name in this page?(y,n)")
        if answer.lower() == "y":
            result.append(1)
        elif answer.lower() == "n":
            result.append(0)
        name = get_name(NAME,result)
        print("your name is",name)
