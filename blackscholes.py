import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import streamlit.components.v1 as components


def blackScholes(S, K, r, T, sigma, type):

    #Calculate Black Scholes option price for a call/put

    d1 = (np.log(S/K) + (r+sigma**2/2)* T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    try:
        if type == "c":
            price = S * norm.cdf(d1, 0, 1) - K* np.exp(-r * T) * norm.cdf(d2, 0, 1)
        
        elif type == "p":
            price = K * np.exp(-r*T) * norm.cdf(-d2, 0, 1) - S * norm.cdf(-d1, 0, 1)

        return price
    
    except: print("Please confirm alloption parameters")