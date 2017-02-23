V,E,R,C,X = map(int,raw_input().split())

print V,E,R,C,X

videos = list(map(int,raw_input().split()))

endpoints = []
for i in xrange(E):
	endpoints.append([list(map(int,raw_input().split()))])
	endpoint = []
	for j in xrange(endpoints[-1][0][1]):
		endpoint.append(list(map(int,raw_input().split())))
	endpoints[-1].append(dict(endpoint))
	
requests = []
for i in xrange(R):
	requests.append(list(map(int,raw_input().split())))

print videos
print
print endpoints
print
print requests