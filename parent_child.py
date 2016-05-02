class Name:
    def last_name(self):
        print("OWaboye")

class Info(Name):
    def first_name(self):
        print("kayode")

class Informa(Name, Info):
    def middle_name(self):
        print("kazeem")

p = Name()
r = Info()
q = Informa()

q.middle_name()
q.last_name()
q.first_name()
p.last_name()
r.first_name()
r.last_name()



