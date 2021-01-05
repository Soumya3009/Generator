class Emp:
    def __init__(self, first, last):
        self.first=first
        self.last=last
        self.email=first+"."+last+"@gmail.com"
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
obj=Emp("Abinash", "Mishra")
print(obj.first)
print(obj.last)
print(obj.email)
print(obj.fullname())
obj.first="Soumya"
print(obj.first)
print(obj.last)
print(obj.email)
print(obj.fullname())

