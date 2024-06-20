#calculating bubble point temperature with antoine equationn using python
import math
import numpy as np
quantity = int(input('number of components : '))
x_value = np.array([])
for i in range(quantity):
    x = float(input(f'x{i+1} = '))
    x_value =  np.append(x_value,x)
P = float(input('Enter the Pressure : '))
print(f'pressure is {P} kpa')
A = np.zeros(quantity)
B = np.zeros(quantity)
C = np.zeros(quantity)
for i in range(quantity):
    A[i] = float(input(f'A{i+1} is: '))
    B[i] = float(input(f'B{i+1} is: '))
    C[i] = float(input(f'C{i+1} is: '))
Saturated_T = np.array([])
for i in range(quantity): 
    TS = (B[i]/(A[i]-math.log(P))-C[i])
    Saturated_T = np.append(Saturated_T,TS)
for i in range(quantity):
    print(f'T{i+1}S is {Saturated_T[i]}')
T0 = np.sum(x_value*Saturated_T)
print(f'selectiv component is 3 by defult & T0(first guss for temprature is {T0})')
alphas = np.array([])
for i in range(quantity):
    alpha = math.exp((A[i]-(B[i]/(T0+C[i])))-(A[quantity-1]-(B[quantity-1]/(T0+C[quantity-1]))))
    alphas = np.append(alphas,alpha)
for i in range(quantity):
    print(f'alpha{i+1}3 = {alphas[i]}')
P3S = (P/(np.sum(x_value*np.array([alphas]))))
print(f'P{quantity}S is {P3S}')
new_T = (B[quantity-1]/(A[quantity-1]-np.log(P3S)))-C[quantity-1]
print(f'new temprature is {new_T}')
err = abs(new_T - T0)
my_T = []
while err > 10**(-3):
    new_T = (B[2]/(A[2]-np.log(P3S)))-C[2]
    new_alphas = np.array([])
    for i in range (quantity):
        new_alpha = math.exp((A[i]-(B[i]/(new_T+C[i])))-(A[quantity-1]-(B[quantity-1]/(new_T+C[quantity-1]))))
        new_alphas = np.append(new_alphas,new_alpha)
    P3S = (80 / (np.sum(x_value * np.array([new_alphas]))))
    new_T_2 = (B[quantity-1] / (A[quantity-1] - np.log(P3S))) - C[quantity-1]
    err = abs(new_T_2 - new_T)
print(F'bubble Point Temprature is {new_T} C')