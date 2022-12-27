def decor(arg):
    d={}
    def inner():
        if arg not in d:
            d[arg]=arg()#d={"tk"}
        return d[arg]
    return inner
@decor 
class movie_tk:
    def __init__(self):
        self.avltk=100;
    def booking_tk(self,n):
        self.number_tk=n
        if self.avltk >= n:
            self.avltk-=n
            print('sucessfull booking')
        else:
            print('not available')
def getdata():
    n=int(input('enter the number'))
    object=movie_tk()
    object.booking_tk(n)
getdata()
getdata()
getdata()