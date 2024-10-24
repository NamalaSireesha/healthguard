import matplotlib.pyplot as plt

# Sample data representing chronic diseases and patient counts
chronic_diseases = ['Diabetes', 'Hypertension', 'Asthma', 'Arthritis']
patient_counts = [100, 150, 80, 120]  # Corresponding patient counts for each disease

# Plotting the bar graph
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.bar(chronic_diseases, patient_counts, color='skyblue')

# Adding labels and title
plt.xlabel('Chronic Diseases')
plt.ylabel('Number of Patients')
plt.title('Patient Counts by Chronic Disease')

# Rotating the x-axis labels for better readability
plt.xticks(rotation=45)

# Displaying the plot
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
