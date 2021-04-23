# Singleton/SingletonPattern.py

class OnlyOne:
    class __Onlytwo:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    
    instance = None
    print(type(instance))
    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__Onlytwo(arg)
           # return OnlyOne.instance
        else:
            OnlyOne.instance.val = arg
            #return OnlyOne.instance.val
    def __getattr__(self,name):
       return getattr(self.instance,name)

x = OnlyOne('sausage')
print(x)
y = OnlyOne('eggs')
print(y)
z = OnlyOne('spam')
print(z)
print(x)
print(y)
print("Hello worls")
print(`x`)
print(`y`)
print(`z`)
output = '''
<__main__.__OnlyOne instance at 0076B7AC>sausage
<__main__.__OnlyOne instance at 0076B7AC>eggs
<__main__.__OnlyOne instance at 0076B7AC>spam
<__main__.__OnlyOne instance at 0076B7AC>spam
<__main__.__OnlyOne instance at 0076B7AC>spam
<__main__.OnlyOne instance at 0076C54C>
<__main__.OnlyOne instance at 0076DAAC>
<__main__.OnlyOne instance at 0076AA3C>
'''
