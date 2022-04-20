statesNeeded = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

finalStations = set()

while statesNeeded:
    bestStation = None
    statesCovered = set()
    for station, stateForStation in stations.items():
        covered = statesNeeded & stateForStation
        if len(covered) > len(statesCovered):
            bestStation = station
            statesCovered = covered
            
    statesNeeded -= statesCovered
    finalStations.add(bestStation)

print(finalStations)