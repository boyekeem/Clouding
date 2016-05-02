def dating_age(age):
    while   age >18:
        allowed_age = age*0.5 + 10
        return allowed_age
print('enter the number of grapes sold')
a= input()
def new(a):
    b=100


    b-=a
    print('the stock ba1lance is ',b)

def new1(x='HELLO', y='world'):
    if x=='m':
        print('male',y)
    elif x=='f':
        print('female',y)
    else:
        print(x, ' ', y)


new(a)
new1('m', 'rules')



for n in range(10,50):
    a= dating_age(n)
    if n>=18:
        print('my age is ',n , ' and my allowed girl\'s age is ',a)
    else:
        print("you are still ", n, 'years old and not mature enough to have a girl friend')