V,E,R,C,X = map(int,raw_input().split())

# print V,E,R,C,X

videos = list(map(int,raw_input().split()))

# print videos

endpoints = []
for i in xrange(E):
    endpoints.append([list(map(int,raw_input().split()))])
    endpoint = []
    for j in xrange(endpoints[-1][0][1]):
        endpoint.append(list(map(int,raw_input().split())))
    endpoints[-1].append(dict(endpoint))
	
requests = {}
for i in xrange(V):
    requests[i] = {}

for i in xrange(R):
    v, e, r = map(int,raw_input().split())
    requests[v][e] = r

res = {}
for i in xrange(V):
    res[i] = []
    for k in requests[i]:
        res[i].append([k, requests[i][k]])
    res[i].sort(key=lambda x: x[1], reverse=True)

caches = []
for c in xrange(C):
    caches.append([])


for v in requests:
    for e in requests[v]:
        for c in endpoints[e][1]:
            caches[c].append([v, videos[v], requests[v][e], endpoints[e][0][0] - endpoints[e][1][c]])

for c in xrange(C):
    caches[c].sort(key=lambda x: x[3]*x[2], reverse=True)

print C
for c in xrange(C):
    s = 0
    i = 0
    v = []
    print c,
    while i < len(caches[c]):
        if caches[c][i][0] in v or s+caches[c][i][1] > X:
            i += 1
            continue
        print caches[c][i][0],
        s += caches[c][i][1]
        v.append(caches[c][i][0])
        i += 1
    print


