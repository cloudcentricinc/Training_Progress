x=int(input("enter the number: "))
a=0
b=1
if x<=0:
    print("the requested series is :")
else:
    print(a,b,end = "")
    for i in range(2,x):
        sum=a+b
        print(sum,end= " ")
        a=b
        b=sum