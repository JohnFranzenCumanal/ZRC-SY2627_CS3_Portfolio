#Single Inheritance
class Grace:
    def func1(self):
        print("This function is in parent class.")

class John(Grace):
    def func2(self):
        print("This function is in child class.")

obj = John()
obj.func1()
obj.func2()

#Multilevel Inheritance
class HenrySR:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

class HenryJR(HenrySR):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        HenrySR.__init__(self, grandfathername)

class BabyHenry(HenryJR):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        HenryJR.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)

s1 = BabyHenry('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()

#Heirarchical Inheritance
class Patrice:
    def func1(self):
        print("This function is in parent class.")

class Vinson(Patrice):
    def func2(self):
        print("This function is in child 1.")

class Vhinz(Patrice):
    def func3(self):
        print("This function is in child 2.")

object1 = Vinson()
object2 = Vhinz()
object1.func1()
object1.func2()
object2.func1()
object2.func3()