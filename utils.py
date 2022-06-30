import numpy as np

INF = 1e9
AVG_LT = 200 # 平均业务时长
REROUTING_TIME = 10 # 重路由耗时

class Request():
    def __init__(self, topo) -> None:
        self.start = np.random.randint(topo.satNum)
        self.end = np.random.randint(topo.satNum)
        while self.end == self.start:
            self.end = np.random.randint(topo.satNum)
        self.t = np.random.randint(topo.duration - AVG_LT)
        self.dur = np.random.randint(AVG_LT * 0.8, AVG_LT * 1.2)
        
class Result():
    def __init__(self) -> None:
        self.paths = []
        self.delay = 0
        self.duration = 0
        self.lossTime = 0
        self.lossRate = 0