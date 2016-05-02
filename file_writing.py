Txting = open("ka.txt", 'w')
Txting.write("I am loving this python programming shii\t")
Txting.write("NO! youre not")
Txting.close()

Reading = open("ka.txt", 'r')
display = Reading.read()
print(display)
Reading.close()

