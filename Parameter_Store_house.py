import numpy as np
import math as mt
def numeric_converter(t):
    counter = 0

    while True:
        try:
            s=float(t)
            round(s,2)
            break
        except:
            print("Error\nInput not a numeric value")
            t = input("Input a numeric value\n")
            counter += 1
        if counter == 10:
            print("Errors made too many")
            break
    return s
        
mass= "100.00"
print(numeric_converter(mass))

def arraying(t):
    l_a=[]
    values = t.strip().split(" ")
    print(values)
    for entities in values:
        integer_form=numeric_converter(entities)
        l_a.append(integer_form)
        print("interger_list",l_a)
    a = np.array(l_a)
    print("array",a)
    print(type(a))
    # f=numeric_converter(a)
    # print(f)

Mass = "10 20 30 40 "
arraying(Mass)
