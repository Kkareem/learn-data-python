class partyAnimal:
    def __init__(self, name):
        self.x=0
        self.name = name
        print(self.name, "constructed")
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

class sportsAnimal(partyAnimal):
    def __init__(self, name):
        super().__init__(name)
        self.points = 0
    def sports(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

s= partyAnimal("Fido")
s.party()
j=sportsAnimal("Jerry")
j.party()
j.sports()
