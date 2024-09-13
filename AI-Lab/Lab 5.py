#Iterative Deepening Search Method

#Lab Activity
'''
def iterative_deepening_dfs(start, target):
    """
    Implementation of iterative deepening DFS (depth-first search) algorithm to find the shortest path from a start to a target node..
    Given a start node, this returns the node in the tree below the start node with the target value (or null if it doesn't exist)
    Runs in O(n), where n is the number of nodes in the tree, or O(b^d), where b is the branching factor and d is the depth.
    :param start:  the node to start the search from
    :param target: the value to search for
    :return: The node containing the target value or null if it doesn't exist.
    """
    # Start by doing DFS with a depth of 1, keep doubling depth until we reach the "bottom" of the tree or find the node we're searching for
    depth = 1
    print(start)
    bottom_reached = False  # Variable to keep track if we have reached the bottom of the tree
    while not bottom_reached:
        # One of the "end nodes" of the search with this depth has to still have children and set this to False again
        result, bottom_reached = iterative_deepening_dfs_rec(start, target, 0, depth)
        if result is not None:
            # We've found the goal node while doing DFS with this max depth
            return result

        # We haven't found the goal node, but there are still deeper nodes to search through
        depth *= 2
        print("Increasing depth to " + str(depth))

    # Bottom reached is True.
    # We haven't found the node and there were no more nodes that still have children to explore at a higher depth.
    return None


def iterative_deepening_dfs_rec(node, target, current_depth, max_depth):
    print("Visiting Node " + str(node["value"]))

    if node["value"] == target:
        # We have found the goal node we we're searching for
        print("Found the node we're looking for!")
        return node, True

    if current_depth == max_depth:
        print("Current maximum depth reached, returning...")
        # We have reached the end for this depth...
        if len(node["children"]) > 0:
            # ...but we have not yet reached the bottom of the tree
            return None, False
        else:
            return None, True

    # Recurse with all children
    bottom_reached = True
    for i in range(len(node["children"])):
        result, bottom_reached_rec = iterative_deepening_dfs_rec(node["children"][i], target, current_depth + 1,
                                                                 max_depth)
        if result is not None:
            # We've found the goal node while going down that child
            return result, True
        bottom_reached = bottom_reached and bottom_reached_rec

    # We've gone through all children and not found the goal node
    return None, bottom_reached

start={"value": 0, "children":[
   {"value": 1, "children":[
     {"value": 3, "children":[  ]},
     {"value": 4, "children":[ ]}
     ]}, {
         "value": 2, "children":[
             {"value": 5, "children":[ ]},
             {"value": 6, "children":[ ]}
             ]
         }
   ]
}


print(iterative_deepening_dfs(start, 6) ["value"])
'''

#Lab Task 1
'''
dict_graph = {}
def IterativeDeepening(graph, src, dst):
    level = 0
    count = 0
    stack = [(src, [src], 0)]
    visited = {src}
    while True:
        level += 1
        while stack:
            if count <= level:
                count = 0
                (node, path, cost) = stack.pop()
                for temp in graph[node].keys():
                    if temp == dst:
                        return path + [temp], cost + graph[node][temp]
                    else:
                        if temp not in visited:
                            visited.add(temp)
                            count += 1
                            stack.append((temp, path + [temp], cost + graph[node][temp]))
            else:
                q = stack
                visited_bfs = {src}
                while q:
                    (node, path, cost) = q.pop(0)
                    for temp in graph[node].keys():
                        if temp == dst:
                            return path + [temp], cost + graph[node][temp]
                        else:
                            if temp not in visited_bfs:
                                visited_bfs.add(temp)
                                q.append((temp, path + [temp], cost + graph[node][temp]))
                break


n = 1
print (dict_graph)
print ("------------------------------------------------")
while n == 1:
    x = input("enter the type of search you want to do \n1.BFS 2.DFS 3.ID:: \n ")
    if x == 1:
        src = raw_input("Enter the source: ")
        dst = raw_input("Enter the Destination: ")
        while src not in dict_graph or dst not in dict_graph:
            print ("No such city name")
            src = raw_input("Enter the correct source (case_sensitive):\n")
            dst = raw_input("Enter the correct destination(case_sensitive):\n ")
        print ("for BFS")
        print (BreadthFirstSearch(dict_graph, src, dst))

    elif x == 2:
        src = raw_input("Enter the source: ")
        dst = raw_input("Enter the Destination: ")
        while src not in dict_graph or dst not in dict_graph:
            print ("No such city name")
            src = raw_input("Enter the correct source (case_sensitive):\n")
            dst = raw_input("Enter the correct destination(case_sensitive):\n ")
        print ("for DFS")
        print (DepthFirstSearch(dict_graph, src, dst))

    elif x == 3:
        src = raw_input("Enter the source:")
        dst = raw_input("Enter the Destination: ")
        while src not in dict_graph or dst not in dict_graph:
            print ("No such city name")
            src = raw_input("Enter the correct source (case_sensitive):\n")
            dst = raw_input("Enter the correct destination(case_sensitive):\n")
        print ("for ID")
        print (IterativeDeepening(dict_graph, src, dst))

    n = input("enter 1 if you wish to continue:\n")
'''
