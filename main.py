from topology import *
from utils import *
from DTSR import *
from dijkstra import *

topo = Topology()
topo.readTopoFromTxt("position.txt", "link.txt")
topo.calcLifeTime()

delay1 = []
delay2 = []
loss1 = []
loss2 = []
path1 = []
path2 = []


for i in range(100):
    req = Request(topo)
    result = DTSR(topo, req)
    delay1.append(result.delay)
    loss1.append(result.lossRate)
    path1.append(len(result.paths))
    # print("DTSR:")
    # print(result.paths, result.delay, result.lossRate)

    result = DijkstraRouting(topo,req)
    delay2.append(result.delay)
    loss2.append(result.lossRate)
    path2.append(len(result.paths))
    # print("Dijstra:")
    # print(result.paths, result.delay, result.lossRate)

print(sum(delay1) / len(delay1), " ", sum(delay2) / len(delay2))
print(sum(loss1) / len(loss1), " ", sum(loss2) / len(loss2))
print(sum(path1) / len(path1), " ", sum(path2) / len(path2))