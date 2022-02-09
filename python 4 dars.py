"""1.a=int(input("a= "))
print(a>0)
2.a=int(input("a= "))
print(a%2==1)
3.a=int(input("a= "))
print(a%2==0)
4.A=int(input("a= "))
B=int(input("b= "))
print(A>2 and B<=3)
5.A=int(input("A= "))
B=int(input("B= ")
print(A>=0 or B<2)
6.A=int(input("A= "))
B=int(input("B= "))
C=int(input("C= "))
print(A<=B<=C)
7.A=int(input("A= "))
B=int(input("B= "))
C=int(input("C= "))
print(A<B<C)
8.A=int(input("A= "))
B=int(input("B= "))
print(A%2==1 and B%2==1)
9.10.A=int(input("A= "))
B=int(input("B= "))
print(A%2==0 and B%2==1 or A%2==1 and B%2==0)
11.A=int(input("A= "))
B=int(input("B= "))
print(A%2==0 and B%2==0 or A%2==1 and B%2==1)
1213.A=int(input("A= "))
B=int(input("B= "))
C=int(input("C= "))
print(A>0 and B>0 and C>0)
14.A=int(input("A= "))
B=int(input("B= "))
C=int(input("C= "))
print(A>0 or B>0 or C>0)
15.A=int(input("A= "))
B=int(input("B= "))
C=int(input("C= "))
print(A>0 and B>0 or A>0 and C>0 or C>0 and B>0)
16.A=int(input("A= "))
print(9<A<99 and A%2==0)
17.A=int(input("A= "))
print(9<A<99 and A%2==0)
18.A=int(input("A= "))
B=int(input("B= "))
C=int(input("C= "))
print(A==B or A==C or B==C)
19.A=int(input("A= "))
B=int(input("B= "))
C=int(input("C= "))
print(A==-B or A==-C or -A==C)
20.A=int(input("A= "))
print(A//100!=A//10%10!=A%10)
21.A=int(input("A= "))
print(A//100==(A//10%10)-1==(A%10)-2)
22.A=int(input("A= "))
print(A%10==(A//10%10)+11==(A//100+2) or A//100==(A//10%10)+1==A%10+2)
23.A=int(input("A= "))
print(A%10==A//100)
 Bool 34
x=int(input('x='))
y=int(input('y='))
print((x+y)%2!=0)
x=9
y=6
Shu koordinatada joylashgan hudud oq bo'ladi: True
# Bool 35
x1=int(input("x1="))
y1=int(input("y1="))
x2=int(input("x2="))
y2=int(input("y2="))
A=((x1+y1)%2==(x2+y2)%2)
print(A)
x1=1
y1=2
x2=3
y2=5
Berilgan maydonlar bir xil rangda: False
# Bool 36
x1=int(input("x1="))
y1=int(input("y1="))
x2=int(input("x2="))
y2=int(input("y2="))
B=(x1==x2 or y1==y2)
print(B)
x1=5
y1=2
x2=6
y2=2
Ruh yura oladi: True
# Bool 37adashibman 
x1=int(input("x1="))
y1=int(input("y1="))
x2=int(input("x2="))
y2=int(input("y2="))
ruh=(abs(x1-x2)+abs(y1-y2)<3 and abs(x1-x2)<2 and abs(y1-y2)<2)
print(ruh)
x1=1
y1=1
x2=2
y2=2
Shoh yura oladi: True
# Bool 38
x1=int(input("x1="))
y1=int(input("y1="))
x2=int(input("x2="))
y2=int(input("y2="))
fil=(abs(x1-x2)==abs(y1-y2))
print(fil)
x1=1
y1=2
x2=1
y2=3
Fil yura oladi: False
# Bool 39
x1=int(input("x1="))
y1=int(input("y1="))
x2=int(input("x2="))
y2=int(input("y2="))
farzin=((x1==x2 or y1==y2) or (abs(x1-x2)==abs(y1-y2)))
print(farzin)
x1=2
y1=4
x2=2
y2=8
Farzin yura oladi: True
# Bool 40
x1=int(input("x1="))
y1=int(input("y1="))
x2=int(input("x2="))
y2=int(input("y2="))
ot=(abs(x1-x2)*abs(y1-y2)==2)
print(ot)
x1=1
y1=2
x2=2
y2=4
Ot yura oladi: True"""

A=int(input("A= "))
    
if A>0:
    print("musbat")
elif A==0:
    print("0")
else:
    print("manfiy")
















































