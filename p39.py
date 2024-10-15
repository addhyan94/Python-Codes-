#Multi  level 
class A():
    def m1(self):
        print("This is m1 form class A..")
class B(A):
    def m2(self):
        print("This is m2 form Class B ")
class C(B):
    def m3(self):
        print("This is m3 from class C ...")
c=C()
c.m3()
c.m2()
c.m1()
