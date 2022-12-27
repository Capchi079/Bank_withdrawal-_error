class A:
    def __go (self):
        print('private')
    def demo (self):
        self.__go()    
oa=A()
# print(oa.__go())
oa._A__go()
oa.demo()