def test1(a,*m,b=20):
    print(a)
    print(type(m))
    print(b)

test1("hello",1,1,2,4)

a = 100
def test2():
    global a #有没有这句话，区别很大
    a = 300
    print(a)

test2()
print(a)