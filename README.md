# Portfolio Beta Calculator

This is a Streamlit application that calculates the beta of a portfolio based on user inputs. The beta measures the volatility of a portfolio in comparison to the market.

## Features

- Input stock tickers and market index
- Select frequency of returns (Daily, Weekly, Monthly)
- Select period for data collection (1 year, 2 years, 5 years)
- Calculate and display the beta of the portfolio

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```sh
    cd <project-directory>
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run beta.py
    ```
2. Open your web browser and go to `http://localhost:8501`
3. Enter your holdings, market index, select the frequency and period for data collection, and click on "Calculate Beta".

## Example

1. Enter your holdings (comma separated): `AAPL, MSFT, GOOG`
2. Enter the market index: `SPY`
3. Select frequency of returns: `Daily`
4. Select period for data collection: `1y`
5. Click on "Calculate Beta"

The application will display the beta of your portfolio.

## Dependencies

- streamlit
- yfinance
- pandas
- numpy

## License

This project is licensed under the MIT License.