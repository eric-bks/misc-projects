import numpy as np
import matplotlib.pyplot as plt

# Parameters
p = 0.51
q = 0.49
kelly_fraction = p - q

# Number of bets
n_bets = 1000

# Wealth arrays for different strategies
wealth_kelly = np.zeros(n_bets + 1)
wealth_half_kelly = np.zeros(n_bets + 1)
wealth_double_kelly = np.zeros(n_bets + 1)
wealth_fixed = np.zeros(n_bets + 1)

# Initial wealth
initial_wealth = 1
wealth_kelly[0] = initial_wealth
wealth_half_kelly[0] = initial_wealth
wealth_double_kelly[0] = initial_wealth
wealth_fixed[0] = initial_wealth

# Simulate the growth of wealth
np.random.seed(42)
for i in range(1, n_bets + 1):
    outcome = np.random.rand() < p  # True if win, False if loss

    # Kelly strategy
    if outcome:
        wealth_kelly[i] = wealth_kelly[i-1] * (1 + kelly_fraction)
    else:
        wealth_kelly[i] = wealth_kelly[i-1] * (1 - kelly_fraction)
    
    # Half Kelly strategy
    if outcome:
        wealth_half_kelly[i] = wealth_half_kelly[i-1] * (1 + 0.5 * kelly_fraction)
    else:
        wealth_half_kelly[i] = wealth_half_kelly[i-1] * (1 - 0.5 * kelly_fraction)
    
    # Double Kelly strategy
    if outcome:
        wealth_double_kelly[i] = wealth_double_kelly[i-1] * (1 + 2 * kelly_fraction)
    else:
        wealth_double_kelly[i] = wealth_double_kelly[i-1] * (1 - 2 * kelly_fraction)
    
    # Fixed bet size strategy (2%)
    fixed_bet_fraction = 0.02
    if outcome:
        wealth_fixed[i] = wealth_fixed[i-1] * (1 + fixed_bet_fraction)
    else:
        wealth_fixed[i] = wealth_fixed[i-1] * (1 - fixed_bet_fraction)

# Plotting the results
plt.figure(figsize=(12, 8))
plt.plot(wealth_kelly, label='Kelly Criterion (2%)', color='blue')
plt.plot(wealth_half_kelly, label='Half Kelly (1%)', color='green')
plt.plot(wealth_double_kelly, label='Double Kelly (4%)', color='red')
plt.plot(wealth_fixed, label='Fixed Bet (2%)', color='orange')
plt.title('Growth of Wealth Over Time Using Different Betting Strategies')
plt.xlabel('Number of Bets')
plt.ylabel('Wealth')
plt.legend()
plt.yscale('log')  # Use logarithmic scale for better visualization
plt.grid(True)
plt.show()
