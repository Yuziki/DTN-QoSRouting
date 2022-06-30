from cgi import print_form
from queue import LifoQueue
from satellite import Satellite
from utils import *
import numpy as np




class Topology():
	def __init__(self):
		self.satNum = 0
		self.duration = 0
		self.satellites = []
		self.cost = []
		self.lifeTime = []

	def readTopoFromTxt(self, posFilePath, linkFilePath):
		pFile = open(posFilePath, "r")
		lFile = open(linkFilePath, "r")
		#position
		for line in pFile:
			line = line.split()
			id = int(line[1])
			lon = float(line[2])
			lat = float(line[3])
			hei = float(line[4])
			if len(self.satellites) <= id:
				tmpSat = Satellite(id)
				tmpSat.lon.append(lon)
				tmpSat.lat.append(lat)
				tmpSat.height.append(hei)
				self.satellites.append(tmpSat)
			else:
				tmpSat = self.satellites[int(id)]
				tmpSat.lon.append(lon)
				tmpSat.lat.append(lat)
				tmpSat.height.append(hei)
		self.satNum = len(self.satellites)
		self.duration = len(self.satellites[0].lon)
		#link
		prevt = -1
		for line in lFile:
			line = line.split()
			t = int(line[0])
			id = int(line[1])
			if (t > prevt):
				prevt = t
				for i in range(self.satNum):
					self.satellites[i].neis.append(set())
			for nei in line[2:]:
				nei = int(nei)
				if nei >= 0 and nei < self.satNum:
					self.satellites[id].neis[t].add(nei)
					self.satellites[nei].neis[t].add(id)

	def updateCost(self, t):
		self.cost = np.ones((self.satNum, self.satNum))
		self.cost[:] = INF 
		for sat in self.satellites:
			for nei in sat.neis[t]:
				self.cost[sat.id][nei] = sat.getDelayWith(self.satellites[nei], t)
				# self.cost[nei][sat.id] = sat.getDelayWith(self.satellites[nei], t)

	def recur(self, i, j, t, val):
		if t < 0 or self.lifeTime[t][i][j] != INF:
			return
		self.lifeTime[t][i][j] = val
		self.recur(i, j, t - 1, val + 1) 
		return

	def calcLifeTime(self):
		for i in range(self.duration):
			tmp = np.ones((self.satNum, self.satNum), dtype=int) # lifetime matrix
			tmp[:] = -1
			for sat in self.satellites:
				for nei in sat.neis[i]:
					tmp[sat.id][nei] = INF
			self.lifeTime.append(tmp)
			if i != 0:
				for j in range(self.satNum):
					for k in range(self.satNum):
						if self.lifeTime[i - 1][j][k] == INF and self.lifeTime[i][j][k] == -1:
							self.recur(j, k, i - 1, 1)