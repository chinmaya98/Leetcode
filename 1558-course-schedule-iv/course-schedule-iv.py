class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        isprereq = [set() for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] +=1
        
        queue = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)
        

        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                indegree[nei] -=1
                isprereq[nei].add(node)
                isprereq[nei].update(isprereq[node])
                if indegree[nei] == 0:
                    queue.append(nei)
        return [u in isprereq[v] for u,v in queries]
        