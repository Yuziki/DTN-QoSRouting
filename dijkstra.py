
from utils import *

def DijkstraRouting(topo, req):
	result = Result()
	result.duration = req.dur
	recur(topo, req.start, req.end, req.t, req.dur, result)
	if result.delay == 0:
		result.lossRate = 1
	else:
		result.lossRate = result.lossTime / req.dur
		result.delay /= req.dur
	return result

def recur(topo, start, end, t, dur, result):
	topo.updateCost(t)
	ret = dijkstra(topo, start, end, t)
	path = ret[0]
	result.paths.append(path)
	minLT = INF
	for i in range(len(path) - 1):
		minLT = min(minLT, topo.lifeTime[t][path[i]][path[i + 1]])
	if minLT < dur:
		result.lossTime += REROUTING_TIME
		result.delay += ret[1] * minLT
		recur(topo, start, end, t + minLT, dur - minLT, result)
	else:
		result.delay += ret[1] * dur

def dijkstra(topo, start, end, t):
	topo.updateCost(t)
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
		for nei in topo.satellites[cur].neis[t]:
			if cost[cur] + topo.cost[cur][nei] <  cost[nei]:
				cost[nei] = cost[cur] + topo.cost[cur][nei]
				prev[nei] = cur
	path = [cur]
	while prev[cur] != -1:
		path.append(prev[cur])
		cur = prev[cur]
	path.reverse()
	delay = 0
	for i in range(len(path) - 1):
		delay += topo.cost[path[i]][path[i + 1]]
	return [path, delay]	

		

