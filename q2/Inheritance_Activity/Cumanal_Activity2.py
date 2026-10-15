# Single Inheritance
class Grace:
    def __init__(self):
        self.parent_msg = "This function is in parent class."

    def get_parent_msg(self):
        return self.parent_msg

    def set_parent_msg(self, msg):
        self.parent_msg = msg

    def func1(self):
        print(self.parent_msg)


class John(Grace):
    def __init__(self):
        Grace.__init__(self)
        self.child_msg = "This function is in child class."

    def get_child_msg(self):
        return self.child_msg

    def set_child_msg(self, msg):
        self.child_msg = msg

    def func2(self):
        print(self.child_msg)


obj = John()
obj.func1()
obj.func2()
obj.set_parent_msg("Parent message changed.")
obj.set_child_msg("Child message changed.")
obj.func1()
obj.func2()


# Multilevel Inheritance
class HenrySR:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

    def get_grandfathername(self):
        return self.grandfathername

    def set_grandfathername(self, name):
        self.grandfathername = name


class HenryJR(HenrySR):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        HenrySR.__init__(self, grandfathername)

    def get_fathername(self):
        return self.fathername

    def set_fathername(self, name):
        self.fathername = name


class BabyHenry(HenryJR):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        HenryJR.__init__(self, fathername, grandfathername)

    def get_sonname(self):
        return self.sonname

    def set_sonname(self, name):
        self.sonname = name

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)


s1 = BabyHenry('Prince', 'Rampal', 'Lal mani')
print(s1.get_grandfathername())
s1.print_name()
s1.set_sonname('Arjun')
s1.set_fathername('Vikram')
s1.set_grandfathername('Hari om')
s1.print_name()


# Hierarchical Inheritance
class Patrice:
    def __init__(self):
        self.parent_msg = "This function is in parent class."

    def get_parent_msg(self):
        return self.parent_msg

    def set_parent_msg(self, msg):
        self.parent_msg = msg

    def func1(self):
        print(self.parent_msg)


class Vinson(Patrice):
    def __init__(self):
        Patrice.__init__(self)
        self.child1_msg = "This function is in child 1."

    def get_child1_msg(self):
        return self.child1_msg

    def set_child1_msg(self, msg):
        self.child1_msg = msg

    def func2(self):
        print(self.child1_msg)


class Vhinz(Patrice):
    def __init__(self):
        Patrice.__init__(self)
        self.child2_msg = "This function is in child 2."

    def get_child2_msg(self):
        return self.child2_msg

    def set_child2_msg(self, msg):
        self.child2_msg = msg

    def func3(self):
        print(self.child2_msg)


object1 = Vinson()
object2 = Vhinz()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
object1.set_child1_msg("Child 1 message changed.")
object2.set_child2_msg("Child 2 message changed.")
object1.func2()
object2.func3()