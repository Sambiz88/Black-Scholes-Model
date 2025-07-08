import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go

from blackscholes import blackscholes
from greeks import greeks
from typing import Optional, Dict, Tuple, List
from rate import get_r
#asks user data he wants to chec
# Create a 10x10 array of random numbers
data = np.random.rand(10, 10)
df = pd.DataFrame(data, columns=[f'Col {i}' for i in range(10)])



st.title('Option Price Heat Map')

st.write("A visual tool for exploring European option prices using the Black-Scholes model. " \
"Select and compare key parameters, and view how option values change across different scenarios with an interactive heatmap.")

st.markdown("<br><span style='font-size:1.5em;'><b>Choose the type of option contract</b></span>", unsafe_allow_html=True)
type = st.radio(
    "Choose the type of option contract", 
    {"Call", "Put",},
)
    

class INPUTS:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

##### Black-Scholes formula inputs
inputs = INPUTS(        
    S=-1.0,
    K=-1.0,
    r=-1.0,
    T=-1.0,
    sigma=-1.0
)
#####

##### Min and max values of each variable
VARIABLES = {
    "Stock price": {"min": 0.01, "max": 1000.0},        # All min/max values are initialized as doubles because
    "Strike price": {"min": 0.01, "max": 2000.0},       # min/max values in number_input need to have the same
    "Time to expiry": {"min": 1.0, "max": 1096.0},      # type (e.g. min cannot be int while max is a double)
    "Volatility": {"min": 1.0, "max": 1000.0},
    "Risk-free rate": {"min": 0.0, "max": 20.0},
}
#####

##### SELECTION OF COMPARED VARIABLES
col_1, col_2, col_3, col_4, col_5 = st.columns([0.5, 1, 0.25, 1, 1])  

with col_1:
    
    st.markdown(
        "<div style='padding-top:2.2rem'><strong>Compare</strong></div>",
        unsafe_allow_html=True,
    )

with col_2:
    choice_1 = st.selectbox(
        label="",                            
        options=VARIABLES,              
        placeholder="select…",
        key="compare_select",

    )

with col_3:
    st.markdown(
        "<div style='padding-top:2.2rem'><strong>with</strong></div>",
        unsafe_allow_html=True,
    )

REMAINING_VARIABLES = [k for k in VARIABLES if k != choice_1]

with col_4:
    choice_2 = st.selectbox(
        label="",
        options=REMAINING_VARIABLES,
        placeholder = "select..."
    )

with col_5:
    st.write(" ")

#####

##### VALUES OF CONSTANT VARIABLES

st.markdown("<br><span style='font-size:1.5em;'><b>Set other parameters</b></span>", unsafe_allow_html=True)

for i in range(len(VARIABLES)):
    if (list(VARIABLES.keys())[i] != choice_1 and list(VARIABLES.keys())[i] != choice_2):
        col_1, col_2, col_3 = st.columns([1, 1, 2])

        with col_1:
            st.markdown(
                f"<div style='padding-top:2.2rem'><strong>{list(VARIABLES.keys())[i]}</strong></div>",
                unsafe_allow_html=True,
            )
            
        
        with col_2:
            if list(VARIABLES.keys())[i] == 'Stock price':
                inputs.S = st.number_input(
                    " ",
                    min_value = VARIABLES["Stock price"]["min"],
                    max_value = VARIABLES["Stock price"]["max"],
                    key = "stock_price_input",
                    value = 100.00,
                    )
            
            if list(VARIABLES.keys())[i] == 'Strike price':
                inputs.K = st.number_input(
                    " ",
                    min_value = VARIABLES["Strike price"]["min"],
                    max_value = VARIABLES["Strike price"]["max"],
                    key = "strike_price_input",
                    value = 105.00
                    )
            
            if list(VARIABLES.keys())[i] == 'Risk-free rate':
                inputs.r = st.number_input(
                    " ",
                    min_value = VARIABLES["Risk-free rate"]["min"],
                    max_value = VARIABLES["Risk-free rate"]["max"],
                    key = "rate_input",
                    value = 5.00,
                )            
                
            if list(VARIABLES.keys())[i] == 'Time to expiry':
                inputs.T = st.number_input(
                    " ",
                    min_value = VARIABLES["Time to expiry"]["min"],
                    max_value = VARIABLES["Time to expiry"]["max"],
                    key = "time_input",
                    value = 30.00,
                    )
            
            if list(VARIABLES.keys())[i] == 'Volatility':
                inputs.sigma = st.number_input(
                    " ",
                    min_value = VARIABLES["Volatility"]["min"],
                    max_value = VARIABLES["Volatility"]["max"],
                    key = "volatility_input",
                    value = 20.00,
                    )
            

                
        with col_3:
            if list(VARIABLES.keys())[i] == 'Stock price':
                st.markdown(
                "<div style='padding-top:2.2rem'><strong>$</strong></div>",
                unsafe_allow_html=True,
                )

            
            if list(VARIABLES.keys())[i] == 'Strike price':
                st.markdown(
                "<div style='padding-top:2.2rem'><strong>$</strong></div>",
                unsafe_allow_html=True,
                )

            if list(VARIABLES.keys())[i] == 'Time to expiry':
                st.markdown(
                "<div style='padding-top:2.2rem'><strong>days</strong></div>",
                unsafe_allow_html=True,
            )
            
            if list(VARIABLES.keys())[i] == 'Volatility':
                st.markdown(
                "<div style='padding-top:2.2rem'><strong>% *</strong></div>",
                unsafe_allow_html=True,
                )

            if list(VARIABLES.keys())[i] == 'Risk-free rate':
                st.markdown(
                "<div style='padding-top:2.2rem'><strong>%</strong></div>",
                unsafe_allow_html=True,
                )


st.markdown(
    f"<span style='color:gray; font-size:0.95em;'>* The risk-free rate is typically the yield of a government bond (e.g., US 3-month T-bill). The current risk-free rate is {get_r()} %.</span>",
    unsafe_allow_html=True
)
#####   


###### RANGE OF COMPARED VARIABLES FOR HEATMAP

col_1, col_2, col_3, col_4 = st.columns([1,1,1,1])


for i in range(len(VARIABLES)):
    key = list(VARIABLES.keys())[i]
    if(key == choice_1):
        with col_1:
            variable_1_lower = st.number_input(
                f"{choice_1} minimum",
                min_value=VARIABLES[key]["min"],
                max_value=VARIABLES[key]["max"],
                value = 100.0 if choice_1 == "Stock price" else 120.0 if choice_1 == "Strike price" else 2.5 if choice_1 == "Risk-free rate" else 1.0 if choice_1 == "Time to expiry" else 10.0,  
                key=f"{choice_1}_min_input"           
            )

        with col_2:
            # Use session state to update upper if needed
            upper_key = f"{choice_1}_max_input"
            if upper_key not in st.session_state or st.session_state[upper_key] < variable_1_lower:
                st.session_state[upper_key] = variable_1_lower
            variable_1_upper = st.number_input(
                f"{choice_1} maximum",
                min_value=variable_1_lower,
                max_value=VARIABLES[key]["max"],
                value= st.session_state[upper_key],
                key=upper_key
    )


for i in range(len(VARIABLES)):
    key = list(VARIABLES.keys())[i]
    if(key == choice_2):
        with col_3:
            variable_2_lower = st.number_input(
                f"{choice_2} minimum",
                min_value=VARIABLES[key]["min"],
                max_value=VARIABLES[key]["max"],
                value = 100.0 if choice_2 == "Stock price" else 120.0 if choice_2 == "Strike price" else 2.5 if choice_2 == "Risk-free rate" else 1.0 if choice_2 == "Time to expiry" else 10.0,   
            )

        with col_4:
            upper2_key = f"{choice_2}_max_input"
            if upper2_key not in st.session_state or st.session_state[upper2_key] < variable_2_lower:
                st.session_state[upper2_key] = variable_2_lower
            variable_2_upper = st.number_input(
                f"{choice_2} maximum",
                min_value=variable_2_lower,
                max_value=VARIABLES[key]["max"],
                value=st.session_state[upper2_key],
                key=upper2_key
            )

#####
##### HEAT MAP CONSTRUCTION

rows = st.number_input('Select number of rows:', min_value=1, max_value=20, value=10)
cols = st.number_input('Select number of columns:', min_value=1, max_value=20, value=10)


# Ensure at least two unique values for each axis
if variable_1_lower == variable_1_upper:
    variable_1_upper += 0.01

if variable_2_lower == variable_2_upper:
    variable_2_upper += 0.01


x_vals = np.linspace(variable_1_lower, variable_1_upper, rows)
y_vals = np.linspace(variable_2_lower, variable_2_upper, cols)

Z = np.empty((len(y_vals), len(x_vals)))

contract_price = np.empty_like(Z)

delta = np.empty_like(Z)
gamma = np.empty_like(Z)
vega = np.empty_like(Z)
theta = np.empty_like(Z)
rho = np.empty_like(Z)


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

        if Z[i, j] < 0.0001:
            Z[i, j] = 0
        
        contract_price[i, j] = 100 * Z[i, j]

        
        greek_values = greeks(S, K, r, T, sigma, type)
        delta[i, j] = greek_values ["delta"]
        gamma[i, j] = greek_values ["gamma"]
        vega[i, j] = greek_values ["vega"]
        theta[i, j] = greek_values ["theta"]
        rho[i, j] = greek_values ["rho"]


df = pd.DataFrame(
    Z,
    index = np.round(y_vals, 2),
    columns = np.round(x_vals, 2),
)



fig = go.Figure(
    data=go.Heatmap(
        z=np.round(Z, 4),
        x= x_vals, #np.round(x_vals, 2),
        y= y_vals, #np.round(y_vals, 2),
        customdata = np.stack([delta, gamma, vega, theta, rho, contract_price], axis=-1),
        colorscale='RdBu_r',
        colorbar=dict(title="Option Price ($)"),
        text= np.round(Z, 4), #Z
        texttemplate="%{text}",  
        hovertemplate=
            f"{choice_1}: %{{x}}<br>" +
            f"{choice_2}: %{{y}}<br>" +
            "<b>Contract Price: %{customdata[5]:.2f}</b><br>" +
            "Delta: %{customdata[0]:.3f}<br>" +
            "Gamma: %{customdata[1]:.3f}<br>" +
            "Vega: %{customdata[2]:.3f}<br>" +
            "Theta: %{customdata[3]:.3f}<br>" +
            "Rho: %{customdata[4]:.3f}<br>" +
            "<extra></extra>"
            
    )
)

def map_units(choice):
    
    if choice == "Stock price" or "Strike price" : return "$"
    if choice == "Time to expiry" : return "days"
    if choice == "Volatility" or "Risk-free rate" : return "%"


fig.update_layout(
    title="Option Price Heatmap",
    xaxis_title=f"{choice_1} ({map_units(choice_1)})",
    yaxis_title=f"{choice_2} ({map_units(choice_2)})",
)

st.plotly_chart(fig)

#####

st.markdown("<br><hr><div style='text-align:center; color:gray;'>Author: Samy Bisaillon</div>", unsafe_allow_html=True)