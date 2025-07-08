import numpy as np
from blackscholes import blackscholes
from math import log, sqrt, exp
from scipy.stats import norm


def greeks(S, K, r, T, sigma, type):

    d1 = (np.log(S/K) + (r+sigma**2/2)* T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T) 

    if type == "Call":
        delta = norm.cdf(d1)
        theta = -((S**sigma*norm.pdf(d1)))/2*T - r*K*(norm.pdf(d2))*exp(-r*T)
        rho = K*T*(exp(-r*T))*norm.cdf(d2)
    
    if type == "Put":
        delta = norm.cdf(d1)-1
        theta = -((S*sigma*norm.pdf(d1))/2*sqrt(T)) + r*K*(exp(-r*T))*(norm.cdf(-d2))
        rho = -K*T*(exp(-r*T))*(norm.cdf(-d2))

    vega = S*(norm.cdf(d2))*sqrt(T)

    gamma = norm.pdf(d1)/(S*sigma*sqrt(T))


    return {
        "delta": delta,
        "gamma": gamma,
        "vega": vega,
        "theta": theta,
        "rho": rho,
    }

