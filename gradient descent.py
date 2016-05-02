x1=3
x2=5
error=0.00000001
step=0.001



def gd(x1):


    H_x= (5*(x1**3.5))- (9*(x1**3))
    return H_x

while abs(x2-x1)>error:
        x1=x2
        x2=x1-(step*gd(x1))
        print (x1,"\n")
        print x2



gd(x1)
