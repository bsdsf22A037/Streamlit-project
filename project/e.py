import pandas as pd

# Load the dataset
df = pd.read_csv('obesity_level.csv')

# Take a random sample of 700 rows
sample_df = df.sample(n=700, random_state=42)

# Save the sampled data to a new file (optional)
sample_df.to_csv('sampled_dataset.csv', index=False)

print(sample_df.head())  # Preview the sample