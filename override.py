class Parent(object):
    def fun(self):
        print('Hi')
        p = Parent()
        p.fun()
        
class child(Parent):
    def fun(self):
        print('Bye')