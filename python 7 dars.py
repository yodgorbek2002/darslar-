"""1.hafta_kuni=int(input("hafta_kuni:"))
if 0<hafta_kuni<8:
    if hafta_kuni<2:
        print("dushanba")
    elif hafta_kuni<3:
        print("seshanba")
    elif hafta_kuni<4:
        print("chorshanba")
    elif hafta_kuni<5:
        print("payshanba")
    elif hafta_kuni<6:
        print("juma")
    elif hafta_kuni<7:
        print("shanba")
    elif hafta_kuni<8:
        print("yakshanba")
    
2.K=int(input("K= "))
if 0<K<6:
     if K<2:
         print("yomon")
     elif K<3:
         print("qoniqarsiz")
     elif K<4:
         print("qoniqarli")
     elif K<5:
         print("yaxshi")
     elif K<6:
         print("a/'lo")
else:
    print("xato")
3.oy=int(input("oy= "))
if 0<oy<13:
    if oy<3 or oy==12:
        print("qish")
    elif oy<6:
        print("bahor")
    elif oy<9:
        print("yoz")
    elif oy<12:
        print("kuz")
else:
    print("xato")
4.oy=int(input("oy= "))
if 0<oy<13:
    if oy==2:
        print("28 kun bor")
    elif oy%2==0:
        print("30 kun bor")
    elif oy%2==1:
        print("31 kun bor:")
else:
    print("bu raqamli oy yoq")

5.a=int(input("a= "))
b=int(input("b= "))
amal=int(input("amal= "))
if a>0 and b>0:
    if amal==1:
        print(a+b)
    elif amal==2:
        print(a-b)
    elif amal==3:
        print(a/b)
    elif amal==4:
        print(a*b)
6.a=int(input("a= "))
b=int(input("b= "))
if 0<b<6:
    if b==1:
        print(a/10,"metr")
    elif b==2:
        print(a*1000,"metr")
    elif b==3:
        print(a,"metr")
    elif b==4:
        print(a/1000,"metr")
    elif b==5:
        print(a/100,"metr")
else:
    print("xato")
    
7.a=int(input("a= "))
b=int(input("b= "))
if 0<b<6:
    if b==1:
        print(a,"kilogram")
    elif b==2:
        print(a/10000,"kilogram")
    elif b==3:
        print(a/1000,"kilogram")
    elif b==4:
        print(a*1000,"kilogram")
    elif b==5:
        print(a*10,"kilogram")
else:
    print("xato")
8.D=int(input("D= "))
M=int(input("M= "))

if 0<M<13 and 0<D<32:
    if M==2 and 0<D<29:
        print(D,"-","fevral")
    elif M==1:
        print(D,"-","yanvar")
    elif M==3:
        print(D,"-","mart")
    elif M==4:
        print(D,"-","aprel")
    elif M==5:
        print(D,"-","may")
    elif M==6:
        print(D,"-","iyun")
    elif M==7:
        print(D,"-","iyul")
    elif M==8:
        print(D,"-","avgust")
    elif M==9:
        print(D,"-","sentabr")
    elif M==10:
        print(D,"-","oktabr")
    elif M==11:
        print(D,"-","noyabr")
    elif M==12:
        print(D,"-","dekabr")
else:
    print("bunaqa sana mavjud emas")
9.D=int(input("D= "))
M=int(input("M= "))
if 0<M<13 and 0<D<32:
    if M==1: print(D+1,"yanvar")
    if M==2 and 1<=D<=28: print(D+1,"fevral")
    if M==3: print(D+1,"mart")
    if M==4: print(D+1,"aprel")
    if M==5: print(D+1,"may")
    if M==6: print(D+1,"iyun")
    if M==7: print(D+1,"iyul")
    if M==8: print(D+1,"avgust")
    if M==9: print(D+1,"sentabr")
    if M==10: print(D+1,"oktabr")
    if M==11: print(D+1,"noyabr")
    if M==12: print(D+1,"dekabr")
else:
    print("bunaqa sana mavjud emas")
10.Y=input("boshlangich nuqtani kiriting:")
K=int(input("K= "))
if Y =="s":
    if K==0:
        print("shimol")
    elif K==1:
        print("sharq")
    elif K==2:
        print("Garb")
    elif K==3:
        print("janub") 
if Y =="j":
    if K==0:
        print("janub")
    if K==1:
        print("Garb")
    if K==2:
        print("sharq")
    if K==3:
        print("shimol") 
if Y =="q":
    if K==0:
        print("sharq")
    if K==1:
        print("shimol")
    if K==2:
        print("janub")
    if K==3:
        print("Garb") 
if Y=="g":
    if K==0:
        print("Garb")
    if K==1:
        print("janub")
    if K==2:
        print("shimol")
    if K==3:
        print("sharq")

11.C=input("boshlangich nuqtani kiriting:")
K=int(input("K1= "))
K2=int(input("K2= "))
if C =="s":
    if K==0:
        if K2==0:
            print("janub")
        if K2==1:
            print("shimol")
        if K2==2:
            print("garb")
        
    if K==1:
        if K2==0:
            print("shimol")
        if K2==1:
            print("janub")
        if K2==2:
            print("sharq")
    if K==2:
        if K2==0:
            print("sharq")
        if K2==1:
            print("garb")
        if K2==2:
            print("shimol")
if C=="j":
    if K==0:
        if K2==0:
            print("shimol")
        if K2==1:
            print("janub")
        if K2==2:
            print("sharq")
    if K==1:
        if K2==0:
            print("janub")
        if K2==1:
            print("shimol")
        if K2==2:
            print("garb")
    if K==2:
        if K2==0:
            print("garb")
        if K2==1:
            print("sharq")
        if K2==2:
            print("janub")
if C =="q":
    if K==0:
        if K2==0:
            print("garb")
        if K2==1:
            print("sharq")
        if K2==2:
            print("janub")
    if K==1:
        if K2==0:
            print("sharq")
        if K2==1:
            print("garb")
        if K2==2:
            print("shimol")
    if K==2:
        if K2==0:
            print("janub")
        if K2==1:
            print("shimol")
        if K2==2:
            print("sharq")
     
if C=="g":
    if K==0:
        if K2==0:
            print("sharq")
        if K2==1:
            print("garb")
        if K2==2:
            print("shimol")
    if K==1:
        if K2==0:
            print("garb")
        if K2==1:
            print("sharq")
        if K2==2:
            print("janub")
    if K==2:
        if K2==0:
            print("shimol")
        if K2==1:
            print("janub")
        if K2==2:
            print("garb")"""
N=int(input("N= "))
M=int(input("M= "))
if M==1:
    if 6<=N<=10: print(N,"gisht")
    if N==11: print("valet gisht")
    if N==12: print("dama gisht")
    if N==13: print("karol gisht")
    if N==14: print("tuz gisht")
if M==2:
    if 6<=N<=10: print(N,"olma")
    if N==11:
        print("valet olma")
    if N==12:
        print("dama olma")
    if N==13:
        print("karol olma")
    if N==14:
        print("tuz olma")
if M==3:
    if 6<=N<=10:
        print(N,"chillik")
    if N==11:
        print("valet chillik")
    if N==12:
        print("dama chillik")
    if N==13:
        print("karol chillik")
    if N==14:
        print("tuz chillik")
if M==4:
    if 6<=N<=10:
        print(N,"qarga")
    if N==11:
        print("valet qarga")
    if N==12:
        print("dama qarga")
    if N==13:
        print("karol qarga")
    if N==14:
        print("tuz qarga")
"""darss.pya=int(input("a= "))
birlik=a%10
onlik=a//10
if a==20:
    print("yigirma")
elif a==30:
    print("ottiz")
elif a==10:
    print("qirq")
elif a==50:
    print("o/'n")
elif a==60:
    print("oltmish")
elif onlik==1:
    print("o/'n")
elif onlik==2:
    print("yigirma")
elif  onlik==3:
    print("ottiz")
elif  onlik==4:
    print("qirq")
if birlik==1:
    print("birinch masala")
if birlik==2:
    print("ikkinchi masam")
if birlik==3:
    print("uchinchi masala")
if birlik==4:
    print("tortinchi masala")
if birlik==5:
    print("beshinchi masal")
if birlik==6:
    print("oltinchi masal")
if birlik==7:
    print("yettinchi masala")
if birlik==8:
    print("sakkizchi masala")
if birlik==9:
    print("toqqizinchi masala")


a=int(input("a= "))
if a%5==4: print("yashil")
if a%5==3: print("qizil")
if a%5==2: print("sariq")
if a%5==1: print("oq")
if a%5==0: print("qora")
if a%12==1: print("sichqon", end= ' ')
if a%12==2: print("sigir", end= ' ')
if a%12==3: print("yolbars", end= ' ') 
if a%12==4: print("quyon", end= ' ')
if a%12==5: print("ajdar", end= ' ')
if a%12==6: print("ilon", end= ' ')
if a%12==7: print("ot", end= ' ')
if a%12==8: print("qo/'y", end= ' ')
if a%12==9: print("maymun", end= ' ')
if a%12==10: print("tovuq", end= ' ')
if a%12==11: print("it", end= ' ')
if a%12==0: print("to/'ngiz", end= ' ')
13,14,16,17,18
d=int(input("d= "))
m=int(input("m= "))
y=int(input("y= "))
d+=1
kabisa=False
if y%4==0:
    kabisa=True
if y%100==0 and y%400!=0:
    kabisa=False

if kabisa==True:
    if m==2:
        d==28+kabisa
        m==2

else:
    if m==4 or m==6 or m==9 or m==11:
        if d>30:
            d=1
            m+=1
    elif m==2:
        if d>28:
            d=1
            m=3
    else:
        if d>31:
            d=1
            m+=1
        if m>12:
            m=1
            y+=1
print(d,m,y,sep="-")"""
    
            
            
   
    



























































































































