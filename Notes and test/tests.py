# This file was used to test how i could iterate over the black-scholes formula
# to output the different prices given different values for the compared variables
# while keeping the other variables constant

import numpy as np
from blackscholes import blackscholes

class INPUTS:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

inputs = INPUTS()

inputs.S = 100          
inputs.K = 120.0
inputs.r = 4.5
inputs.T = 60
inputs.sigma = 20.0


type = "Call"

x_vals = np.linspace(80.0, 120.0, 9)        #9 wil be chosen by the user to have a m x n heatmap
y_vals = np.linspace(10, 60, 9)

Z = np.empty((len(x_vals), len(y_vals)))

choice_1 = "Stock price"
choice_2 = "Time to expiry"

for i, y in enumerate(y_vals):
    for j, x in enumerate(x_vals):

        
        args = {
            "Stock price": inputs.S,
            "Strike price": inputs.K,
            "Risk-free rate": inputs.r,
            "Time to expiry": inputs.T,
            "Volatility": inputs.sigma,
        }
        
        args[choice_1] = x
        args[choice_2] = y

        
        S = args["Stock price"]
        K = args["Strike price"]
        r = args["Risk-free rate"] / 100 
        T = args["Time to expiry"] / 365 
        sigma = args["Volatility"] / 100 

        
        Z[i, j]  = blackscholes(S, K, r, T, sigma, type)


print(Z)