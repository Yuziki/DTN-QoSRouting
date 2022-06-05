import math as m

lightSpeed = 3e8
earthRadius = 63781370

def disBetween(a, b, t):
	lonDis = a.lon[t] - b.lon[t]
	latDis = a.lat[t] - b.lat[t]
	s = 2 * m.asin(
		m.sqrt(
			m.pow(m.sin(latDis / 2), 2) + m.cos(a.lat[t]) * m.cos(b.lat[t]) * m.pow(m.sin(lonDis / 2), 2)))
	return s * (earthRadius + max(a.height[t], b.height[t]) * 1000)

class Satellite():
	def __init__(self, id = -1):
		self.id = id
		self.lon = []
		self.lat = []
		self.height = []
		self.neighbour = []

	def getDelayWith(self, nei, t):
		#计算时延，单位s
		dis = disBetween(self, nei, t)
		return dis / lightSpeed * 1000

