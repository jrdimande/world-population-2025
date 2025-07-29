import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = '../data/current-world-population.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    countries = []
    iso_codes = []
    population = []

    for row in reader:
        countries.append(row[2])
        iso_codes.append(row[6])
        population.append(int(row[0]))


data = [Scattergeo(
    locationmode='ISO-3',
    locations=iso_codes,

    text=[f'{c}: {p:,} pessoas' for c, p in zip(countries, population)],
    marker=dict(
        size=[p / 10000000 for p in population],
        color=population,
        colorscale='Viridis',
        colorbar=dict(title='Population'),
        line=dict(width=0.5, color='rgb(40,40,40)'),
    )
)]

layout = Layout(
    title='World Population Distribution 2025',
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='natural earth'
    )
)

offline.plot({'data': data, 'layout':layout}, filename='../charts/scattergeo_chart.html')
