class Solution:
    def checkIfPrerequisite(self, numCou:int, prereq: List[List[int]], queries:List[List[int]]) -> List[bool]:
        indegree = [0] * numCou
        graph = defaultdict(list)
        isprereq = [set() for _ in range(numCou)]

        for a,b in prereq:
            graph[a].append(b)
            indegree[b] += 1
        
        queue = deque()
        for n in range(numCou):
            if indegree[n] == 0:
                queue.append(n)

        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                isprereq[nei].add(node)
                isprereq[nei].update(isprereq[node])
                indegree[nei] -=1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return [u in isprereq[v] for u, v in queries]
