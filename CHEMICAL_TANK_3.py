class ChemicalTank:
    def __init__(self,Chemical_name,rate=20):
        self.name=Chemical_name
        self.max_capacity=1000
        self.rate=rate
        self.initial_gallons=0
    def current_rate(self,rate_change=5):
        self.new_rate=self.rate+rate_change
        if self.new_rate>0:
            return "The current rate of flow is "+str(self.new_rate)+" gallons per minute"
        elif self.new_rate==0:
            return "Pumping Stopped"
    def add_liquid(self,rate=10,time=5):
        self.current_gallons=self.initial_gallons+(rate*time)
        if self.current_gallons>self.max_capacity:
            return str(self.current_gallons)+" gallons of "+self.name+''' in tank 
            WARNING: TANK OVERFLOW '''
        else:
            return str(self.current_gallons)+" gallons of "+self.name+" in tank"
    def drain(self,rate=10,time=6):
        self.current_gallons_after_removal=self.current_gallons-(rate*time)
        if rate*time>self.current_gallons:
            return "invalid time input for drain, check and try again" 
        if self.current_gallons_after_removal==0:
            return "tanks is now empty"
        else:
            return "The current amount is "+str(self.current_gallons_after_removal)+" gallons"

class Reaction:
    def __init__(self,Initial_temp=25,reactants={}):
        self.Reactants=reactants
        self.initial_temp=Initial_temp
    def Heat_change(self,change_in_heat=10):
        self.New_temp=self.initial_temp+change_in_heat
        while self.New_temp < 200 :
            return "Reaction temperature optimum"
        while self.New_temp == 200:
            return '''Temperature critical
            Overheating eminent
            Applying coolant'''
        if self.New_temp>200 :
            return '''Over heating
            Applying coolant'''
        if self.New_temp>= 1000 :
            return '''Tmperature going SUPERNOVA
            Terminating reation
            aplplying coolant'''
        