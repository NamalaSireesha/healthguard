import matplotlib.pyplot as plt
import numpy as np

# Sample data representing chronic diseases and patient counts for different locations
# Each inner list represents patient counts for each disease in the respective location
locations = ['Kakinada', 'Rajahmundry', 'Amalapuram', 'Pitapuram', 'Samalkota']
chronic_diseases = ['Diabetes', 'Hypertension', 'Asthma', 'Arthritis']

# Sample patient counts for each disease in each location
patient_counts = {
    'Kakinada': [30, 40, 25, 35],
    'Rajahmundry': [20, 35, 30, 40],
    'Amalapuram': [15, 20, 10, 25],
    'Pitapuram': [25, 30, 20, 35],
    'Samalkota': [35, 25, 15, 30]
}

# Total number of locations and diseases
num_locations = len(locations)
num_diseases = len(chronic_diseases)

# Width of each bar
bar_width = 0.15

# Positions for the bars
index = np.arange(num_diseases)

# Plotting the bar graph
plt.figure(figsize=(12, 6))

for i, location in enumerate(locations):
    plt.bar(index + i * bar_width, patient_counts[location], bar_width, label=location)

# Adding labels and title
plt.xlabel('Chronic Diseases')
plt.ylabel('Number of Patients')
plt.title('Patient Counts by Chronic Disease and Location')
plt.xticks(index + bar_width * (num_locations - 1) / 2, chronic_diseases)
plt.legend()

# Displaying the plot
plt.tight_layout()
plt.show()
