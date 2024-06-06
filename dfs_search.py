def dfs_search(tree, start_node, goal_node, visited = None):
    if visited is None:
        visited = set()

    visited.add(start_node)
    print(start_node, end=" ")

    if start_node == goal_node:
        return
    
    for child in tree[start_node]:
        if child not in visited:
            visited.add(child)
            dfs_search(tree,child,goal_node,visited)

            if goal_node in visited:
                break


my_tree = {
    "A" : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F','G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
}

pak_cities = {
    "Pakistan" : ["KPK", "PUNJAB", "SINDH", "BALOCHISTAN", "GB"],
    'KPK' : ['PESHAWAR', 'SWAT'],
    'PUNJAB' : ['LHR', 'FSD', 'RWP'],
    'SINDH' : [],
    'BALOCHISTAN' : ['QUETTA'],
    'GB' : [],
    'PESHAWAR' : [],
    'SWAT' : [],
    'LHR' : [],
    'FSD' : [],
    'RWP' : ['FAIZABAD'],
    'QUETTA' : [],
    'FAIZABAD' : [],
}

dfs_search(pak_cities,'Pakistan',"SWAT")

