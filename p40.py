# Multiple 
class A():
    def m1(self):
        print("This is m1 from A::::")
class B():
    def m2(Self):
        print(" This is a m2 B:::")
class C(A,B):
    def m3(self):
        print("This is m3 C:::")
c=C()
c.m3()
c.m2()
c.m1()