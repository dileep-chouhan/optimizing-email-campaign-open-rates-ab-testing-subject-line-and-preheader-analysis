import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
# Generate synthetic data for A/B testing email campaign
num_emails = 1000
data = {
    'SubjectLine': np.random.choice(['Subject A', 'Subject B'], size=num_emails),
    'Preheader': np.random.choice(['Preheader X', 'Preheader Y'], size=num_emails),
    'Opened': np.random.binomial(1, 0.2, size=num_emails) # 20% open rate on average
}
df = pd.DataFrame(data)
# --- 2. Data Analysis ---
# Calculate open rates for each subject line and preheader combination
open_rates = df.groupby(['SubjectLine', 'Preheader'])['Opened'].mean().reset_index()
open_rates['OpenRatePercentage'] = open_rates['Opened'] * 100
# --- 3. Visualization ---
plt.figure(figsize=(10, 6))
sns.barplot(x='SubjectLine', y='OpenRatePercentage', hue='Preheader', data=open_rates)
plt.title('Email Open Rates by Subject Line and Preheader')
plt.xlabel('Subject Line')
plt.ylabel('Open Rate (%)')
plt.grid(True)
plt.tight_layout()
# Save the plot to a file
output_filename = 'open_rates.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
# Find the best performing combination
best_combination = open_rates.loc[open_rates['OpenRatePercentage'].idxmax()]
print("\nBest Performing Combination:")
print(best_combination)
#Further analysis (optional):  statistical significance testing (chi-squared test) could be added here to determine if the differences in open rates are statistically significant.  This would require additional libraries like scipy.stats.