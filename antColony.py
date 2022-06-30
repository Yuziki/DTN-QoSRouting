import imp
from utils import *

import numpy as np

antNum = 30
ALPHA = 1 #信息素重要程度因子
BETA = 0.1 #启发函数重要程度因子
RHO = 0.1 #信息素挥发因子
Q = 100 #单只蚂蚁携带信息素数量
ITER_TIME = 50 #迭代次数

def AntColonyRouting(topo, start, end, t):
	np.random.seed()
	num = topo.satNum
	Tau = np.ones((num, num)) # 信息素矩阵
	Poss = np.zeros((num, num)) # 概率矩阵
	Eta = 1 / topo.cost # 启发矩阵
	bestPath = []
	minCost = INF
	for iter in range(ITER_TIME):
		Poss = np.power(Tau, ALPHA) * np.power(Eta, BETA)
		paths = []
		pathcosts = []
		for i in range(antNum):
			#每只蚂蚁前往终点
			visit = [start]
			cur = start
			while visit[-1] != end:
				p = np.random.rand()
				neis = []
				for nei in topo.satellites[cur].neis[t]:
					if nei not in visit:
						neis.append(nei)
				totalPoss = 0
				for nei in neis:
					totalPoss += Poss[cur][nei]
				if totalPoss == 0: #没有可用邻居
					break
				for nei in neis:
					if p < Poss[cur][nei] / totalPoss:
						visit.append(nei)
						cur = nei
						break
					else:
						p -= Poss[cur][nei] / totalPoss
			totalDelay = 0
			if visit[-1] == end:
				for j in range(len(visit) - 1):
					totalDelay += topo.cost[visit[j]][ visit[j + 1]]
			#print(totalDelay)
			if totalDelay != 0:
				paths.append(visit)
				pathcosts.append(totalDelay)
				if totalDelay < minCost:
					bestPath = visit
					minCost = totalDelay
		#更新信息素
		deltaTau = np.zeros((num, num))
		for i in range(len(paths)):
			for j in range(len(paths[i]) - 1):
				deltaTau[paths[i][j]][paths[i][j + 1]] += Q / pathcosts[i]
		Tau = (1 - RHO) * Tau + deltaTau
	if bestPath == []:
		minCost = 0
	return [bestPath, minCost]
		
			








