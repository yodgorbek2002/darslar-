"""1.a=int(input("a= "))
if a>0:
    print(a+1)
else:
    print(a)

2.a=int(input("a= "))
if a>0:
    print(a+1)
else:
    print(a/2)
3.a=int(input("a= "))
if a>0:
    print(a+1)
elif a<0:
    print(a/2)
else:
    print(10)
4.a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
S=0
if a>0:
    S=S+1
if b>0:
    S=S+1
if c>0:
    S=S+1
print(S)
5.a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
c=int(input("c= "))
S=0
if a>0:
    S=S+1
if b>0:
    S=S+1
if c>0:
    S=S+1
if c>0:
    S=S+1
print(S,"ta musbat",4-S,"ta manfiy")
6.a=int(input("a= "))
b=int(input("b= "))
if a>b:
    print(a)
if a<b:
    print(b)
7.a=int(input("a= "))
b=int(input("b= "))
if a>b:
    print("ikkinhi son kichik")
if a<b:
    print("birinchi son kichik")

8.a=int(input("a= "))
b=int(input("b= "))
if a>b:
    print(a,b)
if a<b:
    print(b,a)

9.a=int(input("a= "))
b=int(input("b= "))
if a>b:
    print("b=",a,"a=",b)
if b>a:
    print("a=",a,"b=",b)
10.a=int(input("a= "))
b=int(input("b= "))
if a!=b:
    print(a+b)
if a==b:
    print(0)

11.a=int(input("a= "))
b=int(input("b= "))
if a!=b and a>b:
    print(a)
if a!=b and a<b:
    print(b)    
if a==b:
    print(0)
12.a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
if a<b<c:
    print(c)
if a<c<b:
    print(b)
if c<b<a:
    print(a)
13.a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
if a<b<c or c<b<a:
    print(b)
if a<c<b or b<c<a:
    print(c)
if b<a<c or c<a<b:
    print(a)


14.a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
if a<b<c:
    print(a,c)
if c<b<a:
    print(c,a)
if a<c<b:
    print(a,b)
if b<c<a:
    print(b,a)
if b<a<c:
    print(b,c)
if c<a<b:
    print(c,b)

15.
16.
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
if a<b<c:
    print(2*a,2*b,2*c)

else:
    print(-a,-b,-c)
    
17.a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
if a<b<c:
    print(2*a,2*b,2*c)

if a>b>c:
    print(2*a,2*b,2*c)
else:
    print(-a,-b,-c)
18.a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
if a==b:
    print(c)
if a==c:
    print(b)
if b==c:
    print(
19.a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
d=int(input("d= "))
if a==b==c:
    print("tortinchi")
if a==c==d:
    print("ikkinchi")
if b==c==d:
    print("birinchi")
if a==b==d:
    print("uchinchi
if 20
from math import *
a=float(input('1-sonni kiriting:'))
b=float(input('2-sonni kiriting:'))
c=float(input('3-sonni kiriting:'))
if fabs(a-b)>fabs(a-c):
    print(c,fabs(a-c))
elif fabs(a-b)==fabs(a-c):
    print(a,b,c,)
else:
    print(b,fabs(a-b))

if 21
x=int(input('x='))
y=int(input('y='))
if x==0 and y==0:
    print(0)
elif x==0 and y!=0:
    print(1)
elif x!=0 and y==0:
    print(2)
else: 
    print(3)
x=int(input('x='))
y=int(input('y='))
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
print(x>a and x>b and x>c or )
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
if a<b<c:
    print(2*a,2*b,2*c)

else:
    print(-1*a,-1*b,-1*c)
from  math import sin
24.x=int(input("x= "))
if x>0:
    print(2*sin(x))
if x<=0:
    print(x-6)
25.x=int(input("x= "))
if x<-2 or x>0:
    print(2*x)
else:
    print(-3*x)
26.x=int(input("x= "))
if x<=0:
    x=-x
    print(x)
elif 0<x<2:
    print(x**2)
elif x>=2:
    print(4)
x=int(input("x= "))
if x<0:
    print(0)
if x%2==0:
    print(1)
if x%2==1:
    print(-1)
N=int(input("N = ")) 
onlik=N//10
birlik=N%10
if onlik==1:
    print("O'n", end=" ")
    
if onlik==2:
    print("Yigirma", end=" ")
if onlik==3:
    print("O'ttiz", end=" ")
if onlik==4:
    print("Qirq", end=" ")
if onlik==5:
    print("Ellik", end=" ")
if onlik==6:
    print("Oltmish", end=" ")
if onlik==7:
    print("Yetmish", end=" ")
if onlik==8:
    print("Sakson", end=" ")
if onlik==9:
    print("To'qson", end=" ")
if birlik==1:
    print("bir", end=" ")
if birlik==2:
    print("ikki", end=" ")
if birlik==3:
    print("uch", end=" ")
if birlik==4:
    print("to'rt", end=" ")
if birlik==5:
    print("besh", end=" ")
if birlik==6:
    print("olti", end=" ")
if birlik==7:
    print("yetti", end=" ")
if birlik==8:
    print("sakkiz", end=" ")
if birlik==9:
    print("to'qqiz", end=" ")

if N==0:
    print("no'l", end=" ")
ball=int(input("ball= "))
if 0<ball<56:
    print("2 baho")
elif 56<ball<71:
    print("3 baho")
elif 70<ball<86:
    print("4 baho")
elif 86<ball<101:
    print("5 baho")
else:
    print("hech narsa")"""
a=int(input("a= "))
b=int(input("b= "))
x=input("x=")
if a>0 and b>0:
    if x=="+":
        print(a+b)
    elif x=="*":
        print(a*b)
    elif x=="-":
        print(a-b)
    elif x=="/":
        print(a/b)
    elif x=="//":
        print(a//b)
    elif x=="**":
        print(a**b)


























