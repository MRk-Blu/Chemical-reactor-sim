# import numpy as np
# # from Error_Looper import numeric_converter

# def array_maker(t):
#     values = t.strip().split()
#     #print(f"listed input  {values}\n ")
#     a = np.array(list(map(numeric_converter,values)))
#     f_a =[f"{x:.2f}" for x in a]
#     print(f_a)
#     #print(f"Array {a}")
#     return a
    
# Mass = input("Mass\n")
# print(array_maker(Mass))