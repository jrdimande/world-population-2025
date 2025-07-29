import csv
from plotly.graph_objs import Bar, Layout
from plotly import offline

filename = './data/current-world-population.csv'

# Open the csv and create a reader object
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    countries = []                      # <- List to store country names
    population = []                     # <- List to store population values as strings


    for row in reader:
        countries.append(row[2])         # <- Append country name from column index 2
        population.append(row[0])        # <- Append population from column index 0

    countries.reverse()
    population.reverse()

# Select the last 10 countries and their population for plot
x_values = countries[-10:]
y_values = [int(pop) for pop in population[-10:]]

# Creatr the bar chart data
data = [Bar(x=x_values, y=y_values, marker={'color' : 'royalblue'})]

# Config x-axis
x_axis_config = {'title' : 'Countries',
                 'tickangle' : -45}

# Config y-axis
y_axis_config = {'title' : 'Total Population'}

# Set up the layout
layout = Layout(title={'text': 'Top 10 most populated in the world', 'x' : 0.5},
                xaxis=x_axis_config,
                yaxis=y_axis_config,
                annotations=[
                    dict(
                        x=0, y=-0.15,
                        showarrow=False,
                        text="Fonte dos dados: <a href='https://worldpopulationreview.com'>https://worldpopulationreview.com</a>",
                        xref='paper',
                        yref='paper',
                        font=dict(size=10, color='blue'),
                        align='left'
                    )
                ]

                )

# Generate and open bar chart
offline.plot({'data': data, 'layout' : layout}, filename='charts/bar_chart.html')