# Assume df is your DataFrame with models as rows and criteria as columns

# Normalize data
normalized_df = (df - df.min()) / (df.max() - df.min())

# Assign weights (replace with your own weights)
weights = {'perplexity': 0.4, 'training_time': 0.6}

# Identify ideal and negative-ideal solutions
ideal_solution = normalized_df.max()
negative_ideal_solution = normalized_df.min()

# Calculate separation measures
separation_measures = np.sqrt(
    weights['perplexity'] * (normalized_df['perplexity'] - ideal_solution['perplexity'])**2 +
    weights['training_time'] * (normalized_df['training_time'] - ideal_solution['training_time'])**2
)

# Calculate TOPSIS score
topsis_score = separation_measures / (separation_measures + np.sqrt(
    weights['perplexity'] * (normalized_df['perplexity'] - negative_ideal_solution['perplexity'])**2 +
    weights['training_time'] * (normalized_df['training_time'] - negative_ideal_solution['training_time'])**2
))

# Add TOPSIS score to DataFrame
df['TOPSIS Score'] = topsis_score

# Rank models based on TOPSIS score
ranked_models = df.sort_values(by='TOPSIS Score', ascending=False)

# Display or save the ranked_models DataFrame
print(ranked_models)
