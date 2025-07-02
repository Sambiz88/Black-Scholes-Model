import numpy as np
from math import log, sqrt, exp
from scipy.stats import norm
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import streamlit.components.v1 as components


def blackscholes(S, K, r, T, sigma):

    #Calculate Black Scholes option price for a call/put

    d1 = (np.log(S/K) + (r+sigma**2/2)* T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    return {
        'call': S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2),
        'put':  K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    }

