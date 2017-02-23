
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



