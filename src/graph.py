import random

class Edge:
    def __init__(self, destination):
        self.destination = destination

class Vertex:
    def __init__(self, value, color, **pos):
        self.value = value
        self.color = 'white'
        self.pos = pos
        self.edges = []

    def handEdge(self, edge):
        self.edges.append(edge)

class Graph:
    def __init__(self):
        self.vertexes = []


    # def debug_create_test_data(self):
    #     debug_vertex_1 = Vertex("t1", x=10, y=20)
    #     debug_vertex_2 = Vertex("t2", x=300, y=400)
    #     debug_vertex_3 = Vertex("t3", x=200, y=250)
    #     debug_vertex_4 = Vertex("t4", x=400, y=450)

    #     debug_edge_1 = Edge(debug_vertex_1)
    #     debug_edge_2 = Edge(debug_vertex_2)
    #     debug_edge_3 = Edge(debug_vertex_3)
    #     debug_edge_4 = Edge(debug_vertex_4)

    #     debug_vertex_1.edges.append(debug_edge_2)
    #     debug_vertex_2.edges.append(debug_edge_1)

    #     debug_vertex_2.edges.append(debug_edge_3)
    #     debug_vertex_3.edges.append(debug_edge_2)

    #     debug_vertex_1.edges.append(debug_edge_4)
    #     debug_vertex_4.edges.append(debug_edge_1)

    #     self.vertexes.extend(
    #         [debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4])















    # def debug_create_test_data(self):
    #     debug_vertex_1 = Vertex('t1', x = 50, y = 100)
    #     debug_vertex_2 = Vertex('t2', x = 200, y = 20)
    #     debug_vertex_3 = Vertex('t3', x = 100, y = 400)
    #     debug_vertex_4 = Vertex('t4', x = 400, y = 250)
        
    #     debug_edge_1 = Edge(debug_vertex_1)
    #     debug_edge_2 = Edge(debug_vertex_2)
    #     debug_edge_3 = Edge(debug_vertex_3)
    #     debug_edge_4 = Edge(debug_vertex_4)

    #     debug_vertex_1.edges.append(debug_edge_2)
    #     debug_vertex_2.edges.append(debug_edge_1)

    #     debug_vertex_2.edges.append(debug_edge_3)
    #     debug_vertex_3.edges.append(debug_edge_2)

    #     debug_vertex_3.edges.append(debug_edge_4)
    #     debug_vertex_2.edges.append(debug_edge_4)
        

    #     print('deb', debug_edge_3)
        
    #     # debug_vertex_4.edges.append(debug_edge_4)

    #     self.vertexes.extend([debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4])

    

    def randomize(self, width, height, px_box, prob=0.6):
        print('rand')
        def connect_verts(v0, v1):
            v0.edges.append(Edge(v0))
            v1.edges.append(Edge(v1))
        

        counter = 0
    
        grid = []

        for y in range(height):
            row = []
            for x in range(width):
                v = Vertex('default', 'red', x=100, y=100 )
                v.value = f"v{counter}"
                counter += 1
                row.append(v)
            grid.append(row)



        for y in range(height):
            for x in range(width):
                if y < height - 1:
                    if random.random() < prob:
                        connect_verts(grid[y][x], grid[y+1][x])
                if x < width - 1:
                    if random.random() < prob:
                        connect_verts(grid[y][x], grid[y][x+1])


        box_buffer = 0.7
        box_inner = px_box * box_buffer
        box_inner_offset = (px_box - box_inner) / 2 + 10

        for y in range(height):
            for x in range(width):
                grid[y][x].pos['x'] = (
                    x * px_box + box_inner_offset + random.random() * box_inner 
                ) 
                grid[y][x].pos['y'] = (
                    y * px_box + box_inner_offset + random.random() * box_inner 
                )

        for y in range(height):
            for x in range(width):
                self.vertexes.append(grid[y][x])

    
    def bfs(self, start):
        random_color = "#"+''.join([random.choice('012345679ABCDEF') for j in range(6)])
        # random_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        # random_color = 'red'
        queue = []
        found = []

        queue.append(start)
        found.append(start)

        start.color = random_color

        while len(queue) > 0:
            v = queue[0]
            print(queue)
            for edge in v.edges:
                if edge.destination not in found:
                    found.append(edge.destination)
                    queue.append(edge.destination)
                    edge.destination.color = random_color
                queue.pop(0)
        return found
