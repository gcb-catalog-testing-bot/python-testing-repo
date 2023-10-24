import pytest
import src.simple_stat_computing as stat_compute
import pandas as pd
from scipy import stats

# Sample data for testing
sample_data = {
    'sales': [150, 200, 50, 400, 500, 450, 350],
    'expenses': [100, 50, 30, 100, 250, 300, 200]
}
sample_df = pd.DataFrame(sample_data)
sample_df['profit'] = sample_df['sales'] - sample_df['expenses']
correlation, _ = stats.pearsonr(sample_df['sales'], sample_df['profit'])

def test_get_profit():
    expected_profit = [50, 150, 20, 300, 250, 150, 150]
    result = stat_compute.get_profit(sample_df)
    assert result == expected_profit, "The get_profit function did not return expected values"

def test_get_sales_profit_correlation():
    result = stat_compute.get_sales_profit_correlation(correlation)
    assert result == correlation, "The get_sales_profit_correlation function did not return expected values"

def test_main():
    profits, corr = stat_compute.main()
    assert profits == [50, 150, 20, 300, 250, 150, 150], "The main function did not return expected profit values"
    assert corr == correlation, "The main function did not return expected correlation value"
