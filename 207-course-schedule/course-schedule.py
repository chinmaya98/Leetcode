class Solution:
    def canFinish(self, numCou : int, prereq:List[List[int]]) -> bool:
        indegree = [0] * numCou
        graph = defaultdict(list)

        for a,b in prereq:
            graph[b].append(a)
            indegree[a] +=1
        
        queue = deque()
        for n in range(numCou):
            if indegree[n] == 0:
                queue.append(n)

        count = 0
        while queue:
            node = queue.popleft()
            count +=1
            for nei in graph[node]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    queue.append(nei)
        return count == numCou