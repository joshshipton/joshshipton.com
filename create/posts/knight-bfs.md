ID="27570"
TITLE="Min Knight Moves Bfs"
LINK="knight-bfs"
IS_DRAFT=F
IS_POPULAR=F
----------
Lately I've been doing a lot of dsa in preparation for technical interviews. My favorite algorithm and solution at the moment is using [bfs](https://en.wikipedia.org/wiki/Breadth-first_search) (breadth first search) to find the optimal amount of steps to get from point A to point B following a specific rule or sequence. Examples of good problems where this solution is applicable are the [coin change problem](https://leetcode.com/problems/coin-change/) and the classic [Min Knights](https://leetcode.ca/all/1197.html) which I'll discuss more here. 

The beauty of the solution lies in its simplicity. It will never search through more steps than the optimal amount of steps since it will try every single possible solution up to n (where n is the amount of steps in the best case solution). I love the fact that even though the algorithm doesn't know the solution by trying every possible solution one step in a time it will always stumble upon the best solution. It will never waste time computing steps past the optimal solution (if an optimal solution exists).

Take the Min knight moves problem as an example. I'll attach some sample code and walk through the solution.

```python

# Import the deque data structure from the python standard library
from collections import deque

# for simplicty sake lets assume an infite sized board, lets start at 0,0 and try to get to our destination
def find_min_moves(dest_x,dest_y):

# define all the possible moves a knight can make
    possible_moves = [(2,1), (2,-1), (1,2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2,-1)]

    # initialize a set to keep track of squares visited
    visited = set()
    # initalize the queue with the starting point the third value is the amount of steps we are currently at  
    q = deque([(0,0,0)])

    # while there are elements in the queue we have positions to look at 
    while q:
    # get the x and y coordinates and the current amount of steps from the left of the queue
        x,y,steps = q.popleft()

    # if we have already seen x and y we don't need to look at it again
        if (x,y) in visited:
            continue
    # if we are at our destination we can return
        if x == dest_x and y == dest_y:
            return steps
    # add the current destination to visited
        visited.add((x,y))

    # try every possible move from where we currently are and append it to the queue to be looked at later
        for move_x, move_y in possible_moves:
            dx = move_x + x
            dy = move_y + y
            q.append((dx,dy,steps+1))
  
    # if we haven't found a solution we can return -1.
    # for an infinite sized board however there will always be a solution if the coordinates are valid
    return -1

# feel free to test the function
print(find_min_moves(5,3))

```

I also tried to build a way to visualize this, but my javascript is a bit rusty and it didn't work out too well. But [here](https://min-knights-bfs-visualization.vercel.app/) it is anyway.

