import operator

"""
Scores the output file
"""
def scoreOutputFile(requests, endpoints):
    cachedVideos = readOutputFile()

    scoreNumerator = 0
    scoreDenominator = 0

    for request in requests:
        video, endpoint, cardinality = request
        rootServerLatency, nCaches = endpoints[endpoint][0]
        requestGain = outputFile_getLatencyGainForRequest(video, rootServerLatency, endpoints[endpoint][1], cachedVideos)

        scoreNumerator += requestGain * cardinality
        scoreDenominator += cardinality

    return (scoreNumerator / scoreDenominator) * 1000

"""
Used to get the latency gain of the caches versus root dc when scoring the output file.
"""
def outputFile_getLatencyGainForRequest(video, rootServerLatency, cacheConnections, cachedVideos):

        latencies = {}

        for cacheServer in cacheConnections.keys():
            latency = cacheConnections[cacheServer]
            if cachedVideos[cacheServer][video] != 0:
                improvement = rootServerLatency - latency
                if (improvement > 0):
                    latencies[cacheServer] = improvement

        if len(latencies) == 0:
            return 0
        else:
            return max(latencies.values())

"""
Reads the file outputed by the program from stdin
TESTED!!
"""
def readOutputFile():
    nCacheServers = int(raw_input())
    cachedVideos = {}

    for i in xrange(nCacheServers):
        line = map(int, raw_input().split())
        cacheServerId = line[0]
        videos = line[1:]

        cachedVideos[cacheServerId] = videos

    return cachedVideos

"""
Scores an instance generated by carlos local search algorithm
"""
def scoreLocalSearchInstance(cacheServers, requests, endpoints):

    scoreNumerator = 0
    scoreDenominator = 0

    for request in requests:
        video, endpoint, cardinality = request
        rootServerLatency, nCaches = endpoints[endpoint][0]
        requestGain = getLatencyGainForRequest(video, rootServerLatency, endpoints[endpoint][1], cacheServers)

        scoreNumerator += requestGain * cardinality
        scoreDenominator += cardinality

    return (scoreNumerator / scoreDenominator) * 1000

"""
Delivers the latency gain from using the best cache server instead of the root server
"""
def getLatencyGainForRequest(video, rootServerLatency, cacheConnections, cacheServers):

        latencies = {}

        for cacheServer in cacheConnections.keys():
            latency = cacheConnections[cacheServer]
            if cacheServers[cacheServer][video] != 0:
                improvement = rootServerLatency - latency
                if (improvement > 0):
                    latencies[cacheServer] = improvement

        if len(latencies) == 0:
            return 0
        else:
            return max(latencies.values())
