import numpy as np
from scipy import stats

# Simulated scraped data (replace with your real scraped prices)
jan_prices = [80, 85, 90, 75, 95]  # January prices
feb_prices = [88, 92, 87, 89, 91]  # February prices

# Assumption 1: Check Normality
_, jan_p = stats.shapiro(jan_prices)  # Shapiro test for normality
_, feb_p = stats.shapiro(feb_prices)
print(f"Normality p-values: Jan={jan_p:.3f}, Feb={feb_p:.3f}")
# If p > 0.05, assume normal (small sample caveat)

# Assumption 2: Check Equal Variance
_, var_p = stats.levene(jan_prices, feb_prices)
print(f"Equal variance p-value: {var_p:.3f}")
# If p > 0.05, assume equal variance

# Hypothesis Test: Independent t-test
t_stat, p_value = stats.ttest_ind(jan_prices, feb_prices, equal_var=(var_p > 0.05))
print(f"T-test: t={t_stat:.3f}, p={p_value:.3f}")
# If p < 0.05, reject H₀ (prices differ)
if p_value < 0.05:
    print("Prices are significantly different!")
else:
    print("No significant difference.")