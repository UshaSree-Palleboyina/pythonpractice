a=int(input("enter number:"))
b=int(input("enter start range:"))
c=int(input("enter stop range:"))
d=int(input("enter step:"))
for i in range(b,c+1,d):
    print(a,"x",i,"=",a*i)
