#第一題
def one(name,age):
    print (name,age)
#第二題
def two(*num):
    print(num)
#第三題
def three(a,b):
    add=a+b
    reduce = a - b
    print(a,b)
#第四題
def four(name,num=9000):
    print("姓名:",name,"薪水:",num)
#第五題
def five(a,b):
    def five_add(a,b):
        return a+b
    c = five_add(a,b)
    print(c+5)
#第六題
def six(num):
    if num == 1:
        return 1
    else:
        return six(num-1)+num
#第七題
def seven(name, age):
    print (name,age)
seven2 = seven
#第八題
def eight():
    print(list(range(4,30,2)))
#第九題
def nine(num):
    print(max(num))
one("joson",18)
two(3,7,9,15)
three(5,9)
four("joson",500)
four("jo")
five(5,10)
six(10)
seven2("joson",18)
eight()
num=[5,50,63,7,9,48,100,20,11]
nine(num)