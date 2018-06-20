import math
import random

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8

from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()
print(graph_data.vertexes[0])

N=len(graph_data.vertexes)
# n_am = len(N)
node_indices = list(range(N))
randNode = random.choice(node_indices)
print(randNode)
print(N)
print(node_indices)
# debug_pallete = Spectral8
# debug_pallete.append('#ff0000')
# debug_pallete.append('#0000ff')

color_list = [
    "#FF0000",
    "#AA0099"
]
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)

plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,1.1), y_range=(-1.1,1.1),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color='color')

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
print(graph.edge_renderer.data_source.data)  
# print('start' in graph.edge_renderer.data_source.data)  
# print(node_indices)  

### start of layout code
# circ = [i*2*math.pi/8 for i in node_indices]
x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)