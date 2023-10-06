# <Building Currency Converter in Python>

## Author
Name: Wanzhen Chen

Student ID: 25016179

## Description

**1. Converter Application**

The Currency Converter application is a Python-based tool for currency conversion. It retrieves a series of data from an open-source API (https://www.frankfurter.app/), including historical dates, the latest date, and currency exchange rates. Users can choose the base currency, target currency, and date to fetch the conversion rate between the two currencies and obtain the inverse conversion rate. In the project, we utilize requests library to make requests and retrieve currency conversion data, and the results are presented in a user-friendly manner on the web interface using the Streamlit module.

  * Latest Conversion Rate

  Users select from a currency to a currency and provide an amount. Web app will display the latest conversion rate, the converted amount and the inverse conversion rate.

    The conversion rate on 2023-10-05 from AUD to EUR was 0.6031 . So 1.0 in AUD correspond to 0.6031 in EUR. The inverse rate was 1.658.

  * Historical Conversion Rate

Users select historical date. Web app will display the historical conversion rate, the converted amount and the inverse conversion rate.

    The conversion rate on 2023-10-03 from AUD to EUR was 0.602 . So 1.0 in AUD correspond to 0.602 in EUR. The inverse rate was 1.6612.
#
**2. Program Challenges**

(1) Request from URL

When trying to retrieve historical rate data through requests, an error consistently occurred, preventing the retrieval of historical data. Initially, I combined `get()` and the URL, similar to obtaining the latest rate, but it was unsuccessful. Eventually, I found on W3Schools that describing the URL separately allows the interpreter to better interpret it.

    url = f"{BASE_URL}/{from_date}?&from={from_currency}&to={to_currency}"
    status_code,response = requests.get(url)

(2) Rate Output change with amount change

In the `def format_output`, the variable 'convert_currencies' was added. However, in the original`def get_latest_rates(from_currency, to_currency)`, the 'amount' parameter was actually included. Therefore, in the `get()` method, I try to add and the 'amount' was retrieved based on the parameter. When outputting the results, it was noticed that the rate would change with the input 'amount' value. It was later discovered that when accessing the terminal, the response was affected by this variable. In reality, for this project, we don't need to request 'amount' data. After removing the 'amount' parameter, the correct results were obtained.

    convert_currencies = amount*rounded_rate

#
**3. Feature Implement**

Dynamically retrieve a real-time trend chart showing the hourly, weekly and monthly changes in the exchange rate for the latesr date.

## How to Setup

**1. Python Version**
<Provide a step-by-step description of how to get the development environment set and running.>

**2. Python Version**

  * Python 3.11.4



## How to Run the Program

    streamlit run app.py
<Provide instructions and examples>

## Project Structure
<List all files of this project and provide quick description for each of them>

## Citations

Basic writing and formatting syntax. (n.d.). GitHub Docs. October 6, 2023 
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
<Mention authors and provide links code you source externally>

Python Requests get Method. (n.d.). Www.w3schools.com. https://www.w3schools.com/python/ref_requests_get.asp
