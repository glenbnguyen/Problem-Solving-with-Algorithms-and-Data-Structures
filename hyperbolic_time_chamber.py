def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while (True):
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm

class Fraction:
    def __init__(self, top, bottom):
        if not isinstance(top, int):
            raise Exception("Only integers accepted as input")

        if not isinstance(bottom, int):
            raise Exception("Only integers accepted as inputs")

        if top < 0 and bottom < 0:
            top = abs(top)
            bottom = abs(bottom)

        elif bottom < 0:
            bottom = abs(bottom)


        self.num = top
        self.den = bottom
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other):
        common = lcm(self.den, other.den)
        if self.den and other.den == common:
            new_den = self.den
            new_num = self.num - other.num
        else:
            new_num = self.num * common
            new_den = self.den * common
        return str(new_num) + '/' + str(new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __gt__(self, other):
        first_num = self.num / self.den
        second_num = other.num / other.den
        return first_num > second_num
        # if first_num > second_num:
        #     greater = True
        # else:
        #     greater = False
        #     print("First number and Second number are the same.")
        # return greater

    def __ge__(self, other):

        first_num = self.num / self.den
        second_num = other.num / other.den
        return first_num >= second_num

        # if first_num >= second_num:
        #     bowl = True
        # else:
        #     bowl = False
        # return bowl

    def __lt__(self, other):
        first_num = self.num / self.den
        second_num = other.num / other.den
        return first_num < second_num
        # if first_num < second_num:
        #     lesser = True
        # elif first_num > second_num:
        #     lesser = False
        # else:
        #     print("First number and Second number are the same.")
        # return lesser

    def __le__(self, other):
        first_num = self.num / self.den
        second_num = other.num / other.den
        return first_num < second_num

        # if first_num <= second_num:
        #     bowl = True
        # else:
        #     bowl = False
        # return bowl

    def __ne__(self, other):
        first_num = self.num / self.den
        second_num = other.num / other.den
        return first_num != second_num
        # if first_num != second_num:
        #     bowl = True
        # else:
        #     bowl = False
        # return bowl

    def simplify(self):
        common = gcd(self.num, self.den)
        self.num = self.num // common
        self.den = self.den // common

    def show(self):
        print(self.num, "/", self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

myf = Fraction(12, 16)
myg = Fraction(10, 16)
# myf = Fraction(12, "1")
# myg = Fraction(10, "2")

print(f" Magic Method Addition: {myf} + {myg} = {myf + myg}")
print(f" Magic Method Subtraction: {myf} - {myg} = {myf - myg}")
print(f" Magic Method Multiplication {myf} * {myg} = {myf * myg}")
print(f" Magic Method Division {myf} / {myg} = {myf / myg}")
print(f" Magic Method Greater Than {myf} > {myg} = {myf > myg}")
print(f" Magic Method Greater Equal Than {myf} >= {myg} = {myf >= myg}")
print(f" Magic Method Less Than {myf} < {myg} = {myf < myg}")
print(f" Magic Method Lesser Equal Than {myf} <= {myg} = {myf <= myg}")
print(f" Magic Method Not Equal To {myf} != {myg} = {myf != myg}")

# print("Magic Method Addition: " + str(myf) + " + " + str(myg) + " = " + str(myf + myg))
# print("Magic Method Multiplication: " + str(myf) + " * " + str(myg) + " = " + str(myf * myg))
# print("Magic Method Division: " + str(myf) + " / " + str(myg) + " = " + str(myf / myg))
#
# print("Magic Method Greater Than: " + str(myf) + " > " + str(myg) + " " + str(myf > myg))
# print("Magic Method Greater or Equal Than: " + str(myf) + " >= " + str(myg) + " " + str((myf) >= (myg)))
#
# print("Magic Method Less Than: " + str(myf) + " < " + str(myg) + " " + str(myf < myg))
# print("Magic Method Lesser or Equal Than: " + str(myf) + " <= " + str(myg) + " " + str((myf) <= (myg)))
#
# print("Magic Method Not Equal To: " + str(myf) + " != " + str(myg) + " " + str((myf) != (myg)))
#


# print(f"The least common multiple of {} and {other.den} is {lcm(self.den,other.den)}")
