# Code ERROR's

## First issue

### Numpy array incompatibility @ Error looper

#### _Error Dialogue_

Currently the arraying function works well with converting mutiple inputs into numpy arrays but the arrays are in string format and as such cannot be used in mathematical operations the cause of this error seem to be coming from the numeric converter function within the Error looper file.
eg.

```python
1 import numpy as np
2 from Error_Looper import numeric_converter
3
4 def arraying(t):
5     values = t.strip().split(" ")
6     print(values)
7     a = np.array(values)
8     print(a)
9     print(type(a))
10    f=numeric_converter(a)
11    print(f)

12 Mass = "10 20 30 40 "
13 arraying(Mass)
```

The output is as follows :

```python
PS C:\BLU\python learning\Chemical-reactor-sim-Remodeled> & C:\Users\HP\AppData\Local\Microsoft\WindowsApps\python3.13.exe "c:/BLU/python learning/Chemical-reactor-sim-Remodeled/Array_maker.py"
['10', '20', '30', '40']
['10' '20' '30' '40']
<class 'numpy.ndarray'>
Error
Input not a numeric value
Input a 'numeric_value'
```

As seen the code runs with no Error inparticular but the output is not what was anticipated.From the code layout and the output it is ccleary seen that the error comes when wetry to call the 'numeric_value' function an using the array 'a', thus showing the incompatibilty with the 'numeric_converter' function  and the numpy array type.

The code for the numeric converter is as follows

```python
def numeric_converter(t):
    counter = 0

    while True:
        try:
            s=int(t)
            break
        except:
            print("Error\nInput not a numeric value")
            t = input("Input a numeric value\n")
            counter += 1
        if counter == 10:
            print("Errors made too many")
            break
    return s
```

#### _Possible Fixes (PF)_

PF 1.
 Cause the arraying function to loop through the list calling the 'numeric_converter' function for each value of the list and add it to a new list
 for example :

```python
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
```

The output is as follows:

```python
PS C:\BLU\python learning\Chemical-reactor-sim-Remodeled> & C:\Users\HP\AppData\Local\Microsoft\WindowsApps\python3.13.exe "c:/BLU/python learning/Chemical-reactor-sim-Remodeled/Array_maker.py"
['10', '20', '30', '40']
interger_list [10]
interger_list [10, 20]
interger_list [10, 20, 30]
interger_list [10, 20, 30, 40]
array [10 20 30 40]
<class 'numpy.ndarray'>
```

From the output it is seen that this method bypasses the Error cleanly.

## Second Error

### Code incompatibility with float inputs @ Error looper

#### _Error Dialogue_

When an ```Integer``` is passed  as an arguments for the ```numeric_converter``` the code runs as intended,but when a ```float``` is passed as one the code brings up a form of logic error, where as instead of the code to convert the numeric flot sting to an interger value it output the fail safe for when the input is a text.

For example

```python
import math as mt
def numeric_converter(t):
    counter = 0

    while True:
        try:
            s=int(t)
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

```

the output of the preceeding is as follows

```python
Error
Input not a numeric value
Input a numeric value
```

were as the input was a numeric value but a string
