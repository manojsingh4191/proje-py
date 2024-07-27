# count=0
a=int(input("enter any no "))
# for i in range (2,a,1):
#     if (a%i==0):
#         count=count+1   
# if(count>=1):
#     print("non prime number ")
# else:
#     print ("the number prime")
b=a
noto=0
while (2<b):
    b=b-1
    if (a%b==0):
        noto=noto+2
if(noto>=2):
    print("non prime")
else:
    print("prime")

