class ChemicalTank:
    def __init__(self,chemical_name):
        self.name =chemical_name
        self.max_capacity=12
        self.current_gallons=0
    def add_liquid(self,amount):
        self.current_gallons=self.current_gallons+amount
        if self.current_gallons>self.max_capacity:
            return "WARNING: TANK OVERFLOW" 
        else:
            return str(self.current_gallons)+" gallons of "+self.name+" in tank"
Reaction_1=ChemicalTank("berylium")
print(Reaction_1.add_liquid(10))