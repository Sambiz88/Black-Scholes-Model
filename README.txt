# Black-Scholes Options Trading Model

This project implements a Black-Scholes options pricing model in Python. It allows users to input the five main parameters that affect an option's price and returns the calculated values for both call and put options.

## Features

- Calculates European call and put option prices using the Black-Scholes formula.
- User inputs for:
  - Stock price
  - Strike price
  - Risk-free interest rate
  - Time to expiry (in days)
  - Volatility

## Usage

1. Run `main.py`:
    ```sh
    python main.py
    ```
2. Enter the required parameters when prompted.

## Files

- [`main.py`](main.py): Main script for user interaction and displaying results.
- [`blackscholes.py`](blackscholes.py): Contains the Black-Scholes pricing function.
- [`notes.txt`](notes.txt): Project goals and notes.
- `README.txt`: This file.

## Requirements

- numpy
- scipy
- matplotlib (not currently used)
- seaborn (not currently used)
- streamlit (not currently used)

Install dependencies with:
```sh
pip install numpy scipy matplotlib seaborn streamlit
```

## Notes

- Only the console interface is currently implemented.
- The model uses the standard Black-Scholes formula for European