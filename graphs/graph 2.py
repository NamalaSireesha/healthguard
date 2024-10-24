import matplotlib.pyplot as plt
import numpy as np

# Sample data representing chronic diseases and patient counts for different age groups
# Each inner list represents patient counts for each disease in the respective age group
# Age groups: 0-10, 11-25, 25+
chronic_diseases = ['Diabetes', 'Hypertension', 'Asthma', 'Arthritis']
patient_counts_0_to_10 = [20, 30, 15, 25]  # Counts for age group 0-10
patient_counts_11_to_25 = [50, 60, 40, 30]  # Counts for age group 11-25
patient_counts_25_above = [30, 40, 25, 45]  # Counts for age group 25+

# Total number of diseases
num_diseases = len(chronic_diseases)

# Width of each bar
bar_width = 0.2

# Positions for the bars
index = np.arange(num_diseases)

# Plotting the bar graph
plt.figure(figsize=(10, 6))

plt.bar(index, patient_counts_0_to_10, bar_width, label='0-10 years')
plt.bar(index + bar_width, patient_counts_11_to_25, bar_width, label='11-25 years')
plt.bar(index + 2*bar_width, patient_counts_25_above, bar_width, label='25+ years')

# Adding labels and title
plt.xlabel('Chronic Diseases')
plt.ylabel('Number of Patients')
plt.title('Patient Counts by Chronic Disease and Age Group')
plt.xticks(index + bar_width, chronic_diseases)
plt.legend()

# Displaying the plot
plt.tight_layout()
plt.show()
