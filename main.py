import numpy as np
from math import log, sqrt, exp
from scipy.stats import norm
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import streamlit.components.v1 as components

from blackscholes import blackscholes
from rate import get_r

def main():
    
    S = float(input("Enter the price of the stock: "))
    K = float(input("Enter the strike price of the option: "))
    T = float(input("Enter the time to expiry (in calendar days): "))/365
    sigma = float(input("Enter the volatility of the asset: "))/100

    r = get_r()
    

    prices = blackscholes(S, K, r, T, sigma)

    price_call = prices['call']
    price_call = round(price_call, ndigits = 2)
    print(f"Call price: {price_call} $")
    
    price_put = prices['put']
    price_put = round(price_put, ndigits = 2)
    print(f"Put price: {price_put} $")
    


if __name__ == "__main__":
    main()