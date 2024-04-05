def check_constraints(graph, source, sink, flow):
        
    #Constraint no. 1
    for edge in graph.edges:
        for flows in flow:
            if (edge.tail, edge.head) == flows: #compares capacity of and flow through the edge
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
            if k == kk.head: #checks if there is a flow into the vertex
                for flows in flow:
                    if (kk.tail, kk.head) == flows:
                        inflow += flow[flows] #adds the total inflows for each vertex
            if k == kk.tail: #checks if there is a flow out of the vertex
                for flows in flow:
                    if (kk.tail, kk.head) == flows:
                        outflow += flow[flows] #adds total outflows for each vertex
        
        if not is_equal(inflow, outflow):
            return False #returns false once an edge with different inflow and outflow is detected
        
    #Constraint no. 3
    vertices_wo_sink = vertices_wo_ss + [source] #sink should not be part of constraint checking no. 3

    for y in vertices_wo_sink:
        outflow = []
        for n in graph.edges:
            if y == n.tail: #checks all the outflows of the vertex
                for flows in flow:
                    if (n.tail, n.head) == flows:
                        outflow.append(flow[flows]) #appends all the outflows occurring on each edge
                    
        for i in outflow:
            if not is_equal(i, outflow[0]): 
                return False #returns false if at least one outflow is not equal to other outflows on the same vertex
            
    return True #returns true if and only if constraint checking 1-3 do not return false        
            
    raise NotImplementedError('You must implement the function without changing the function name and argument list.')
