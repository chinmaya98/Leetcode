class Solution:
    def canFinish(self, numCourses:int, prerequisities:List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a,b in prerequisities:
            graph[b].append(a)
            indegree[a] +=1

        queue = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)
        
        count = 0

        while queue:
            node = queue.popleft()
            count += 1
            for n in graph[node]:
                indegree[n] -=1
                if indegree[n] == 0:
                    queue.append(n)
        return count == numCourses


