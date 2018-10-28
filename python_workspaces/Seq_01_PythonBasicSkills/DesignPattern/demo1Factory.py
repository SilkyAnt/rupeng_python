class Singleton(object):
    __instance=None
    def __init__(self,*args,**kwd):
       object.__init__(self,*args,**kwd)
    def __new__(cls,*args,**kwd):
        if Singleton.__instance is None:
            Singleton.__instance=object.__new__(cls)
        return Singleton.__instance

class MyClass(Singleton):
    def __init__(self,name):
        Singleton.__init__(self)
        self.name = name
a = MyClass("Alex")
b = MyClass("Jack")
print(a.name)
print(b.name)