import math
import random

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, Oval, ColumnDataSource, Range1d, LabelSet, Label
from bokeh.palettes import Spectral8


from graph import *

WIDTH = 640
HEIGHT = 480
CIRCLE_SIZE = 30

graph_data = Graph()
# graph_data.debug_create_test_data()
graph_data.randomize(10, 10, 50, 20)
# print(graph_data.vertexes[0])
graph_data.bfs(graph_data.vertexes[0])

N=len(graph_data.vertexes)
# n_am = len(N)
node_indices = list(range(N))
# randNode = random.choice(node_indices)
# print(randNode)
# print(N)
# print(node_indices)
# debug_pallete = Spectral8
# debug_pallete.append('#ff0000')
# debug_pallete.append('#0000ff')

color_list = []

for vertex in graph_data.vertexes:
    color_list.append(vertex.color)

plot = figure(title='Graph Layout Demonstration', x_range=(0, WIDTH), y_range=(0, HEIGHT),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Circle(size=CIRCLE_SIZE, fill_color='color')

start_n = []
end_n = []

# i == verts
# j == edges

for i in graph_data.vertexes:
    for j in i.edges:
        start_n.append(graph_data.vertexes.index(i))
        end_n.append(graph_data.vertexes.index(j.destination))

graph.edge_renderer.data_source.data = dict(
    # start=random.choice(graph_data.vertexes) * graph_data.vertexes,
    start=start_n,
    end=end_n)
# print(graph.edge_renderer.data_source.data(node_indices))
# print(graph.edge_renderer.data_source.data)  
# print('start' in graph.edge_renderer.data_source.data)  
# print(node_indices)  

### start of layout code
# circ = [i*2*math.pi/8 for i in node_indices]
x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]


graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, Range1d, LabelSet, Label

output_file("label.html", title="label.py example")

source = ColumnDataSource(data=dict(height=[0, 71, 72, 68, 58, 62],
                                    weight=[0, 189, 220, 141, 260, 174],
                                    names=['Mark', 'Amir', 'Matt', 'Greg',
                                           'Owen', 'Juan']))

# new dictionary for data source, 3 lists, ordered as vertexes
# list of x vals 
# list of y vals
# list of labels

value = [v.value for v in graph_data.vertexes] #TODO: Optimization: Run through loop 3 times

label_source = ColumnDataSource(data=dict(x=x, y=y, v=value))

labels = LabelSet(x='x', y='y', text='v', level='overlay',
              source=label_source, render_mode='canvas', text_align='center', text_baseline='middle')

# citation = Label(x=70, y=70, x_units='screen', y_units='screen',
#                  text='Collected by Luke C. 2016-04-01', render_mode='css',
#                  border_line_color='black', border_line_alpha=1.0,
#                  background_fill_color='white', background_fill_alpha=1.0)

#TODO: plot.add_layout vs plot.renderers.append
plot.add_layout(labels)
# plot.add_layout(citation)

# show(p)



output_file('graph.html')
show(plot)