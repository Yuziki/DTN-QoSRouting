
def DijkstraRouting(topo, start, end, t):
	cost = [1e9 for i in range(topo.satNum)]
	prev = [-1 for i in range(topo.satNum)]
	cost[start] = 0
	visit = set()
	cur = -1
	while True:
		minCost = 1e9
		for i in range(topo.satNum):
			if cost[i] < minCost and i not in visit:
				minCost = cost[i]
				cur = i
		if cur == end:
			break
		visit.add(cur)
		for nei in topo.satellites[cur].neighbour[t]:
			if cost[cur] + topo.cost[cur][nei] <  cost[nei]:
				cost[nei] = cost[cur] + topo.cost[cur][nei]
				prev[nei] = cur
	path = [cur]
	while prev[cur] != -1:
		path.append(prev[cur])
		cur = prev[cur]
	path.reverse()
	return path	

		

