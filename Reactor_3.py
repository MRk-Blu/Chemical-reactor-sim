import time
class ChemicalTank:
    def __init__(self,Chemical=None,Current_gallons=0,max_capacity=1000,temperature=25.0):
        self.name=Chemical
        self.max_capacity=max_capacity
        self.temp=temperature
        self.ammount=Current_gallons

    def add_liquid(self,rate=10,Time_to_add=60):
        print(f"---Adiing{self.name} to Reactor")
        Total_Chem = (rate*Time_to_add)+self.ammount

        Timer=0

        while Timer < Time_to_add and Total_Chem > self.ammount :
            time.sleep(1)
            self.ammount += rate
            Timer += 1
            if self.ammount < 0:
                self.ammount = 0
            print(f"{Timer} Second : {self.ammount} Gallons in tank")
        if self.ammount == Total_Chem :
            return f'''The Chemical has been added
            {self.ammount}  of {self.name} gallons in tank'''
        return "Addition Complete"

class TemperateAlternator:
    def __init__(
            self,Chemical,Mass,SpecifIc_Heat_c,Latent_heat_F,Latent_heat_V,temperature,Up_limit = 1000,Low_limit = -300
            ):
        self.name=Chemical
        self.M=Mass
        self.S_c=SpecifIc_Heat_c
        self.L_f=Latent_heat_F
        self.L_v=Latent_heat_V
        self.T=temperature
        self.Up=Up_limit
        self.Lw=Low_limit

    def Heater(self,Heat_input,Temp_env=25,run_time=None) :
        print(f"---Heating{self.name}---")
        E_ho=((Heat_input/(self.M*self.S_c))+self.T)
        
        if self.T==0:
            Heat_input-=self.M*self.L_f

        elif self.T==100:
            Heat_input-=self.M*self.L_v
        k=1.3806504*10**-23
        dt=0

        New_temp=(Heat_input)-(k*((Heat_input+self.T)-Temp_env)*dt)

        Timer=0

        while New_temp <E_ho and Timer<run_time and Heat_input > 0 :
            time.sleep(1)
            dt+=1
            Timer+=1
            
            if self.T==100 :
                Heat_input-=self.M*self.L_v
            elif self.T==0:
                Heat_input-=self.M*self.L_f
            print(f"{Timer} Seconds : Cureent Temperature is {self.T}℃, expected temperture = {New_temp}")

        if New_temp==E_ho or Heat_input==0 :
            return  f'''Heating Completed in {Timer} Seconds
The Chemicals Temperature is now {New_temp}℃'''
            def Heater(self,I=1,V=20,t=60) :
    
                k=1.3806504*10**-23
                loss=k*(I*V*t+self.T)-self.T_e
                limit=1000
    
                print("---Heating Chemical---")
                E_temp= ((I*V*t/(self.M*self.S_c)) - loss )
    
                timer=0
    
                dt=0
                Instanteneous_loss = k*(I*V*t+self.T)-self.T_e
    
                while timer < time and self.T < E_temp :
                    time.sleep(1)
                    timer+=1
                    dt+=1
                    self.T += I*V*timer/((self.M*self.S_c) - Instanteneous_loss*dt)
                    print(f"{timer} Seconds : {self.T}℃")
                if self.T >= limit:
                    return f''' ---Warning---
                Temperature={self.T}℃
                Activating Cooler
                '''
                if self.T==E_temp :
                    return f'''Chemical Heated
                Current Temperature is now {self.T}℃'''
                return "Heating Complete"

Liquid="H₂O"
Boil=TemperateAlternator(Liquid,Mass=100,SpecifIc_Heat_c=4200,Latent_heat_F=336000,Latent_heat_V=3.23*10**5,temperature=0.0)
print(Boil.Heater(Heat_input=2000*10**20,run_time=10))