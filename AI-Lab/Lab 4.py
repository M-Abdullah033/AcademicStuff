#Lab Task 1
'''
dict_graph = {}
with open('data.txt', 'r') as f:
    for l in f:
        city_a, city_b, p_cost = l.split()
        if city_a not in dict_graph:
            dict_graph[city_a] = {}
        dict_graph[city_a][city_b] = int(p_cost)
        if city_b not in dict_graph:
            dict_graph[city_b] = {}
        dict_graph[city_b][city_a] = int(p_cost)
        
def DepthFirstSearch(graph, src, dst):
    stack = [(src, [src], 0)]
    visited = {src}
    while stack:
        (node, path, cost) = stack.pop()
        for temp in graph[node].keys():
            if temp == dst:
                return path + [temp], cost + graph[node][temp]
            else:
                if temp not in visited:
                    visited.add(temp)
                    stack.append((temp, path + [temp], cost + graph[node][temp]))
'''

#Lab Task 2
'''row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]
 
 

def isSafe(x, y, processed):
    return (0 <= x < len(processed)) and (0 <= y < len(processed[0]))\
        and not processed[x][y]
 
 
def searchBoggle(board, words, result, processed, i, j, path=''):
    processed[i][j] = True
 
    path += board[i][j]
 
    if path in words:
        result.add(path)
 
    for k in range(len(row)):
        if isSafe(i + row[k], j + col[k], processed):
            searchBoggle(board, words, result, processed, i + row[k], j + col[k], path)
 
    processed[i][j] = False
 
 
def searchInBoggle(board, words):
 
    result = set()
 
    if not board or not len(board):
        return
 
    (M, N) = (len(board), len(board[0]))
 
    processed = [[False for x in range(N)] for y in range(M)]
 
    for i in range(M):
        for j in range(N):

            searchBoggle(board, words, result, processed, i, j)
 
    return result
 
 
if __name__ == '__main__':
 
    board = [
        ['M', 'S', 'E'],
        ['R', 'A', 'T'],
        ['L', 'O', 'N']
    ]
 
    words = ['STAR', 'NOTE', 'SAND', 'STONE']
 
    validWords = searchInBoggle(board, words)
    print(validWords)
'''
