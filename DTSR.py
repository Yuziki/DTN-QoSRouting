from antColony import *
from utils import *
from scipy import stats

SWITCH_TH = 0.8

def DTSR(topo, req, TH = SWITCH_TH):
    global SWITCH_TH
    SWITCH_TH = TH
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
    switchAvoid(topo, t)
    ret = AntColonyRouting(topo, start, end, t)
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

def switchAvoid(topo, t):
    for i in range(topo.satNum):
        for j in range(topo.satNum):
            if topo.lifeTime[t][i][j] < 0 or topo.lifeTime[t][i][j] > topo.duration:
                continue
            p = 1 - stats.poisson.cdf(topo.lifeTime[t][i][j] / 20, AVG_LT / 20)
            if (p > SWITCH_TH):
                topo.cost[i][j] = INF
