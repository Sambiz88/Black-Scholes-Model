import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import streamlit.components.v1 as components

from blackscholes import blackScholes
from rate import get_r

def main():
    
    S = float(input("Enter the price of the stock: "))
    K = float(input("Enter the strike price of the option: "))
    T = float(input("Enter the time to expiry (in calendar days): "))/365
    sigma = float(input("Enter the volatility of the asset: "))/100
    type = (input("Are you buying a call (enter c) or a put(enter p): "))

    r = get_r()

    price = blackScholes(S, K, r, T, sigma, type)
    price = round(price, ndigits = 2)
    print(f"{price} $")
    


if __name__ == "__main__":
    main()