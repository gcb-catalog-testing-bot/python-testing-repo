import pandas as pd
from scipy import stats
import logging

# Configuring logging to display information to the console
logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Starting the simple_stat_computing.py script.")
    # Sample data representing sales and expenses
    data = {
        'sales': [150, 200, 50, 400, 500, 450, 350],
        'expenses': [100, 50, 30, 100, 250, 300, 200]
    }

    # Convert the data dictionary into a DataFrame for easy manipulation
    df = pd.DataFrame(data)

    # Calculating profit for each entry as the difference between sales and expenses
    df['profit'] = df['sales'] - df['expenses']
    logging.info("Profit calculated for each data entry.")

    # Compute and log the correlation between sales and profit
    correlation, _ = stats.pearsonr(df['sales'], df['profit'])
    logging.info(f"Correlation between sales and profit: {correlation:.2f}")

    # Call the functions to get profit values and correlation
    profits = get_profit(df)
    correlation_value = get_sales_profit_correlation(correlation)

    logging.info("Ending the simple_stat_computing.py script.")

    return profits, correlation_value

def get_profit(df):
    """Function to retrieve the list of profit values."""
    profit_list = df['profit'].tolist()
    logging.info(f"Profit values: {profit_list}")
    return profit_list

def get_sales_profit_correlation(correlation):
    """Function to retrieve the correlation value between sales and profit."""
    logging.info(f"Returning correlation value: {correlation:.2f}")
    return correlation

if __name__ == '__main__':
    main()
