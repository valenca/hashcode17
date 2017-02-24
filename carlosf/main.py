from random import randint, seed, random
import scoring
from copy import deepcopy
import sys

V, E, R, C, X = map(int, raw_input().split())

# print(V, E, R, C, X)

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

# print(videos)
# print()
# print(endpoints)
# print()
# print(requests)

empty_solution = [[0]*V for i in xrange(C)]

def free_cache(server):
    return X - sum([videos[i]*server[i] for i in xrange(V)])

def perm_cache(server):
    r = randint(0, V-1)
    # server[r] ^= 1
    server[r] = 1
    return server

def swap_cache(server):
    r0 = randint(0, V-1)
    r1 = randint(1, V-1)
    r1 = (r0 + r1) % V
    server[r0], server[r1] = server[r1], server[r0] 
    return server

def swap_rnd_cache(server_list):
    r = randint(0, V-1)
    tmpi = perm_cache(server_list[i][:])
    if free_cache(tmpi) >= 0:
        server_list[i] = tmpi
    return server_list

def random_solution():
    solution = deepcopy(empty_solution)
    for j in xrange(10):
        for i in xrange(len(solution)):
            tmpi = perm_cache(solution[i][:])
            free = free_cache(tmpi)
            if free >= 0:
                solution[i] = tmpi
    return solution

def swap_server(server_list):
    r0 = randint(0, C-1)
    r1 = randint(1, C-1)
    r1 = (r0 + r1) % C
    server_list[r0], server_list[r1] = server_list[r1], server_list[r0]
    return server_list

getScore = scoring.scoreLocalSearchInstance

def local_search():
    sol = random_solution()
    score = getScore(sol, requests, endpoints)
    for i in xrange(10):
        sys.stderr.write(str(i)+"-"+str(score)+"\n")
        # tmp = swap_server(sol)
        # tmpScore = getScore(tmp, requests, endpoints)
        # if tmpScore > score:
        #     sol = deepcopy(tmp)
        #     score = tmpScore
        tmp = swap_rnd_cache(sol)
        tmpScore = getScore(tmp, requests, endpoints)
        if tmpScore > score:
            # sol = deepcopy(tmp)
            sol = tmp
            score = tmpScore
    return sol, score

def print_solution(sol):
    print(C)
    for i in xrange(C):
        print i,
        for j in xrange(len(sol[i])):
            if sol[i][j] == 1:
                print j,
        print
    

# seed(8)
def local_search2():
    #sol = random_solution()
    sol = [[0]*V for i in xrange(C)]
    freeC = [X]*C
    score = getScore(sol, requests, endpoints)
    flag = 1
    while(flag):
        flag = 0
        for i in xrange(C):
            # free = free_cache(sol[i])
            if freeC[i] <= 0:
                continue
            for j in xrange(V):
                if sol[i][j] == 0 and freeC[i] - videos[j] >= 0:
                    if random() > 0.4:
                        freeC[i] -= videos[j]
                        sol[i][j] = 1
                        tmpScore = getScore(sol, requests, endpoints)
                        if tmpScore <= score:
                            sol[i][j] = 0
                            freeC[i] += videos[j]
                        else:
                            flag = 1
                            score = tmpScore
                if freeC[i] - minVideo <= 0:
                    break
        # sys.stderr.write("-"+str(score)+"\n")
    
    for i in xrange(C):
        if freeC[i] <= 0:
            continue
        for j in xrange(V):
            if sol[i][j] == 0 and freeC[i] - videos[j] >= 0:
                freeC[i] -= videos[j]
                sol[i][j] = 1
                tmpScore = getScore(sol, requests, endpoints)
                if tmpScore < score:
                    sol[i][j] = 0
                    freeC[i] += videos[j]
                else:
                    score = tmpScore
            if freeC[i] - minVideo <= 0:
                break
        # sys.stderr.write("- "+str(score)+"\n")

    return sol, score

minVideo = min(videos)

scoreBest = 0
bestSol = []
for i in xrange(1000):
    solution, score = local_search2()
    if scoreBest < score:
        scoreBest = score
        bestSol = solution
    sys.stderr.write("-->"+str(i)+" "+str(score)+"\n")

print_solution(solution)

sys.stderr.write(str(scoreBest)+"\n")

