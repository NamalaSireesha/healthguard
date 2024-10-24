import matplotlib.pyplot as plt

# Data
socioeconomic_status = ['Low Income', 'Middle Income', 'High Income']
access_percentage = [60, 30, 10]  # Example percentages, adjust according to your data

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(access_percentage, labels=socioeconomic_status, autopct='%1.1f%%', startangle=140)
plt.title('Easy Healthcare Access by Socioeconomic Status')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
