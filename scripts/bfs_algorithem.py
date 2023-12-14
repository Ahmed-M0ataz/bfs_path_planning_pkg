#!/usr/bin/env python


import numpy as np
import time


# frist we need to define the map
# S is the start point
# E is the end point
# . is the free space
# # is the obstacle
R, C = 5, 5
m = [['S', '.', '', '#', '.'],
     ['.', '#', '.', '.', 'E'],
     ['.', '#', '.', '#', '.'],
     ['.', '.', '.', '.', '#'],
     ['#', '.', '#', '.', '.']]

sr, sc = 0, 0  # start row and column for robot starting position

 # end row and column for robot ending position but we dont know the location
e = (0, 0) 
# queue is used to store the next position to be explored by the robot
# rq, cq are the row and column queue that i want to explore
# i will use the first in first out method
# i will use the append and pop function
# becouse the map is 5x5 i will use a list of 5 elements

rq, cq = [], []  # row queue and column queue


# variable to track number of steps taken by the robot
# move_count is acual the number of steps taken by the robot
move_count = 0
# nodes_left_in_layer is the number of nodes in the current layer
# how many nodes need to de queued before the next layer is started
nodes_left_in_layer = 1

#nodes_in_next_layer how many nodes need to be explored in the next layer
nodes_in_next_layer = 0

reached_end = False  # flag variable to indicate if the end point 'E' is reached


# keep track of visited cells
# we dont want to explore the same cell twice
# visited is same size as m
visited = np.zeros((5, 5))

prev = np.zeros((5, 5), dtype=tuple)
# define the four possible movements of the robot
# this is depend on what i wand 
# i can make explore up down left right 
# or left right up down
# or any other combination
# i can even add diagonal movements

# but for now i will use the four basic movements up down right left

dr = [-1, 1, 0, 0]  # row movement
dc = [0, 0, 1, -1]  # column movement

def explore_neighbours(r, c):
    global nodes_in_next_layer, prev
    for i in range(4):
        # rr is the row of the next location to be explored
        # cc is the column of the next location to be explored
        rr = r + dr[i]
        cc = c + dc[i]
        # if rr or cc is out of the map we will ignore it and continue 
        if rr < 0 or cc < 0:
            continue
        if rr >= R or cc >= C:
            continue
        # if rr , cc is visited we will ignore it and continue
        if visited[rr][cc]:
            continue
        # if rr, cc is an obstacle we will ignore it and continue
        if m[rr][cc] == '#':
            continue
        # if not all above we will add rr, cc to the queue
        rq.append(rr)
        cq.append(cc)
        # make it as visited
        visited[rr][cc] = True
        
        # prev is used to track the path
        prev[rr][cc] = (r, c)
        nodes_in_next_layer += 1
    # print (f"matrix visited: \n{visited} \n")
    # print (f"matrix track path: \n{prev} \n")
    
    # print(f'next layer: \n row {rq} \n column {cq}')



    
def bfs_solve():
    global move_count, nodes_left_in_layer, nodes_in_next_layer, reached_end, e, prev
    # in frist we need to make start location as visited
    # and remove it from rq and cp queue
    # becouse we dont want to explore it again
    visited[sr][sc] = True
    # prev[sr][sc] = 'S'
    # add frist location to the queue
    # that we want to explore
    rq.append(sr)
    cq.append(sc)
    
    while len(rq) > 0:
        # r is the row and c is the column for first element in the queue
        # i made pop becouse i want to explore the first element in the queue
        # but i dont want to explore it again
        
        r = rq.pop(0)
        c = cq.pop(0)
        
        if m[r][c] == 'E':
            # now we know the location of the end point 
            e = (r, c)
            # prev[r][c] = 'E'
            reached_end = True
            break
        
        explore_neighbours(r, c)
        # nodes_left_in_layer is the number of nodes in the current layer
        # this use to track number of steps 
        nodes_left_in_layer -= 1
        
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1    
        
    if reached_end:
        
        return move_count
    return -1
     
def get_shortest_path(prev,s):
    global e
    path = []
    at = e
    while(at != 0.0):
        path.append(at)
        # print(at)
        at = prev[at[0]][at[1]]

    path.reverse()

    if path[0] == s:
        return path
    return []

bfs_solve()



shortest_path = get_shortest_path( prev,(sr, sc))
prev[sr][sc] = 'S'
prev[e[0]][e[1]] = 'E'
print (f"final visited: \n{visited} \n")
print (f"matrix  final track path: \n{prev} \n")
print("Shortest path indexing:", shortest_path)
