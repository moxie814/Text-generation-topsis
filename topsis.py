import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def topsis(input_file, weights):
    # Read the input CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Extract criteria columns
    criteria = df.iloc[:, 1:]

    # Normalize data
    normalized_criteria = (criteria - criteria.min()) / (criteria.max() - criteria.min())

    # Apply weights to normalized criteria
    weighted_criteria = normalized_criteria * weights

    # Identify ideal and negative-ideal solutions
    ideal_solution = weighted_criteria.max()
    negative_ideal_solution = weighted_criteria.min()

    # Calculate separation measures
    separation_measures = np.sqrt(
        np.sum((weighted_criteria - ideal_solution)**2, axis=1) +
        np.sum((weighted_criteria - negative_ideal_solution)**2, axis=1)
    )

    # Calculate TOPSIS score
    topsis_score = separation_measures / (separation_measures + np.sqrt(
        np.sum((weighted_criteria - negative_ideal_solution)**2, axis=1)
    ))

    # Combine TOPSIS score into the original DataFrame
    df['TOPSIS Score'] = topsis_score

    # Rank models based on TOPSIS score
    ranked_models = df.sort_values(by='TOPSIS Score', ascending=False)

    return ranked_models

def plot_topsis_comparison(ranked_models):
    # Plotting the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(ranked_models.index, ranked_models['TOPSIS Score'], color='skyblue')
    plt.xlabel('Models')
    plt.ylabel('TOPSIS Score')
    plt.title('Comparison of TOPSIS Scores for Models')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Show the plot or save it to a file
    plt.show()

if __name__ == "__main__":
    # Input CSV file path
    input_file = '102103561-data.csv'

    # Define weights (replace with your own weights)
    weights = np.array([0.4, 0.6,1,1,1])

    # Apply TOPSIS and get ranked models
    ranked_models = topsis(input_file_path, weights)

    # Print the ranked models
    print("Ranked Models:")
    print(ranked_models)

    # Plot the bar graph for comparison
    plot_topsis_comparison(ranked_models)
