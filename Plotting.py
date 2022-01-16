from video import df
from bokeh.plotting import figure, show, output_file
import pandas

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

p = figure(x_axis_type='datetime', height=100, width=500, sizing_mode="scale_width", title="Motion Graph")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

q = p.quad(left="Start", right="End", bottom=0, top=1, color="green")

output_file("Graph1.html")
show(p)
