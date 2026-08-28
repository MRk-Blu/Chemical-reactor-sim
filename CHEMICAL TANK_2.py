from manim import *
class ChemicalTank:
    def __init__(self,Chemical_name,rate=5):
        self.name=Chemical_name
        self.max_capacity=20
        self.rate=rate
        self.initial_gallons=0
    def current_rate(self,rate_change):
        self.new_rate=self.rate+rate_change
        if self.new_rate>0:
            return "The current rate of flow is "+str(self.new_rate)+" gallons per minute"
        elif self.new_rate==0:
            return "Pumping Stopped"
    def add_liquid(self,time):
        self.current_gallons=self.initial_gallons+(self.rate*time)
        if self.current_gallons>self.max_capacity:
            return str(self.current_gallons)+" gallons of "+self.name+''' in tank 
            WARNING: TANK OVERFLOW '''
        else:
            return str(self.current_gallons)+" gallons of "+self.name+" in tank"
    def drain(self,rate=2,time=5):
        self.current_gallons_after_removal=self.current_gallons-(rate*time)
        if self.current_gallons_after_removal==0:
            return "tanks is now empty"
        else:
            return "The current amount is"+str(self.current_gallons_after_removal) +f"of {self.name} gallons"
    
Reaction_1=ChemicalTank("Mecury",2)
Current_rate=Reaction_1.current_rate(3)
Current_amount=Reaction_1.add_liquid(11)
Current_amount_2=Reaction_1.drain(3,10)

acid_name="H_{2}SO_{4}"
Acid_tank=ChemicalTank(acid_name)
current_ammount_for_acid=Acid_tank.add_liquid(0)
Current_amount_2_for_acid=Acid_tank.drain()
print(Current_amount_2_for_acid)