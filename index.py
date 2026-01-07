python
import pandas as pd
import matplotlib.pyplot as plt

# Load public transportation data
public_transport_data = pd.read_csv('Public_Transportation_Usage_Statistics.csv')

# Load air quality data
aqi_data = pd.read_json('AQI_Historical_Data.json')

# Merge datasets on common attributes, e.g., date and location
merged_data = pd.merge(public_transport_data, aqi_data, on=['Date', 'Location'])

# Analyze correlation between transport usage and air quality
correlation_matrix = merged_data.corr()
print('Correlation between transport usage and AQI:', correlation_matrix['Transport_Usage']['AQI'])

# Plot analysis
plt.figure(figsize=(10, 6))
plt.scatter(merged_data['Transport_Usage'], merged_data['AQI'], alpha=0.5)
plt.title('Transport Usage vs Air Quality Index')
plt.xlabel('Transport Usage')
plt.ylabel('Air Quality Index')
plt.grid(True)
plt.show()
