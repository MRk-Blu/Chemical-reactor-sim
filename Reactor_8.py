from copy import error
import math
import sys
import time
from datetime import datetime
from pathlib import Path
from pdb import run
from scipy.integrate import quad

folder_path=Path("chemical-reactor-sim")

class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, data):
        for stream in self.streams:
            stream.write(data)

    def flush(self):
        for stream in self.streams:
            stream.flush()

    def isatty(self):
        return True


log_dir = Path(r"folder_path/RunLogs")
log_dir.mkdir(parents=True, exist_ok=True)

run_stamp = datetime.now().strftime("%Y-%m-%d")
log_folder = log_dir / f"run_{run_stamp}"
log_folder.mkdir(parents=True, exist_ok=True)
log_file = log_folder / "Reactor Log.txt"
log_handle = log_file.open("w", encoding="utf-8")

original_stdout = sys.stdout
sys.stdout = Tee(original_stdout, log_handle)

print(f"Logging to: {log_file}")

# addressing modes
Mode = input("""Mode:
1:Add
2:drain
3:heat
4:cool
""")
Chemical_name = input("Chemical:")
Current_temperature = input("Current Temperature:")
Enviroment_temperature = input("Enviroment Temperature:")
k = float(input("K: "))


class safety_parameters:
    def __init__(self, Chemical=Chemical_name, Temperature=float(Current_temperature)):
        self.name = Chemical
        self.temperature = Temperature
        if Mode == 1 or Mode == 2:
            self.Required_temperature = None
        else:
            self.Required_temperature = float(input("Required Temperature:"))
        self.max_temp = 1000
        self.min_temp = -300
        self.present = float(input("Current Amount:"))
        self.max_capacity = 10
        11
        self.t_enviroment = float(Enviroment_temperature)
        self.Chemical_Heat_limit = int(input("Chemical Heat Limit:"))
        self.Chemical_cool_limit = int(input("Chemical Cool Limit:"))

    def safety_check(self):
        timer = 0
        # added a safety check to ensure that the chemical is within the required temperature range
        # inputting overheat safety parameters
        if self.present > self.max_capacity:
            print(f"""Warning
The amount of the chemical{self.name} is too high""")
            print(f"""The maximum capacity limit is {self.max_capacity}
{Chemical_name} is at {self.present}
Removing chemical from Reactor""")
            while self.present > self.max_capacity - 20:
                time.sleep(1)
                self.present -= 10
                print(f"Removing chemical from Reactor: {self.present} Ltrs in Reactor")
        if (
            self.temperature > self.max_temp
            or self.temperature > self.Chemical_Heat_limit
        ):
            print(f"""Warning
            The temperature of the chemical{self.name} is too high""")
            if self.temperature > self.max_temp:
                print(f"""The maximum temperature limit is {self.max_temp}
{Chemical_name} is at {self.temperature}""")
            elif self.temperature > self.Chemical_Heat_limit:
                print(
                    f"""The maximum temperature limit for {self.name} is {self.Chemical_Heat_limit}
{Chemical_name} is at {self.temperature}"""
                )
            print("Activating Emergency Cooling System")

            while timer < 60 and (
                self.temperature > self.max_temp
                or self.temperature > self.Chemical_Heat_limit
            ):

                time.sleep(1)
                timer += 1
                self.t_enviroment -= 40
                self.temperature -= k * (self.temperature - self.t_enviroment)
                print(
                    f"Emergency cooler Activated Enviromental Temperature = {self.t_enviroment}"
                )
                print(
                    f"in{timer} Seconds: Chemicals Temperatuere is {self.temperature}℃"
                )
                if (
                    self.temperature < self.max_temp
                    and self.temperature < self.Chemical_Heat_limit
                ):
                    print(f"""The temperature of the chemical{self.name} is now safe""")

                elif (
                    self.temperature > self.max_temp
                    or self.temperature > self.Chemical_Heat_limit
                ):
                    print(f"""Warning
                    The temperature of the chemical{self.name} is still too high
                    Remove Chemical
                    Terminating Process""")
        if (
            self.temperature < self.min_temp
            or self.temperature < self.Chemical_cool_limit
        ):
            timer = 0
            print(f"""Warning
            The temperature of the chemical{self.name} is too low""")
            if self.temperature < self.min_temp:
                print(f"""The minimum temperature limit is {self.min_temp}
{Chemical_name} is at {self.temperature}""")
            elif self.temperature < self.Chemical_cool_limit:
                print(
                    f"""The minimum temperature limit for {self.name} is {self.Chemical_cool_limit}
{Chemical_name} is at {self.temperature}"""
                )

            print("Activating Emergency Heating System")
            while timer < 60 and (
                self.temperature < self.min_temp
                or self.temperature < self.Chemical_cool_limit
            ):

                time.sleep(1)
                timer += 1
                self.t_enviroment += 40
                self.temperature += k * (self.t_enviroment - self.temperature)
                print(
                    f"Emergency heater Activated Enviromental Temperature = {self.t_enviroment}"
                )
                print(
                    f"in{timer} Seconds: Chemicals Temperatuere is {self.temperature}℃"
                )
                if (
                    self.temperature > self.min_temp
                    and self.temperature > self.Chemical_cool_limit
                ):
                    print(f"""The temperature of the chemical{self.name} is now safe""")

                elif (
                    self.temperature < self.min_temp
                    or self.temperature < self.Chemical_cool_limit
                ):
                    print(f"""Warning
                    The temperature of the chemical{self.name} is still too low
                    Remove Chemical
                    Terminating Process""")


class Reactor(safety_parameters):
    def __init__(self, Chemical=Chemical_name, Temperature=float(Current_temperature)):
        super().__init__(Chemical, Temperature)
        self.name = Chemical
        self.run_time = float(input("Run Time:"))
        self.temperature = Temperature
        self.Chemical_density = float(input("Chemical Density:"))
        self.Chemical_mass = self.present * self.Chemical_density
        self.k = k

    def loss(self, x):
        return self.t_enviroment + (self.temperature - self.t_enviroment) * math.exp(
            -self.k * x
        )

    # inputting functions to add and drain chemicals from the reactor
    def add_Chem(self):
        rate = input("Rate:")
        print(f"---Adding {self.name} to Reactor")
        Expected_Amm = self.present + (float(rate) * float(self.run_time))

        timer = 0

        while timer < float(self.run_time) and self.present < Expected_Amm:
            time.sleep(1)
            self.present += float(rate)
            timer += 1
            print(f"{timer} Seconds : {self.present} Ltrs in Reactor")
        if self.present == Expected_Amm:
            return f"""The Chemical has been added
            {self.present}  of {self.name} gallons in Reactor"""
        if self.present > self.max_capacity:
            return """ Warning
            Reactor OverLoad"""
        return "Addition Complete"

    def drain(self):
        rate = input("Rate:")
        run_time = input("Run Time:")
        print("---Draining Reactor---")
        Expected_Remainder = self.present - (float(rate) * float(run_time))

        timer = 0

        while timer < float(run_time) and self.present > Expected_Remainder:
            time.sleep(1)
            self.present -= float(rate)
            timer += 1
            if self.present < 0:
                self.present = 0
            print(f"{timer} Seconds : {self.present} Ltrs in Reactor")
        if self.present == Expected_Remainder:
            return f"""Chemical removed
            {self.present} of {self.name} in Reactor
        """
        return "Drain Complete"

    def heater(self):
        current = float(input("Current:"))
        voltage = float(input("voltage:"))
        print(f"---Heating {self.name} in Reactor---")

        runtime = self.run_time

        def cooling_rate(t):
            return -self.k * (self.loss(t) - self.t_enviroment)

        total_loss, error = quad(cooling_rate, 0, runtime)

        print(
            f"Total temperature loss over {runtime} seconds = {abs(total_loss):.2f} °C"
        )
        return abs(total_loss)

        expected_temperature = (current * voltage * runtime) - total_loss

    def cooler(self):
        coolant = -10
        print(f"---Cooling {self.name} in Reactor---")

        runtime = self.run_time
        timer = 0

        def cooling_rate(t):
            return -self.k * (self.loss(t) - self.t_enviroment)

        total_loss, error = quad(cooling_rate, 0, runtime)
        print(
            f"Total temperature change over {runtime} seconds = {abs(total_loss):.2f} °C"
        )

        expected_temperature = self.temperature + total_loss

        while timer < runtime:
            time.sleep(1)
            timer += 1

            if coolant < 0:
                self.temperature += coolant * self.k
            else:
                self.temperature += -self.k * (self.temperature - self.t_enviroment)

            if self.temperature <= self.t_enviroment:
                self.temperature = self.t_enviroment

            if coolant > 0:
                coolant -= 0.5
            else:
                coolant += 0.5

            print(
                f"{timer} Seconds : Temperature = {self.temperature:.2f}℃ | Coolant = {coolant:.2f}"
            )

        self.temperature = expected_temperature
        print(f"Expected temperature after cooling = {self.temperature:.2f} °C")
        return f"Cooling Complete. Final temperature = {self.temperature:.2f}℃"


Reactor_test = Reactor()

try:
    if Mode == "1":
        print(Reactor_test.add_Chem())
    elif Mode == "2":
        print(Reactor_test.drain())
    elif Mode == "3":
        print(Reactor_test.heater())
    elif Mode == "4":
        print(Reactor_test.cooler())
finally:
    sys.stdout = original_stdout
    log_handle.close()
    print(f"\nLog saved to {log_file}")
