import time
from scipy.integrate import quad


# inuting storage class
Chemical=input("Chemical:")
initial=input("initial temp:")
rate=input("rate:")
run_time=input("time:")
class StorageUnit:
    def __init__(self, Chemical, initial):
        self.name = Chemical
        self.max = 1000
        self.present = initial

    # inputing functions to add and drain chemicals from the storage unit
    def add_Chem(self, rate, run_time):
        print(f"---Adding{self.name} to tank")
        Expected_Amm = self.present + (rate * run_time)

        timer = 0

        while timer < run_time and self.present < Expected_Amm:
            time.sleep(1)
            self.present += rate
            timer += 1
            print(f"{timer} Seconds : {self.present} Ltrs in tank")
        if self.present == Expected_Amm:
            return f"""The Chemical has been added
            {self.present}  of {self.name} gallons in tank"""
        if self.present > self.max:
            return """ Warning
            Tank OverLoad"""
        return "Addition Complete"

    def drain(self, rate, run_time):
        print("---Draining Tank---")
        Expected_Remainder = self.present - rate * run_time

        timer = 0

        while timer < run_time and self.present > Expected_Remainder:
            time.sleep(1)
            self.present -= rate
            timer += 1
            if self.present < 0:
                self.present = 0
            print(f"{timer} Seconds : {self.present} Ltrs in tank")
        if self.present == Expected_Remainder:
            return f"""Chemical removed
            {self.present} of {self.name} in tank
        """
        return "Drain Complete"


# inputing temperature class
class Heat_Safety:
    def __init__(self, Heat_limit, Cold_limit, Initial_temp, Enviroment=25, k=0.05):

        self.Hl = Heat_limit
        self.Cl = Cold_limit
        self.T = Initial_temp
        self.T_env = Enviroment
        self.k = k

    # adding a thermostat function to the temperature class to monitor the temperature of the chemical in the tank
    def safety_parameters(self):
        timer = 0
        if self.T > self.Hl:
            print("""Warning: Heat Limit Exceeded
            Activating Safety Cooler imaediately""")
            for _ in range(60):
                time.sleep(1)
                timer += 1
                self.T_env -= 40
                self.T -= self.k * (self.T - self.T_env)
                print(
                    f"Emergency cooler Activated Enviromental Temperature = {self.T_env}"
                )
                print(f"in{timer} Seconds: Chemicals Temperatuere is {self.T}℃")

        if self.T < self.Cl:
            timer = 0
            print(""" Warning: Chemicals Temperature balow cold limit
            Activating Safety Heater imaediately
            """)
            for _ in range(60):
                time.sleep(1)
                timer += 1
                self.T_env += 40
                self.T += self.k * (self.T_env - self.T)
                print(
                    f"Emergency Heater Activated Enviromental Temperature = {self.T_env}"
                )
                print(f"in{timer} Seconds: Chemicals Temperatuere is {self.T}℃")


# Adding Temperature Alternator class to the temperature class to alternate the temperature of the chemical in the tank to desired requirements
class Temp_Alternator(Heat_Safety):
    def __init__(
        self,
        Chemical,
        Mass,
        SpecifIc_Heat_c,
        Latent_heat_F,
        Latent_heat_V,
        temperature,
        Temp_env=25,
        Hot_limit=1000,
        Cold_limit=-300,
        current=1,
        Voltage=220,
        run_time=60,
    ):
        self.name = Chemical
        self.M = Mass
        self.S_c = SpecifIc_Heat_c
        self.L_f = Latent_heat_F
        self.L_v = Latent_heat_V
        self.T = temperature
        self.T_env = Temp_env
        self.Hl = Hot_limit
        self.cl = Cold_limit
        self.I = current
        self.V = Voltage
        self.t = run_time
        self.total_Heat_input = self.I * self.V * self.t
        super().__init__(Hot_limit, Cold_limit, temperature, Temp_env)

    def loss(self, run_time):
        return self.k * ((self.T + self.total_Heat_input) - self.T_env)

    def Heater(self, run_time):
        print(f"---Heating {self.name} to desired temperature---")
        total_loss, error = quad(self.loss, 0, run_time)
        Expected_Temp = (
            self.T + self.total_Heat_input / (self.M * self.S_c) - total_loss
        )
        timer = 0
        dt = 0

        while timer < run_time and self.T < Expected_Temp:
            time.sleep(1)
            current_heat = self.I * self.V
            instant_loss = self.k * ((self.T + current_heat - self.T_env) * dt)
            self.T += current_heat / (self.M * self.S_c) - instant_loss
            timer += 1
            dt += 1
            print(f"{timer} Seconds : {self.T}℃ in tank")
        if self.T >= Expected_Temp:
            return f"""The Chemical has been heated
            {self.T}  of {self.name} ℃ in tank"""
        if self.T > self.Hl:
            return """ Warning
            Heat Limit Exceeded"""
        return "Heating Complete"

Storage_test=StorageUnit()
add_test=Storage_test.add_Chem()
print(add_test)
