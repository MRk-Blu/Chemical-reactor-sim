from copy import error
import math
import sys
import time
from datetime import datetime
from pathlib import Path
from pdb import run
from scipy.integrate import quad

from Reactor_6 import LatentHeat_of_vaporisation


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


log_dir = Path(r"C:\BLU\DOCS")
log_dir.mkdir(parents=True, exist_ok=True)

run_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
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
        self.max_capacity = 1000
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

class capacites:
    def __init__(
        self,
        chemical_name=Chemical_name,
        Specific_heat_capacity=None,
        LatentHeat_of_fusion=None,
        LatentHeat_of_vaporisation=None,
    ):
        self.name = str(chemical_name).strip().lower()
        heat_data = {
            "hydrogen": (14.304, 58.0, 449.0),
            "helium": (5.193, 21.0, 20.9),
            "lithium": (3.582, 295.0, 8700.0),
            "beryllium": (1.825, 12100.0, 11400.0),
            "boron": (1.026, 4990.0, 5500.0),
            "carbon": (0.709, 0.0, 0.0),
            "nitrogen": (1.040, 25.7, 199.1),
            "oxygen": (0.918, 13.9, 213.0),
            "fluorine": (0.824, 12.7, 59.0),
            "neon": (1.030, 26.2, 112.0),
            "sodium": (1.228, 113.0, 8970.0),
            "magnesium": (1.020, 297.0, 8360.0),
            "aluminium": (0.897, 398.0, 10500.0),
            "silicon": (0.705, 1800.0, 8580.0),
            "phosphorus": (0.710, 144.0, 510.0),
            "sulfur": (0.710, 38.0, 572.0),
            "chlorine": (0.479, 25.0, 169.0),
            "argon": (0.520, 27.6, 161.0),
            "potassium": (0.757, 65.0, 3800.0),
            "calcium": (0.647, 184.0, 13400.0),
        }
        if Specific_heat_capacity is not None or LatentHeat_of_fusion is not None or LatentHeat_of_vaporisation is not None:
    # someone passed manual values — use them (with 0.0 for any left blank)
            self.Cp = Specific_heat_capacity if Specific_heat_capacity is not None else 0.0
            self.Lf = LatentHeat_of_fusion if LatentHeat_of_fusion is not None else 0.0
            self.Lv = LatentHeat_of_vaporisation if LatentHeat_of_vaporisation is not None else 0.0
        else:
            # no manual values — look it up
            result = heat_data.get(self.name)
            if result is None:
                print(f"Warning: no heat data found for '{self.name}'")
                self.Cp = self.Lf = self.Lv = None
            else:
                self.Cp, self.Lf, self.Lv = result
    def summary(self):
        return (
            f"Chemical: {self.name.title()} | Cp = {self.Cp} J/(g·K) | "
            f"Latent Heat of Fusion = {self.Lf} kJ/kg | "
            f"Latent Heat of Vaporisation = {self.Lv} kJ/kg"
        )

class Reactor(safety_parameters,capacites):
    def __init__(self, Chemical=Chemical_name, Temperature=float(Current_temperature)):
        super().__init__(Chemical, Temperature)
        super().__init__(Chemical)
        self.name = Chemical
        self.run_time = float(input("Run Time:"))
        self.temperature = Temperature
        self.Chemical_density = float(input("Chemical Density:"))
        self.Chemical_mass = self.present * self.Chemical_density
        self.k = k
        self.capacity = capacites(self.name)
        print(self.capacity.summary())

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
