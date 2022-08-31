import plotly.figure_factory as ff
import pandas as pa
import csv

df = pa.read_csv("data.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"])
fig.show()