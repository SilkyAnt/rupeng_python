class Person:
    name = ""
    sex = ""

    def __init__(self, name, sex):
        pass

    def getName(self):
        return self.name;

    def getSex(self):
        return self.sex


class Male(Person):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


class Female(Person):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


class Personfactory:
    def getPerson(self, name, sex):
        if sex == "M":
            return Male(name, sex)
        if sex == "F":
            return Female(name, sex)


factor = Personfactory()
p1 = factor.getPerson("梨花", 'F')
print(p1.getName())
print(p1.getSex())
p2 = factor.getPerson("胡继虎", 'M')
print(p2.getName())
print(p2.getSex())