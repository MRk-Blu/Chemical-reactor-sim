import time
from scipy.integrate import quad

# inuting storage class
Mode = input("Mode:")
Type = input("Type:")
Chemical_name = input("Chemical:")
Initial_temperature = input("Initial Temperature:")


class StorageUnit:
    Initial_ammount = input("Initial Ammount:")

    def __init__(self, initial=float(Initial_ammount), Chemical=Chemical_name ):
        self.name = Chemical
        self.max = 1000
        self.present = initial

    # inputing functions to add and drain chemicals from the storage unit
    def add_Chem(self):
        rate = input("Rate:")
        run_time = input("Run Time:")
        print(f"---Adding{self.name} to tank")
        Expected_Amm = self.present + (float(rate) * float(run_time))

        timer = 0

        while timer < float(run_time) and self.present < Expected_Amm:
            time.sleep(1)
            self.present += float(rate)
            timer += 1
            print(f"{timer} Seconds : {self.present} Ltrs in tank")
        if self.present == Expected_Amm:
            return f"""The Chemical has been added
            {self.present}  of {self.name} gallons in tank"""
        if self.present > self.max:
            return """ Warning
            Tank OverLoad"""
        return "Addition Complete"

    def drain(self):
        rate = input("Rate:")
        run_time = input("Run Time:")
        print("---Draining Tank---")
        Expected_Remainder = self.present - (float(rate) * float(run_time))

        timer = 0

        while timer < float(run_time) and self.present > Expected_Remainder:
            time.sleep(1)
            self.present -= float(rate)
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
    def __init__(
        self,
        Heat_limit,
        Cold_limit,
        Initial_temp=float(Initial_temperature),
        Enviroment=25,
        k=0.05,
    ):

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
    time_for_action = input("Enter run time: ")
    Current = input("Enter current: ")
    Voltage = input("Enter voltage: ")

    def __init__(
        self,
        Chemical,
        Mass,
        SpecifIc_Heat_c,
        Latent_heat_F,
        Latent_heat_V,
        temperature=float(Initial_temperature),
        Temp_env=25,
        Hot_limit=1000,
        Cold_limit=-300,
        current=float(Current),
        voltage=float(Voltage),
        run_time=float(time_for_action),
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
        self.V = voltage
        self.t = run_time
        self.total_Heat_input = self.I * self.V * self.t
        super().__init__(Hot_limit, Cold_limit, temperature, Temp_env)

    def loss(self, run_time=float(time_for_action)):
        return self.k * ((self.T + self.total_Heat_input) - self.T_env)

    def Heater(self, run_time=float(time_for_action)):
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
            {self.T}  of {self.name} ℃ in {timer} Seconds in tank"""
        if self.T > self.Hl:
            return """ Warning
            Heat Limit Exceeded"""
        return "Heating Complete"


Storage_test = StorageUnit()
add_test = Storage_test.add_Chem()
print(add_test)
reaction = Temp_Alternator(
    Chemical=Chemical_name,
    Mass=10,
    SpecifIc_Heat_c=4.18,
    Latent_heat_F=334,
    Latent_heat_V=2260,
)
print(reaction.Heater())