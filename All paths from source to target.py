class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node,path):
            if node==lastNode:
                output.append(path)
            for neighbour in graph[node]:
                dfs(neighbour,path+[neighbour])
        lastNode=len(graph)-1
        output=[]
        dfs(0,[0])
        return output
