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