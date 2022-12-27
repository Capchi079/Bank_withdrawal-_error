class error(BaseException):
    def __init__(self,m):
        self.message=m

class bank2:
    bank_name='sbi'
    babk_roi=7
    def __init__(self,cn,cb):
        self.customer=cn
        self.customerbal=cb
    def withdrawall(self):
        self.n=self.get_data()
        if self.customerbal>=self.n:
            self.customerbal-=self.n
            print('withdrwa sucessfull')
        else:
            raise error('insufficient bal')
    @staticmethod
    def get_data():
        n=int(input("enter the ammount: "))
        return n
saty=bank2('satyajit', 1000)
try:
    saty.withdrawall()
except error as e:
    print(e)
