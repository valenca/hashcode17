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
	
### SOLUTION 1
# requests = {}
# for i in xrange(V):
#     requests[i] = {}

# for i in xrange(R):
#     v, e, r = map(int,raw_input().split())
#     requests[v][e] = r

# res = {}
# for i in xrange(V):
#     res[i] = []
#     for k in requests[i]:
#         res[i].append([k, requests[i][k]])
#     res[i].sort(key=lambda x: x[1], reverse=True)

# caches = []
# for c in xrange(C):
#     caches.append([])

# for v in requests:
#     for e in requests[v]:
#         for c in endpoints[e][1]:
#             caches[c].append([v, videos[v], requests[v][e], endpoints[e][0][0] - endpoints[e][1][c]])

# print(caches[0])

# for c in xrange(C):
#     caches[c].sort(key=lambda x: x[3]*x[2], reverse=True)

# print C
# for c in xrange(C):
#     s = 0
#     i = 0
#     v = []
#     print c,
#     while i < len(caches[c]):
#         if caches[c][i][0] in v or s+caches[c][i][1] > X:
#             i += 1
#             continue
#         print caches[c][i][0],
#         s += caches[c][i][1]
#         v.append(caches[c][i][0])
#         i += 1
#     print


### SOLUTION 2
# requests = {}
# for i in xrange(E):
#     requests[i] = {}

# for i in xrange(R):
#     v, e, r = map(int,raw_input().split())
#     requests[e][v] = r

# res = []
# for e in xrange(E):
#     res.append([])

# for e in requests:
#     for v in requests[e]:
#         for c in endpoints[e][1]:
#             res[e].append([v, videos[v], c, requests[e][v], endpoints[e][0][0] - endpoints[e][1][c]])
#     res[e].sort(key=lambda x: x[3]*x[4], reverse=True)



# print(res[0])

### SOLUTION 3
requests = []
for i in xrange(R):
    requests.append(map(int,raw_input().split()))

caches = []
for c in xrange(C):
    caches.append([0, []])

tmp = {}
for v in xrange(V):
    for c in range(C):
        tmp[(v,c)] = [0]

for r in requests:
    for c in endpoints[r[1]][1]:
        tmp[(r[0],c)][0] += endpoints[r[1]][0][0] - endpoints[r[1]][1][c]

tmp2 = tmp.items()
tmp2.sort(key=lambda x:x[1][0], reverse=True)
for i in xrange(len(tmp2)):
    if tmp2[i][1][0] == 0:
        tmp2 = tmp2[:i]
        break

f = lambda x:x[1][0]

i = 0
while True:
    # print(i)
    i+=1

    #tmp2 = tmp.items()
    tmp2.sort(key=f, reverse=True)
  
    cut = 0
    for t in tmp2:
        changed = False
        v1 = t[0][0]
        c1 = t[0][1]
        if v1 in caches[c1][1] or videos[v1]+caches[c1][0] > X:
            cut += 1
            continue
        caches[c1][1].append(v1)
        caches[c1][0] += videos[v1]

        for r in requests:
            if r[0] == v1:
                try:
                    lo = endpoints[r[1]][0][0]-endpoints[r[1]][1][c1]
                    if lo > 0:
                        for c in endpoints[r[1]][1]:
                            l = endpoints[r[1]][0][0]-endpoints[r[1]][1][c]
                            tmp[(r[0],c)][0] -= min(l,lo)
                except KeyError:
                    continue

        changed = True
        break

    tmp2 = tmp2[:cut]+tmp2[cut+1:]
    tmp2 = tmp2[1:]+[tmp2[0]]
    

    if not changed:
        break

# print(caches)

print C
for c in xrange(C):
    print c,
    for v in caches[c][1]:
        print v,
    print



