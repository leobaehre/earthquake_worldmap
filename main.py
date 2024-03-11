import pandas as pd
import map

# Read the data from the CSV file
csv_data = pd.read_csv('data/earthquake_data.csv', delimiter=',')

# Extract the data we need
data = csv_data[['magnitude', 'longitude', 'latitude']]
data.dropna() # Remove rows with missing data

# Create a map
map.draw_map()

# Draw the points
map.draw_points(data)