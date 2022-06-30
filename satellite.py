from math import * 

lightSpeed = 3e8
EARTH_RADIUS = 6378

def disBetween(a, b, t):
	x1 = (a.height[t] + EARTH_RADIUS) * cos(a.lat[t]) * cos(a.lon[t])
	y1 = (a.height[t] + EARTH_RADIUS) * cos(a.lat[t]) * sin(a.lon[t])
	z1 = (a.height[t] + EARTH_RADIUS) * sin(a.lat[t])

	x2 = (b.height[t] + EARTH_RADIUS) * cos(b.lat[t]) * cos(b.lon[t])
	y2 = (b.height[t] + EARTH_RADIUS) * cos(b.lat[t]) * sin(b.lon[t])
	z2 = (b.height[t] + EARTH_RADIUS) * sin(b.lat[t])

	return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2)) * 1000  

class Satellite():
	def __init__(self, id = -1):
		self.id = id
		self.lon = []
		self.lat = []
		self.height = []
		self.neis = []

	def getDelayWith(self, nei, t):
		#计算时延，单位s
		dis = disBetween(self, nei, t)
		return dis / lightSpeed * 1000

