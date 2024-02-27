class Hello:

    def __init__(self):
        self.a=10
        self._b=20
        self.__c=30
    def public_method(self):
        print("In Public Method")
        self.__c=self.__c+10
        print("__c changed to: ",self.__c)
        print("In Private Method")
        self.__private_method()
        print("__c changed to: ",self.__c)

    def __private_method(self):
        self.__c=self.__c+100

hello=Hello()
print(hello.a)
print(hello._b)
#print(hello.__c)
hello.public_method()
#hello.__private_method()
   