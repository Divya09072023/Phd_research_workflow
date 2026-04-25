🔹 Input Files Required
data/sample_data.csv – Raw dataset used as input
data/cleaned_data.csv – Intermediate dataset generated after preprocessing (used by visualization module)
🔹 Scripts to be Executed
src/clean_data.py – Performs data cleaning and preprocessing
src/visualize_data.py – Generates visualizations from the cleaned dataset
🔹 Execution Order

To ensure correct results, the scripts must be executed in the following sequence:

Run data cleaning script:

python src/clean_data.py

Run visualization script:

python src/visualize_data.py

This order is necessary because the visualization step depends on the output of the data cleaning stage.

🔹 Expected Output Files
data/cleaned_data.csv – Cleaned and processed dataset
Files inside results/ directory, such as:
Plots (e.g., .png, .jpg)
Analytical outputs and summaries
🔹 Software Dependencies

The project requires the following Python libraries:

pandas – data manipulation
numpy – numerical computations
matplotlib / seaborn – data visualization

Install dependencies using:

pip install -r requirements.txt
🔹 Assumptions
Input dataset is structured and follows a consistent schema
Missing values are random in nature and can be handled via standard techniques
Cleaned dataset (cleaned_data.csv) is correctly generated before visualization
Required libraries are properly installed in the environment
🔹 Limitations
The workflow assumes static batch processing and does not support real-time data
Basic preprocessing techniques may not handle complex data anomalies
Visualization is limited to static plots without interactive exploration
Results depend heavily on the quality and completeness of input data