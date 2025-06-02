class Solution:
    def findOrder(self, numCou:int, prereq:List[List[int]]) -> List[int]:
        indegree = [0] * numCou
        graph = defaultdict(list)

        for a,b in prereq:
            graph[b].append(a)
            indegree[a] +=1
        
        queue = deque()
        for n in range(numCou):
            if indegree[n] == 0:
                queue.append(n)
        
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for nei in graph[node]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    queue.append(nei)
        if len(result) == numCou:
            return result
        else:
            return []