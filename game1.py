from random import randint
print("hello i want to play with me ?:")
print("<-- I will show you my intelligence hh -->")
e=input("if you want to  play tab y(yes) ou if you want to exit tab n(non) :")
if e=="y" or e=="yes" or e=="Y" or e=="YES":
    print("Let's go : ")
    print(" 1. First my name is (computer) and I make the rules ")
    print(" ------ bach n5tar ra9m mn (1 ,99) ou bach na3tik 3 mou7awlat kana e5atrt ra9m akber mn ra9m taw n9olk "
          "kana a9al taw n9olk ou kana 9ad 9ad rba7t <3  ")
    mo=input("3and 3 mode fi gamme facil(f) ou normal(n) ou difficult(d): ")

    if mo=="f" or mo=="facil":
        sc=10
    elif mo=="n" or mo=="noraml":
        sc=6
    elif mo=="d" or mo=="difficult":
        sc=3
    else:
        mo = input("3and 3 mode fi gamme facil(f) ou normal(n) ou difficult(d): ")
    print("<___ 3andk ",sc,"mo7awlat ___>")

    d=randint(1,99)
    for i in range(sc):
         x=int(input("donner un nombre de (1 , 99 ) mo7awla r0a9m :"))
         while not (1<=x<=99):
             x= int(input("donner un nombre de (1,99):"))
         if x<d:
             print("ra9mk s4ir barcha hh ")
         if x>d:
             print("ra9mk kbir barcha hh ")
         if x==d:
              print("bravo <3")
              break

         if i==2 and x!=d:
             print("c'est bon ou ra9m eli ml9itoch howa ",d)
             print("goode by 4odwa game o5ra ")

else:
    print("good by ")