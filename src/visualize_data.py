import pandas as pd
import matplotlib.pyplot as plt
import os

# File paths
input_path = "C:\Phd_research_workflow\data\cleaned_data.csv"
output_path1 = "C:/Phd_research_workflow/results/plot1_histogram.png"
output_path2 = "C:/Phd_research_workflow/results/plot2_scatter.png"

# Read data
df = pd.read_csv(input_path)

# Plot 1: Histogram (experiment_score)
plt.figure()
plt.hist(df['experiment_score'])
plt.title("Experiment Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.savefig(output_path1)
plt.close()

# Plot 2: Scatter plot (temperature vs experiment_score)
plt.figure()
plt.scatter(df['temperature'], df['experiment_score'])
plt.title("Temperature vs Experiment Score")
plt.xlabel("Temperature")
plt.ylabel("Experiment Score")
plt.savefig(output_path2)
plt.close()

print("Plots saved successfully in results folder")