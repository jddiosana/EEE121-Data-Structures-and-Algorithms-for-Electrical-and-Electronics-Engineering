def is_feasible(graph, source, sink, flow_value):

    start_value = 1
    flow = {}
    flow[source] = start_value
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
                            
            #print(vertex_list)
            #print(flow)
            #print(inflow_counter)
            
        if len(vertex_new) == 0:
            return
        else:
            #print(vertex_new)
            flow_division(vertex_new)
        
    flow_division(graph.vertices)
    
    capacities = []
    tails = []
    min_tails = []
    
    for edge in graph.edges:
        capacities.append(edge.capacity)
        tails.append(edge.tail)
        
    for i in range(len(capacities)):
        if capacities[i] == min(capacities):
            min_tails.append(tails[i])
            
    max_flow = []
    
    for x in min_tails:
        flow_div = flow[x] / len(graph.out_edges(x))
        max_flow.append(flow_div)
    
    max_value = min(capacities) / max(max_flow)
    
    if max_value >= flow_value:
        return True
    else:
        return False
    
    raise NotImplementedError('You must implement the function without changing the function name and argument list.')
     