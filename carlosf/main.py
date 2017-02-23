from random import randint
import scoring

V, E, R, C, X = map(int, raw_input().split())

print(V, E, R, C, X)

videos = map(int, raw_input().split())

endpoints = []
for i in xrange(E):
    endpoints.append([map(int,raw_input().split())])
    endpoint = []
    for j in xrange(endpoints[-1][0][1]):
        endpoint.append(map(int,raw_input().split()))
    endpoints[-1].append(dict(endpoint))

requests = []
for i in xrange(R):
    requests.append(map(int,raw_input().split()))

print(videos)
print()
print(endpoints)
print()
print(requests)

empty_solution = [[0]*V for i in xrange(C)]

def free_cache(server):
    return X - sum([videos[i] if server[i] == 1 else 0 for i in xrange(V)])

def perm_cache(server):
    r = randint(0, V-1)
    server[r] ^= 1
    return server

def swap_cache(server):
    r0 = randint(0, V-1)
    r1 = randint(1, V-1)
    r1 = (r0 + r1) % V
    server[r0], server[r1] = server[r1], server[r0] 
    return server

def random_solution():
    solution = empty_solution[:]
    for i in solution:
        tmpi = perm_cache(i)
        free = free_cache(tmpi)
        if free >= 0:
            i = tmpi
    return solution

def swap_server(server_list):
    r0 = randint(0, C-1)
    r1 = randint(1, C-1)
    r1 = (r0 + r1) % C
    server_list[r0], server_list[r1] = server_list[r1], server_list[r0]
    return server_list

sol = random_solution()
print(scoring.scoreLocalSearchInstance(sol, requests, endpoints))

sol = swap_server(sol)

print(sol)
