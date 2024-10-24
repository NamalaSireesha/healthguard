import matplotlib.pyplot as plt

# Sample data representing the impact of remote patient monitoring over time
# Replace with your actual data
time_periods = ['year 2020', 'year 2021', 'year 2022', 'year 2023', 'year 2024']
impact_scores = [3.5, 4.0, 4.2, 4.5, 4.8]  # Impact scores on a scale of 1 to 5

# Plotting the line graph
plt.figure(figsize=(10, 6))
plt.plot(time_periods, impact_scores, marker='o', color='b', linestyle='-')

# Adding labels and title
plt.xlabel('Time Period')
plt.ylabel('Impact Score')
plt.title('Impact of Remote Patient Monitoring with Enhanced EHR Integration Over Time')

# Displaying the plot
plt.grid(True)  # Add grid for better readability
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
