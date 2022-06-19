from satellite import Satellite
import antColony as ac

import numpy as np

INF = 1e9

class Topology():
	def __init__(self):
		self.satNum = 0
		self.satellites = []
		self.cost = []

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
		#link
		for line in lFile:
			line = line.split()
			id = int(line[1])
			neis = []
			for nei in line[2:]:
				nei = int(nei)
				if nei >= 0 and nei < self.satNum:
					neis.append(nei)
			self.satellites[int(id)].neighbour.append(neis)

	def update(self, t):
		self.cost = np.ones((self.satNum, self.satNum))
		self.cost[:] = INF 
		for sat in self.satellites:
			for nei in sat.neighbour[t]:
				self.cost[sat.id][nei] = sat.getDelayWith(self.satellites[nei], t)

			
		

topo = Topology()
topo.readTopoFromTxt("position.txt", "link.txt")
ac.AntColonyRouting(topo, np.random.randint(topo.satNum), np.random.randint(topo.satNum), np.random.randint(10))