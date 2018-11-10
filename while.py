name=input("enter your name  ")
i=0
tc=""
sum=0
while i<len(name):
    if name[i] not in tc:
        tc+=name[i]
        print(f"   #   {name[i]}   :     {name.count(name[i])}")
    i+=1




