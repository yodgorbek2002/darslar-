a=int(input("a"))
i=1
if a<100:
  while a%2==0:
    print(i,"maqsud ko't")
  while a%3==0 or a%5==0:
    print(i,"nodir ko't")
    i+=1
