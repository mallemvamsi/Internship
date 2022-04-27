'''
this project is developed by the team 7
project info:Tracker:for the govt free software projects
host:M.Vamsi krishna
'''
from bokeh.plotting import figure, output_file, show

from bokeh.models import ColumnDataSource, HoverTool, WheelPanTool

import pandas as pd

df = pd.read_csv("https://code.swecha.org/CivicTech/Indian-govt-funding-free-software/-/raw/patch-1/list_of_projects_include_time_series_latest.csv", encoding='cp1252')

source = ColumnDataSource(df)

output_file("patch_1.html")

fund = figure(toolbar_location="below")

fund.xaxis.axis_label = 'Year of project release'

fund.yaxis.axis_label = 'No of projects funded with respect to years from 2000'

fund.square_dot(
    x='year', y='Noofprojects', size=10, fill_alpha=1.0, fill_color='white', 
    line_alpha=1.5, line_color='#8080ff', line_width=1.5, 
    legend_label="Represents no of organisations & funded Statistics",
    muted_color='white', muted_alpha=0.4, source=source)

fund.line(
    y='Noofprojects', x='year', line_width=1.2, color="#8080ff", line_dash='4 4',
    legend_label="Statistical report of growth in software", muted_color='blue', 
    muted_alpha=0.2, source=source)

fund.circle( 
    y='Noofprojects', x='year', size=26,
    fill_color='#809fff', hover_fill_color="#ff8080", fill_alpha=0.05,
    line_color='#ff8080', legend_label='Variations in the No.of Software Releases/Year', 
    muted_color='white', muted_alpha=0.4, source=source)

hover = HoverTool()

pantool = WheelPanTool()

hover.tooltips = [("Organisation", "@Organization"), ("Name of the Software", "@NameofSoftware")]

fund.add_tools(hover, pantool)

fund.legend.location = "top_left"

fund.legend.click_policy = "mute"

show(fund)
