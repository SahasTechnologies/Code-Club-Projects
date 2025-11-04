#!/bin/python3
import pygal
import os

# Define the path to the CSV file
csv_path = os.path.join('Python', 'charting-champions', 'medals.csv')

# Create a bar chart with a title
chart = pygal.Bar(title='Olympic Medals')

# Read and add data from the CSV file
try:
    with open(csv_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line:  # Skip empty lines
                try:
                    country, medals = line.split(',')
                    chart.add(country, int(medals))
                except ValueError:
                    print(f"Skipping malformed line: {line}")
except FileNotFoundError:
    print(f"CSV file not found at: {csv_path}")

# Save the chart to a file
chart.render_to_file('medals.svg')