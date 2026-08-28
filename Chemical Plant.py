import time
class ChemicalTank:
    def __init__(self,Chemical,rate=5,initial=0):
        self.name=Chemical
        self.Max_capacity=1000
        self.rate=rate
        self.present=initial

    def adding_Chem(self,rate_2,time_to_add):
        print(f"--- Adding {self.name} to Tank")
        Total_Chem=self.present+(rate_2*time_to_add)
        
        timer=0

        while timer < time_to_add and Total_Chem > self.present :
            time.sleep(1)
            self.present += rate_2
            timer += 1
            if self.present < 0 :
                self.present=0
            print(f"{timer} Second : {Total_Chem - self.present} Ltrs remaining")
        if self.present == Total_Chem :
            return "The Chemical has been Added"
        return "Addition Complete"
    
Chemical_1="HCl"
tanka_1=ChemicalTank(Chemical_1,initial=15)
print(tanka_1.adding_Chem(10,15))