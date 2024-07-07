import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the disassembly results
df = pd.read_csv('disassembly_results.csv')

# Box plot for valid instructions count
plt.figure(figsize=(10, 6))
plt.boxplot(df['valid_instructions_count'], showfliers=False)
plt.title('Box Plot of Valid Instructions Count')
plt.xlabel('All Data')
plt.ylabel('Number of Valid Instructions')
plt.show()

df = pd.read_csv('disassembly_results.csv')

# Define a reasonable max value for the histogram to zoom into the lower range
max_valid_instructions = 1000

# Filter the DataFrame to only include rows within this range
filtered_df = df[df['valid_instructions_count'] <= max_valid_instructions]

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(filtered_df['valid_instructions_count'], bins=100, alpha=0.75, edgecolor='black')
plt.title('Distribution of Valid Instructions Before Encountering an Invalid Instruction ')
plt.xlabel('Number of Valid Instructions')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

total_samples = len(df)
average_valid_instructions = df['valid_instructions_count'].mean()
maximum_valid_instructions = df['valid_instructions_count'].max()
minimum_valid_instructions = df['valid_instructions_count'].min()

# Print the statistics
print(f"Total Samples: {total_samples}")
print(f"Average Number of Valid Instructions: {average_valid_instructions:.2f}")
print(f"Maximum Number of Valid Instructions: {maximum_valid_instructions}")
print(f"Minimum Number of Valid Instructions: {minimum_valid_instructions}")

