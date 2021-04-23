class OnlyOne(object):
    class __two:
        def __init__(self):
            self.val = None
        def __str__(self):
            return self.val
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__two()
            print("new instance is assigned")
            
        else:
        	print("old instance is set")
    
        return OnlyOne.instance
    '''
    def __getattr__(self, name):
    	print("get attribute is being called")
        return getattr(self.instance, name)
    def __setattr__(self, name):
        print("Set attribute is being called")
        return setattr(self.instance, name)
    ''' 

x = OnlyOne()
x.val = 'sausage'
print(x)
y = OnlyOne()
y.val = 'eggs'
print(y)
z = OnlyOne()
z.val = 'spam'
print(z)
print(x)
print(y)
#<hr>
output = '''
<__main__.__OnlyOne instance at 0x00798900>sausage
<__main__.__OnlyOne instance at 0x00798900>eggs
<__main__.__OnlyOne instance at 0x00798900>spam
<__main__.__OnlyOne instance at 0x00798900>spam
<__main__.__OnlyOne instance at 0x00798900>spam
'''
