import pandas as pd
import matplotlib.pyplot as plt

# Read in data from data directory
df = pd.read_csv("data/Electric_Vehicle_Population_Data.csv")

# Count instances of each model type
make_counts = df['Make'].value_counts()

# Prepare counts for plot
make_counts = make_counts.head(15)                          # a lot of model types so just taking the top 15
make_counts.sort_values(ascending=True, inplace=True)       # reverse order for plot

# Plot
plot = make_counts.plot.barh(title='Most Popular Electric Vehicle Makes in Washington')
plt.xlabel('Count')
plt.ylabel('Make')
plt.show()

# Save plot to data directory
fig = plot.get_figure()
fig.savefig('result/top_wa_vehicle_makes.png', dpi=300, bbox_inches='tight')

print("Bar Chart Saved to data Directory")