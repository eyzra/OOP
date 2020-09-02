class parent:
    def __init__(self, fname, fage):
        self.name = fname
        self.age = fage

    def view(self):
        print(self.name, self.age)

class parent2: #'''This class was created to show multiple inheritance'''
    def __init__(self, height, color):
        self.height = height
        self.color = color

    def show(self):
        print(self.height, self.color)

class child(parent, parent2):
    def __init__(self, fname, fage, height, color):
        parent.__init__(self, fname, fage)
        parent2.__init__(self, height, color)
        self.lastname = "Michael"
 
    def view(self):
        print(self.age, self.lastname, self.name)

p2 = child("Ezra", 18, 6.2, "Brown")

p2.show()