import numpy as np
from scipy.integrate import quad
import time
class StorageUnit:
    def __init__(self,Chemical,initial=0):
        self.name=Chemical
        self.Max_capacity=1000
        self.present=initial

    def adding_Chem(self,rate,run_time):
        print(f"--- Adding {self.name} to Tank")
        Total_Chem=self.present+(rate*run_time)
        
        timer=0

        while timer < run_time and Total_Chem > self.present :
            time.sleep(1)
            self.present += rate
            timer += 1
            print(f"{timer} Seconds : {Total_Chem} Ltrs in tank")
        if self.present == Total_Chem :
            return f'''The Chemical has been added
            {self.ammount}  of {self.name} gallons in tank'''
       
        if self.present > self.Max_capacity :
            return ''' Warning
            Tank OverLoad'''
        return "Addition Complete"

    def drain(self,rate,run_time):
        print("---Draining Tank---")
        Expected_Remainder=self.present-rate*run_time

        timer=0

        while timer < run_time and self.present > Expected_Remainder :
            time.sleep(1)
            self.present-=rate
            timer += 1
            if self.present<0:
                self.present==0
            print(f"{timer} Seconds : {self.present} Ltrs in tank")
        if self.present==Expected_Remainder :
            return f'''Chemical removed
            {self.present} of {self.name} in tank
        '''
        return "Drain Complete"

class TemperateAlternator:
    def __init__(self,Chemical,Mass,SpecifIc_Heat_c,Latent_heat_F,Latent_heat_V,temperature,Temp_env=25,Hot_limit=1000,Cold_limit=-300):
        self.name=Chemical
        self.M=Mass
        self.S_c=SpecifIc_Heat_c
        self.L_f=Latent_heat_F
        self.L_v=Latent_heat_V
        self.T=temperature
        self.T_env=Temp_env
        self.Hl=Hot_limit
        self.cl=Cold_limit

    def thermostat(self):
        print("---Booting System---")

        print(f"---Thermostat Activated---\nCurrent Temperature is {self.T}℃")

        if self.T > self.Hl :
            return f'''WARNING Overheating
            Entry temp too high {self.T}℃'''
        elif self.T < self.cl :
            return f'''WARNING Overcooling
            Entry temp too low {self.T}℃
            Initializing Heaters Immediately'''
        else:
            print("""Temperature optimum
            Starting system""")

    def Heater(self,Current,Voltage,Run_time):
        print("---Heating Chemical---")
        I=Current
        V=Voltage
        t=Run_time

        Total_Heat_input=I*V*t

        k=0.05
        timer=0
        dt=0
        current_heat=I*V*timer
        current_loss=k*((current_heat+self.T)-self.T_env)*dt
        loss= k*((Total_Heat_input+self.T)-self.T_env)
        total_loss,absolute_error = quad(loss,0,Run_time)
        Expected_temp=Total_Heat_input/(self.M*self.S_c) - total_loss
        

        while timer < Run_time and self.T < Expected_temp  :
            time.sleep(1)
            timer+=1
            dt+=1
            self.T+= current_heat-current_loss
            print (f'''Seconds {timer} :
            Teperature is now {self.T}℃''')
        if self.T >= self.Hl :
            return f'''WARNING Overheating
            Entry temp too high {self.T}℃'''
        if self.T==Expected_temp:
            return f"""Temperature Request met with no Errors
            Temperature is now {self.T}"""
        return "Heating Completed"

reaction_1=TemperateAlternator("macury",Mass=10,SpecifIc_Heat_c=35,Latent_heat_F=40,Latent_heat_V=60,temperature=44)
print(reaction_1.Heater())


