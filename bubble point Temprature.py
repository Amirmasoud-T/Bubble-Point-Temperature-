#calculating bubble point temperature with antoine equationn using python
import math
import numpy as np  
import pandas as pd    #import necessary libraries
quantity = int(input('number of components : ')) #number of your liquid components
x_value = np.array([]) #value of youre liquid components 
for i in range(quantity):
    x = float(input(f'x{i+1} = '))
    x_value =  np.append(x_value,x) #add value of liquid components to your array that define in line 6
P = float(input('Enter the Pressure : ')) #get total pressure
print(f'pressure is {P} kpa')
A = np.zeros(quantity)
B = np.zeros(quantity)
C = np.zeros(quantity) #A,B,C is antoine equation constants
for i in range(quantity): #use for loop to returns antoine equation constants
    A[i] = float(input(f'A{i+1} is: '))
    B[i] = float(input(f'B{i+1} is: '))
    C[i] = float(input(f'C{i+1} is: '))
saturation_T = np.array([]) #calculates saturation temperature from pressure
for i in range(quantity): 
    TS = (B[i]/(A[i]-math.log(P))-C[i])
    saturation_T = np.append( saturation_T,TS) #calculates saturation temperature for all components and add to array which is define in line 19
for i in range(quantity):
    print(f'T{i+1}S is { saturation_T[i]}') #prints saturation temperature that calculated in before for loop
T0 = np.sum(x_value* saturation_T) #calculates first Temperature
Selective_component = int(input('selective component is : ')) #selective components that you want to calculate nexts stages by this component
print(f'selective component (between 1,{quantity} ) is number {Selective_component}')
alphas = [] #activity coefficients
for i in range(quantity):
    alpha = np.exp((A[i]-(B[i]/(T0+C[i])))-(A[Selective_component-1]-(B[Selective_component-1]/(T0+C[Selective_component-1]))))
    alphas.append(alpha.round(3)) #add alpha values to line 28 lists
PS = (P/(np.sum(x_value*alphas))).round(3) #calculate selective components saturation pressures
new_T_1 = ((B[Selective_component-1]/(A[Selective_component-1]-np.log(PS)))-C[Selective_component-1]).round(3) #calculats new T by selective components saturation pressures
err = abs(new_T_1 - T0)
my_T = [T0,new_T_1]
PS_list = [PS]
my_alphas = [alphas]
while err>10**(-3):
    new_T = (B[Selective_component-1]/(A[Selective_component-1]-np.log(PS)))-C[Selective_component-1]
    new_alphas = []
    for i in range(quantity):
        new_alpha = (np.exp((A[i]-(B[i]/(new_T+C[i])))-(A[Selective_component-1]-(B[Selective_component-1]/(new_T+C[Selective_component-1]))))).round(4)
        new_alphas.append(new_alpha.round(3))
        my_alphas.append(new_alphas)
    PS = (P/(np.sum(x_value * np.array([new_alphas])))).round(3)
    PS_list.append(PS)
    new_2_T = (B[Selective_component-1]/(A[Selective_component-1]-np.log(PS)))-C[Selective_component-1]
    my_T.append((new_2_T).round(3))
    err = abs(new_2_T - new_T)
print(f'This is PS{Selective_component} list {PS_list}')
print(f'This is Temprature list {my_T}')
print(f'bubble point tempratuer is {(new_2_T).round(3)} C')
Table = pd.DataFrame(my_alphas[0:len(PS_list)],columns=[f'alpha{i+1}{quantity}' for i in range(quantity)])
Table[f'PS{Selective_component}'] = PS_list[0:len(PS_list)]
Table['Temprature'] = my_T[0:(len(PS_list))]
print(Table)
