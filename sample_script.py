from header_script import *

def in_degree(graph, vertex):
    return len(graph.in_edges(vertex))
    raise NotImplementedError('You must implement the function without changing the function name and argument list.')

def check_constraints(graph, source, sink, flow):
        
    #Constraint no. 1
    for edge in graph.edges:
        for flows in flow:
            if (edge.tail, edge.head) == flows:
                if edge.capacity < flow[flows]:
                    return False #returns false once a flow greater than capacity is detected
                    
    #Constraint no. 2          
    vertices_wo_ss = [] #(vertices without source/sink) source and sink removed for checking constraint #2        

    for vertex in graph.vertices:
        vertices_wo_ss.append(vertex)  
    for vertex_new in vertices_wo_ss:
        if vertex_new == source or vertex_new == sink:
            vertices_wo_ss.remove(vertex_new)
        
    for k in vertices_wo_ss:
        inflow = 0
        outflow = 0
        for kk in graph.edges:
            if k == kk.head:
                for flows in flow:
                    if (kk.tail, kk.head) == flows:
                        inflow += flow[flows] #adds the total inflows for each edge
            if k == kk.tail:
                for flows in flow:
                    if (kk.tail, kk.head) == flows:
                        outflow += flow[flows] #adds total outflows for each edge
        
        if not is_equal(inflow, outflow):
            return False #returns false once an edge with different inflow and outflow is detected
        
    #Constraint no. 3
    vertices_wo_sink = vertices_wo_ss + [source] #sink should not be part of constraint checking no. 3

    for y in vertices_wo_sink:
        outflow = []
        for n in graph.edges:
            if y == n.tail:
                for flows in flow:
                    if (n.tail, n.head) == flows:
                        outflow.append(flow[flows]) #appends all the outflows occurring on each edge
                    
        for i in outflow:
            if not is_equal(i, outflow[0]): 
                return False #returns false if one flow is not equal to other outflows (same edge)
            
    return True #returns true if and only if constraint checking 1-3 do not return false        
            
    raise NotImplementedError('You must implement the function without changing the function name and argument list.')

def is_feasible(graph, source, sink, flow_value):

    flow = {}
    flow[source] = flow_value
    inflows = {}
    inflow_counter = {}
    inflows[source] = 0
    inflow_counter[source] = 0

    for x in graph.vertices:
        if x != source:
            flow[x] = 0
            inflows[x] = len(graph.in_edges(x))
            inflow_counter[x] = 0

    def flow_division(vertex_list):
    
        vertex_new = [] 
        
        while len(vertex_list) > 0:
            
            tail = vertex_list[0]
            vertex_list.remove(vertex_list[0])
            
            for edge in graph.edges:
                if edge.tail == tail:
                    if inflows[edge.tail] - inflow_counter[edge.tail] == 0:
                        outflows = len(graph.out_edges(edge.tail))
                        flow[edge.head] += (flow[edge.tail] / outflows)
                        inflow_counter[edge.head] += 1
                        
                    else:
                        if edge.tail not in vertex_new:
                            vertex_new.append(edge.tail)
                                    
        if len(vertex_new) == 0:
            return
        
        else:
            flow_division(vertex_new)
            
    vertices = [i for i in graph.vertices] 
        
    flow_division(vertices)

    flow_each_edge = {}
    
    for edge in graph.edges:
        flow_each_edge[(edge.tail, edge.head)] = flow[edge.tail] / len(graph.out_edges(edge.tail))

        
    for edge in graph.edges:
        for flows in flow_each_edge:
            if (edge.tail, edge.head) == flows:
                if edge.capacity < flow_each_edge[flows]:
                    return False
    
    return True
    
    raise NotImplementedError('You must implement the function without changing the function name and argument list.')       

def max_equal_split_flow(graph, source, sink):
    
    edges = []
    edge_per_index = {}
        
    for edge in graph.edges:
        
        if graph.vertices.index(edge.tail) not in edge_per_index:
            edge_per_index[graph.vertices.index(edge.tail)] = [edge]
            
        else:
            edge_per_index[graph.vertices.index(edge.tail)].append(edge)
    
    for i in range(len(graph.vertices)-1):
        edges += edge_per_index[i]
    
    
    flow = {}
    flow[source] = 1 #let the flow value of the source = 1 (or 100% of starting value)
    
                
    edges_new = edges.copy()

    for x in graph.vertices:
        if x != source:
            flow[x] = 0
            
    while len(edges) > 0:
        
        edge_tail = edges[0].tail
        edge_head = edges[0].head
        edges.pop(0)
        
        #if edge_tail == tail:
                        
        outflows = len(graph.out_edges(edge_tail))
        flow[edge_head] += (flow[edge_tail] / outflows)
        
                                       
    capacities = [(edge.capacity/ (flow[edge.tail] / len(graph.out_edges(edge.tail)))) for edge in edges_new] #appends all capacities in a list                      
    
    def find_max_split(capacity, left, right, min):
 
        # if the list contains only one element
     
        if left == right:               
     
            if min > capacity[right]:         
                min = capacity[right]
         
            return min
     
        # if the list contains only two elements
     
        if right - left == 1:          
     
            if capacity[left] < capacity[right]:      
                if min > capacity[left]:       
                    min = capacity[left]
          
            else:
                if min > capacity[right]:      
                    min = capacity[right]
         
            return min
     
        mid = (left + right) // 2
     
        min = find_max_split(capacity, left, mid, min)
     
        min = find_max_split(capacity, mid + 1, right, min)
     
        return min
    
    max_split = find_max_split(capacities, 0, len(capacities)-1, 99999)    
           
             
    return max_split #returns the minimum value (or the maximum value that satisfies all constraints) from the assumed starting values.
    
    raise NotImplementedError('You must implement the function without changing the function name and argument list.')
    
   
def max_equal_split_flow_upgrade(graph, source, sink):
    
    edges = []
    edge_per_index = {}
        
    for edge in graph.edges:
        
        if graph.vertices.index(edge.tail) not in edge_per_index:
            edge_per_index[graph.vertices.index(edge.tail)] = [edge]
            
        else:
            edge_per_index[graph.vertices.index(edge.tail)].append(edge)
    
    for i in range(len(graph.vertices)-1):
        edges += edge_per_index[i]
    
    
    flow = {}
    flow[source] = 1 #let the flow value of the source = 1 (or 100% of starting value)
    
    edges_new = edges.copy()

    for x in graph.vertices:
        if x != source:
            flow[x] = 0
            
    while len(edges) > 0:
        
        edge_tail = edges[0].tail
        edge_head = edges[0].head
        edges.pop(0)
        
        #if edge_tail == tail:
                        
        outflows = len(graph.out_edges(edge_tail))
        flow[edge_head] += (flow[edge_tail] / outflows)
        
                                       
    capacities = [(edge.capacity/ (flow[edge.tail] / len(graph.out_edges(edge.tail)))) for edge in edges_new] #appends all capacities in a list                      
    
    def find_max_split(capacity, left, right, min):
 
        # if the list contains only one element
     
        if left == right:               
     
            if min > capacity[right]:         
                min = capacity[right]
         
            return min
     
        # if the list contains only two elements
     
        if right - left == 1:          
     
            if capacity[left] < capacity[right]:      
                if min > capacity[left]:       
                    min = capacity[left]
          
            else:
                if min > capacity[right]:      
                    min = capacity[right]
         
            return min
     
        mid = (left + right) // 2
     
        min = find_max_split(capacity, left, mid, min)
     
        min = find_max_split(capacity, mid + 1, right, min)
     
        return min
    
    max_split = find_max_split(capacities, 0, len(capacities)-1, 99999)    
   
    capacities.remove(max_split)

    new_max = find_max_split(capacities, 0, len(capacities)-1, 9999)        
             
    return new_max #returns the minimum value (or the maximum value that satisfies all constraints) from the assumed starting values.
    
    raise NotImplementedError('You must implement the function without changing the function name and argument list.')
    
def grid_graph(width, height, common_capacity):
    vertices = [(x,y) for x in range(width + 1) for y in range(height + 1)]
    capacities = [common_capacity for _ in range(width*(height + 1) + height*(width + 1))]
    edges = [((x,y),(x + 1, y)) for x in range(width) for y in range(height + 1)] + [((x,y),(x, y + 1)) for x in range(width + 1) for y in range(height)]

    return Graph(vertices, edges, capacities)

def grid_graph_pseudorandom(width, height, seed):
    vertices = [(x,y) for x in range(width + 1) for y in range(height + 1)]
    edges = [((x,y),(x + 1, y)) for x in range(width) for y in range(height + 1)] + [((x,y),(x, y + 1)) for x in range(width + 1) for y in range(height)]

    capacities = [0 for _ in range(width*(height + 1) + height*(width + 1))]
    capacities[0] = seed
    for i in range(1, len(edges)):
        capacities[i] = (8121*capacities[i - 1] + 28411) % 134456
    
    for i in range(len(capacities)):
        capacities[i] = 1 + (capacities[i] % 100)
    
    return Graph(vertices, edges, capacities)

import itertools

if __name__ == '__main__':
    graph_a = Graph(list(range(1,9)), [(1,2), (2,5), (5,8), (1,3), (3,6), (6,8), (1,4), (4,7), (7,8)], [5,4,4, 3,7,2, 2,2,1])
    graph_b = Graph([1, 2, 4, 3, 6, 7, 5, 8], [(1,2), (2,5), (5,8), (1,3), (3,6), (6,8), (1,4), (4,7), (7,8)] + [(2,3), (4,3), (6,5), (6,7)], [5,4,4, 3,7,2, 2,2,1] + [9, 8, 7, 6])
    graph_c = Graph(list(range(1, 10)), [(1,2), (2,3), (1,4), (2,5), (3,6), (4,5), (5,6), (4,7), (5,8), (6,9), (7,8), (8,9)], [3, 4, 6, 2, 5, 5, 5, 8, 3, 3, 8, 2])
    graph_d = Graph(list(range(1, 10)), [(1,2), (2,3), (1,4), (2,5), (3,6), (4,5), (5,6), (4,7), (5,8), (6,9), (7,8), (8,9)] + [(2,6), (4,8)], [3, 4, 6, 2, 5, 5, 5, 8, 3, 3, 8, 2] + [6, 3])

    print('In-degrees of vertices in Graph B (Sub-task 0 example)')
    for v in graph_b.vertices:
        print(v, in_degree(graph_b, v), sep='\t')
    print()

    print('Brute-force enumeration of integer-valued feasible flows on a 2x1 grid using check_constraints:')
    
    tiny_grid = grid_graph(2, 1, 6)
    E = tiny_grid.edges
    for flow_values in itertools.product(range(1, 7), range(1, 7), range(1, 7), range(1, 7), range(1, 7), range(1, 7), range(1, 7)):
        flow = dict()
        for i in range(len(E)):
            flow[(E[i].tail, E[i].head)] = flow_values[i]

        if check_constraints(tiny_grid, (0,0), (2,1), flow):
            print(flow)
    
    print()
    print('Expected output for sample graphs given in MP specifications PDF')
    print('ID', 'no upgrade', 'with upgrade', sep='\t')
    sample_graph = {'A': graph_a, 'B': graph_b, 'C': graph_c, 'D': graph_d}
    source_vertex = {'A': 1, 'B': 1, 'C': 1, 'D': 1}
    sink_vertex = {'A': 8, 'B': 8, 'C': 9, 'D': 9}

    for graph_id in sample_graph:
        ans_no_upgrade = max_equal_split_flow(sample_graph[graph_id], source_vertex[graph_id], sink_vertex[graph_id])
        ans_with_upgrade = max_equal_split_flow_upgrade(sample_graph[graph_id], source_vertex[graph_id], sink_vertex[graph_id])

        print(graph_id, "{0:8.3f}".format(ans_no_upgrade), "{0:8.3f}".format(ans_with_upgrade), sep='\t')

    print()
    print('Expected output for a pseudorandom 20x20 square grid')
    print('no upgrade', 'with upgrade', sep='\t')
    for seed in range(10):
        medium_grid = grid_graph_pseudorandom(20, 20, seed)

        ans_no_upgrade = max_equal_split_flow(medium_grid, (0,0), (20,20))
        ans_with_upgrade = max_equal_split_flow_upgrade(medium_grid, (0,0), (20,20))

        print("{0:8.3f}".format(ans_no_upgrade), "{0:8.3f}".format(ans_with_upgrade), sep='\t')

    print()
    print('Expected output for a pseudorandom 100x100 square grid')
    print('no upgrade', 'with upgrade', sep='\t')
    for seed in range(10):
        large_grid = grid_graph_pseudorandom(100, 100, seed)

        ans_no_upgrade = max_equal_split_flow(large_grid, (0,0), (100,100))
        ans_with_upgrade = max_equal_split_flow_upgrade(large_grid, (0,0), (100,100))

        print("{0:8.3f}".format(ans_no_upgrade), "{0:8.3f}".format(ans_with_upgrade), sep='\t')
        
    '''large_grid = grid_graph_pseudorandom(100,100, 5)
    max_equal_split_flow(large_grid, (0,0), (100,100))'''