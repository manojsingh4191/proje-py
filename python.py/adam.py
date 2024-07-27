#it is f()
def manoj(a,c,b):
    if c=="*":
        print(a*b)
    elif c=="/":
        print(a/b)
    elif c=="-":
        print(a-b)
    elif c=="+":
        print(a+b)
    else:
        print("enter thre corect value's ")

    return

#print the value 
a=int(input("enter 1st no."))
c=input("chuse +-*/:-")
b=int(input("enter 2nd no."))
manoj(a,c,b)


