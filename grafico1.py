from bokeh.plotting import figure, ColumnDataSource
from bokeh.io import show, output_notebook
from bokeh.layouts import row, column, gridplot
from bokeh.models import HoverTool
from bokeh.models.widgets import Panel, Tabs
import pandas as pd
import numpy as np

data = pd.read_csv("CO2_passenger_cars_v12.csv", sep='\t')

diesel_mass = data[data["Ft"] == "DIESEL"]["m (kg)"]
diesel_power = data[data["Ft"] == "DIESEL"]["ep (KW)"]
petrol_mass = data[data["Ft"] == "PETROL"]["m (kg)"]
petrol_power = data[data["Ft"] == "PETROL"]["ep (KW)"]

p = figure(x_axis_label = "mass", y_axis_label = "power")
p.circle(diesel_mass, diesel_power)
p.x(petrol_mass, petrol_power, color = "red")
output_notebook()
show(p)


## Gráfico 2

from bokeh.plotting import figure, ColumnDataSource
from bokeh.io import show, output_notebook
import pandas as pd

data = pd.read_csv("CO2_passenger_cars_v12.csv", sep='\t')

mass_nissan = data[data["Mh"] == "NISSAN"]["m (kg)"]
emissions_nissan = data[data["Mh"] == "NISSAN"]["e (g/km)"]

mass_toyota = data[data["Mh"] == "TOYOTA"]["m (kg)"]
emissions_toyota = data[data["Mh"] == "TOYOTA"]["e (g/km)"]

p2 = figure(x_axis_label = "Mass", y_axis_label = "Emissions")
p2.circle(mass_nissan, emissions_nissan, color = "green")
p2.x(mass_toyota, emissions_toyota, color = "red")
output_notebook()
show(p2)

##Gráfico 3

from bokeh.plotting import figure
from bokeh.io import show, output_notebook
from bokeh.layouts import *
from bokeh.models.widgets import *
import pandas as pd

data = pd.read_csv("CO2_passenger_cars_v12.csv", sep='\t')

mass_tesla = data[data["Mh"] == "TESLA"]["m (kg)"]
emissions_tesla = data[data["Mh"] == "TESLA"]["e (g/km)"]
mass_vw = data[data["Mh"] == "VOLKSWAGEN"]["m (kg)"]
emissions_vw = data[data["Mh"] == "VOLKSWAGEN"]["e (g/km)"]
mass_ferrari = data[data["Mh"] == "FERRARI"]["m (kg)"]
emissions_ferrari = data[data["Mh"] == "FERRARI"]["e (g/km)"]

p1 = figure(title = 'Tesla', x_axis_label = "Mass", y_axis_label = "Emissions")
p2 = figure(title = 'Volkswagen', x_axis_label = "Mass", y_axis_label = "Emissions")
p3 = figure(title = 'Ferrari', x_axis_label = "Mass", y_axis_label = "Emissions")


p1.circle(mass_tesla, emissions_tesla, color = "red")
p2.x(mass_vw, emissions_vw, color = "blue")
p3.circle(mass_ferrari, emissions_ferrari, color = "green")
tabP1 = Panel(child=p1, title='Tesla')
tabP2 = Panel(child=p1, title='Volkswagen')
tabP3 = Panel(child=p1, title='Ferrari')

tabs = Tabs(tabs=[tabP1,tabP2,tabP3])
output_notebook()
show(tabbed_layout)