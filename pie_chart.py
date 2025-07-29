import csv
from plotly.graph_objs import Pie, Layout

from plotly import offline

filename = 'data/population_by_continent.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    continents = []
    population = []

    for row in reader:
        continents.append(row[0])
        population.append(row[1])

data = [Pie(labels=continents, values=population)]
layout = Layout(
    title={'text' : 'World Population Distribution by Continent 2025', 'x' : 0.5}
)

offline.plot({'data' : data, 'layout' : layout}, filename='charts/pie_chart.html')
