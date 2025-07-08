# Black-Scholes Options Trading Model

This project is an interactive web app for visualizing European option prices and Greeks using the Black-Scholes model. Built with Python and Streamlit, it allows users to explore how option values change as key parameters vary, with results displayed as an interactive heatmap.

## Features

- Lets users select any two parameters to compare (stock price, strike price, volatility, time to expiry, risk-free rate).
- All other parameters can be set as constants.
- Calculates European call and put option prices using the Black-Scholes formula.
- Visualizes option prices and Greeks (Delta, Gamma, Vega, Theta, Rho) on a heatmap.
- Interactive controls for parameter ranges and heatmap resolution.
- Hovering over a heatmap cell shows detailed option price, Greeks, and contract value.
- Automatically fetches the current risk-free rate (US 3-month T-bill) via FRED.

## Usage

1. **Install dependencies**  
   Create a virtual environment (recommended) and install requirements:
   ```sh
   pip install -r requirements.txt
   ```

2. **Run the app**  
   Launch the Streamlit app:
   ```sh
   streamlit run main.py
   ```
   *(or use `ui3.py` if that is your main UI file)*

3. **Interact**  
   - Select the option type (Call or Put).
   - Choose two parameters to compare and set their ranges.
   - Set the values for the remaining parameters.
   - Adjust the heatmap resolution.
   - Hover over cells to see detailed info.

## Screenshots

(screenshot1.png)

(screenshot2.png)

## Files

- `main.py` / `ui3.py` — Main Streamlit app.
- `blackscholes.py` — Black-Scholes pricing function.
- `greeks.py` — Functions to compute option Greeks.
- `rate.py` — Fetches the current risk-free rate.
- `requirements.txt` — List of required Python packages.
- `notes.txt` — Project notes and development log.

## Requirements

- Python 3.8–3.12 (recommended)
- See `requirements.txt` for all Python package dependencies.

## Author

Samy Bisaillon

---

*This app is for educational and informational purposes