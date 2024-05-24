ID="16764"
TITLE="Disjoint Sets are really cool"
LINK="Disjoint-Set-Union-Find-Summary"
IS_DRAFT=F
IS_POPULAR=F
----------

Quick little post to consolidate knowledge and quickly talk about a new algorithm and data-structure that I think is really cool. 

Disjoint set's are set's in which the union of said set's results in the empty set. Or in more normal speak, if you take all the common element's from both sets and try to create a new set then this set will be empty (the set's have no common elements). 

We can use disjoint set's to represent things like social media networks or a network of trains. The train example is a good one to use to understand the idea. If each interconnected group of train stations is a set then these set's are going to be disjoint. It's easy to see that if we can somehow get to train station x, then we can also get to every train station from train station x. So if we can get to train station x we should add train station x (and all the stations connected to train station x) to the station that can get there (which we represent as a disjoint set). After we do this for every train station, each set is going to represent a network of interconnected trains. From this we can easily tell if you can or cannot get from one train station to another by seeing if two stations are in the same set. If they are, we can get from one to the other, if they aren't, **no bueno**. 

But now the switched on observer (not me), might exclaim. But Josh! This is going to take quadratic N^2 time! First you're going to take O(N) time looking at each element and then for each element you're going to have to look at every element to see what it's connected to! This is just a naive solution with extra steps!

If this is you stop reading now, you're only going to get dumber reading joshshipton.com, this is way below your pay grade. 

But that's a good point! One potential optimisation is to represent the set as a tree, and then look up the tree towards the root to see if the two elements have the same root, this is a good optimisation and would lead the find operation to take O(h) time where h is the time of the tree. But we can do even better. 

This is where the real magic of the Union-Find part of the solution comes in, when we union our set's together we can do something magical called *path compression* which represents the nodes/elements in the set as a flat graph in which we arbitrarily choose a representative to act as the "root" of the graph. Or in other words, pick an element. Make every element in the set point to that element.  

<img class="center" src="/images/disjoint-sets-are-cool/path-compression.png" alt="path-compression-visual"> 
  <b class="center"><figcaption>Path Compression Visual</figcaption></b>

This means that if we want to check if two elements are in the same set instead of having to go all the way back up to the root, we only have to go up one element and check that two sets have the same representative. This is really fast, we are talking [inverse Ackerman](https://www.geeksforgeeks.org/inverse-ackermann-function/) O(α(n) time. And means that the whole solution takes O(N+M * α(n)) time, where n is the amount of elements, and m is the amount of operations. This is for all practical applications constant time. (borat voice) *Very nice!*. 


<img src="/images/disjoint-sets-are-cool/union-find.png" alt="union-find"> 
  <b><figcaption class="center">Union Find Visual</figcaption></b>


#### Post Script

I found these links really helpful when trying to understand Union-Find.

[great video](https://l.messenger.com/l.php?u=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DayW5B2W9hfo%26ab_channel%3DPotatoCoders&h=AT2TcfdPWNsvmeONdqErMkpXt2Q99PWB9LNZH7KDfPE2PHJ41iFGXgNymPkv0hc9zCqQf-OEXsrSCX53T1OxhohmaomaoZe9C9iNanQOg8bVw0J8wzx93vnSV38ztLaUMvbIJgA)

[handy article](https://l.messenger.com/l.php?u=https%3A%2F%2Fwww.geeksforgeeks.org%2Fintroduction-to-disjoint-set-data-structure-or-union-find-algorithm%2F&h=AT2TcfdPWNsvmeONdqErMkpXt2Q99PWB9LNZH7KDfPE2PHJ41iFGXgNymPkv0hc9zCqQf-OEXsrSCX53T1OxhohmaomaoZe9C9iNanQOg8bVw0J8wzx93vnSV38ztLaUMvbIJg)(W3 schools goated)



### Here's some example code from one of my university labs


```python

class UnionFind:
    def __init__(self):
        # Initialize the parent and rank sets
        self.parent = {}
        self.rank = {}

    def find(self, city):
        # Recursively find the root of the city with path compression
        # if the self.parent[city] is not the city itself then we need to find the root of the city
        # and set the parent of the city to the root of the city
        # this is done to reduce the height of the tree and make the find operation faster taking inverse Ackermann function time
        if self.parent[city] != city:
            self.parent[city] = self.find(self.parent[city])
        return self.parent[city]

    def union(self, city1, city2):
        # Find the roots of the two cities
        root1 = self.find(city1)
        root2 = self.find(city2)

        # If they are in different sets (have different roots), then you merge them together
        # we can merge the two sets by attaching the root of the smaller tree to the root of the larger tree
        # this works because the root of the tree is the representative of the set
        # and the rank of the tree is the height of the tree
        if root1 != root2:
            # Attach the smaller tree under the root of the larger tree
            if self.rank[root1] > self.rank[root2]:
                # If the rank of the first city is greater than the rank of the second city, then we set the parent of the second city to the first city
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                # If the rank of the first city is less than the rank of the second city, then we set the parent of the first city to the second city
                self.parent[root1] = root2
            else:
                # If ranks are the same, arbitrarily choose one and increment its rank
                self.parent[root2] = root1
                self.rank[root1] += 1

    def add(self, city):
        # Add a city as a new set if it's not already present
        if city not in self.parent:
            # Set the parent of the city to itself and the rank of the city to 0
            self.parent[city] = city
            self.rank[city] = 0

def trains_planes(trains, planes):
    """
    Find what flights can be replaced with a rail journey.

    Initially, there are no rail connections between cities. As rail connections
    become available, we are interested in knowing what flights can be replaced
    by a rail journey, no matter how indirect the route. All rail connections
    are bidirectional.

    Target Complexity: O(N lg N) in the size of the input (trains + planes).

    Args:
        trains: A list of `(date, lcity, rcity)` tuples specifying that a rail
            connection between `lcity` and `rcity` became available on `date`.
        planes: A list of `(code, date, depart, arrive)` tuples specifying that
            there is a flight scheduled from `depart` to `arrive` on `date` with
            flight number `code`.

    Returns:
        A list of flights that could be replaced by a train journey.
    """
    # Initialize the UnionFind data structure
    uf = UnionFind()

    # Sort trains and planes by date
    trains.sort(key=lambda x: x[0])
    planes.sort(key=lambda x: x[1])

    # Initialize the train index and the result list
    train_index = 0
    result = []

    # Iterate through all the planes
    for code, date, depart, arrive in planes:
        # Process all trains that are available by this date
        while train_index < len(trains) and trains[train_index][0] <= date:
            # Add the cities to the UnionFind data structure
            _, lcity, rcity = trains[train_index]
            uf.add(lcity)
            uf.add(rcity)
            # Merge the cities into the same set
            uf.union(lcity, rcity)
            # Increment the train index
            train_index += 1

        # Check if this flight can be replaced
        # If the departure and arrival cities are in the same set, then the flight can be replaced
        uf.add(depart)
        uf.add(arrive)
        # Use the find operation to check if the departure and arrival cities are in the same set
        if uf.find(depart) == uf.find(arrive):
            # If they are in the same set, then the flight can be replaced
            # Add the flight to the result list
            result.append((code, date, depart, arrive))

    # Return the result list
    return result

```

