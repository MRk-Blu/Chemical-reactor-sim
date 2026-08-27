import time
class ChemicalTank:
    def __init__(
        self, Chemical=None, Current_gallons=0, max_capacity=1000, temperature=25.0
    ):
        self.name = Chemical
        self.max_capacity = max_capacity
        self.temp = temperature
        self.ammount = Current_gallons

    def add_liquid(self, rate=10, Time_to_add=60):
        print(f"---Adiing{self.name} to Reactor")
        Total_Chem = (rate * Time_to_add) + self.ammount

        Stopwatch = 0

        while Stopwatch < Time_to_add and Total_Chem > self.ammount:
            time.sleep(1)
            self.ammount += rate
            Stopwatch += 1
            if self.ammount < 0:
                self.ammount = 0
            print(f"{Stopwatch} Second : {self.ammount} Gallons in tank")
        if self.ammount == Total_Chem:
            return f"""The Chemical has been added
            {self.ammount}  of {self.name} gallons in tank"""
        return "Addition Complete"


Chemical_name = "HCl"
rate = 10
Storage = ChemicalTank(Chemical_name, rate)
Current_amount_2 = Storage.add_liquid(3, 20)
print("Chemical: " + Chemical_name)
print(Current_amount_2)
