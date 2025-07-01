import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import streamlit.components.v1 as components



from blackscholes import blackScholes

def main():
    
    S = float(input("Enter the price of the stock: "))
    K = float(input("Enter the strike price of the option: "))
    r = float(input("Enter the risk-free rate: "))
    T = float(input("Enter the time to expiry (in days): "))/365
    sigma = float(input("Enter the volatility of the asset: "))
    type = (input("Are you buying a call (enter c) or a put(enter p): "))

    print(blackScholes(S, K, r, T, sigma, type))


if __name__ == "__main__":
    main()