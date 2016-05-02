class   Naira:

    def pounds(self, x):

        self.amount = x * 410
        output = "The naira equivalent is "
        print(output+ str(self.amount))

    def dollars(self, x):

        self.amount = x * 250
        output = "The naira equivalent is "
        print(output+ str(self.amount))

    def Euro(self, x):

        self.amount = x * 280
        output = "The naira equivalent is "
        print(output+ str(self.amount))

r = Naira()
print("This system does the Naira conversion of currencies in dollars, pounds, and euro")
while 1<3:
    try:
        Conversion = raw_input('Enter the currency type to convert in lowercase pls\n')
        amt= int(input("Enter the Amount to convert\n"))
        if Conversion == "pounds":
            r.pounds(amt)
            break
        elif Conversion=="dollars":
            r.dollars(amt)
            break
        elif Conversion== "euro":
            r.Euro(amt)
            break
        else: print("you have not input the right info")


    except:
        print("please supply the right information ")
        print("Only letters for currency type and figures for amount")






