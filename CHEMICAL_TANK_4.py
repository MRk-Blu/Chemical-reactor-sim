import time
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
        print("Draining "+str(rate*time)+" gallons of "+self.name+" from tank")

        timer=0
        while timer<time:
            timer+=1
            print("Draining "+str(rate)+" gallons of "+self.name+" from tank")
            time.sleep(1)
        self.current_gallons_after_removal=self.current_gallons-(rate*time)
        while self.current_gallons_after_removal > 0:
            return "The current amount is "+str(self.current_gallons_after_removal)+" gallons"
        if self.current_gallons_after_removal==0:
            return "The tanks is now empty"

        if self.current_gallons_after_removal<0:
            return '''Tank Empty
Terminating Drain'''
    
Chemical_name="HCl"
rate=10
Storage=ChemicalTank(Chemical_name,rate)
Current_rate=Storage.current_rate()
Current_amount=Storage.add_liquid()
Current_amount_2=Storage.drain(3,20)
print("Chemical: "+ Chemical_name)
print(Current_amount_2)