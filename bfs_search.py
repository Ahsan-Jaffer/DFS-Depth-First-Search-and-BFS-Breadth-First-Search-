#   [1,2,3,4]
# enque(5) -------------->   [1,2,3,4,5]
# deque() --------------->   [2,3,4,5]
# [2,3,4,5].pop() ------------------> [2,3,4]
# [2,3,4,5].popleft() --------------> [3,4,5]


from collections import deque

def bfs_search(tree, start_node, goal):
    visited = set()

    visited.add(start_node)
    queue = deque([start_node])
    print(queue)

    while queue:
        node = queue.popleft()
        print(node, end= " ")
        
        if node is goal:
            print("\nGoal node found!")
            return  
        

        for child in tree[node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)


tree = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
}


bfs_search(tree,'A','D')


