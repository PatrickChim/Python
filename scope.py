a= 250

def f1():
    global a
    a = 100 #global
    print(a)

def f2():
    a = 50 #local
    print(a)
    
f1()
f2()
print(a)
