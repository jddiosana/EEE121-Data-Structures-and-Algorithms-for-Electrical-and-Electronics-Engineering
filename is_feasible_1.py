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