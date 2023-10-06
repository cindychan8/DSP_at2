import streamlit as st
import datetime

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import reverse_rate, round_rate, format_output

# Display Streamlit App Title

# Get the list of available currencies from Frankfurter

# If the list of available currencies is None, display an error message in Streamlit App

# Add input fields for capturing amount, from and to currencies

# Add a button to get and display the latest rate for selected currencies and amount

# Add a date selector (calendar)

# Add a button to get and display the historical rate for selected date, currencies and amount

st.title("FX Converter")
currencies = get_currencies_list()
if  currencies is None:
    st.error("Error: Not access to available Currrency, please try again!")
else:
    amount = st.number_input("Amount to be converted", min_value=0.01, value=1.00, step=0.01)
    from_currency = st.selectbox("From Currency", currencies)
    to_currency = st.selectbox("To Currency", currencies)

#set up latest button and output response in specific text from frankfurter
if st.button("Get Latest Rates"):
    date, rate = get_latest_rates(from_currency, to_currency)
    st.header("Latest Conversion Rate")
    st.write(format_output(date, from_currency, to_currency, rate, amount))

#set up select botton to users
selected_date = st.date_input("Select date", datetime.date.today())

#set up historical button based on selected_date to output format
if st.button("Get Historical Rate"):
    rate = get_historical_rate(from_currency, to_currency, selected_date)
    st.header("Historical Conversion Rate")
    st.write(format_output(selected_date, from_currency, to_currency, rate, amount))

    








