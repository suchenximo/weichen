class Frace:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __repr__(self):   #repr是一个特殊方法，用于返回一个对象的字符串表示形式
        return '%d/%d' % (self.a,self.b)

    def __add__(self,other):
        a = self.a*other.b + self.b*other.a
        b = self.b*other.b
        return Frace(a,b)
    def __sub__(self,other):
        a = self.a*other.b - self.b*other.a
        b = self.b*other.b
        return Frace(a,b)
    def __mul__(self,other):
        a = self.a*other.a
        b = self.b*other.b
        return Frace(a,b)
    def __truediv__(self,other):
        a = self.a*other.b
        b = self.b*other.a
        return Frace(a,b)
    def __gt__(self,other):
        return self.a/self.b > other.a/other.b




if __name__ == '__main__':
    f1 = Frace(1, 2)
    print(f1)
    print(f1.__init__(1,2))
    print(f1.__repr__())

    f2 = Frace(1,3)
    print(f2)
    print(f2.__repr__())


    print(f1 + f2)          #f1.__add__(f2)
    print(f1 - f2)          #f1.__sub__(f2)
    print(f1 * f2)          #f1.__mul__(f2)
    print(f1 / f2)          #f1.__truediv__(f2)
    print(f1 > f2)          #f1.__gt__(f2)