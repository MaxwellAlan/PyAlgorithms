# 《图解算法》

#1.2 二分查找
from collections import deque


def binary_search(testList,item):
    low = 0
    high = len(testList)-1

    while low <= high :
        mid=(low+high)//2
        guess=testList[mid]
        if guess == item:
            return mid
        if guess > item:
            high=mid-1
        else:
            low=mid+1
    return None

#2.3 选择排序
def selectionSort(arr):
    newArr=[]
    while len(arr)!=0:
        smallest=findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

def findSmallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i] <smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index

#4.2 快速排序
def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        less = [i for i in arr[1:] if i <=pivot]
        greater=[i for i in arr[1:] if i>pivot]
    return quicksort(less)+[pivot]+quicksort(greater)

#6.3 广度优先搜索
graph={}
graph["you"]=['alice','bob','claire']
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] == 'm'

def bfsearch(name):
    search_queue = deque()
    search_queue+=graph[name]
    searched=[]
    while search_queue:
        person=search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person+" is a seller")
                return True
            else:
                search_queue+=graph[person]
                searched.append(person)
    return False

#7 Dijkstra's Algorithm
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# the costs table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# the parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node.
    for node in costs:
        cost = costs[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if cost < lowest_cost and node not in processed:
            # ... set it as the new lowest-cost node.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Find the lowest-cost node that you haven't processed yet.
node = find_lowest_cost_node(costs)
# If you've processed all the nodes, this while loop is done.
while node is not None:
    cost = costs[node]
    # Go through all the neighbors of this node.
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # If it's cheaper to get to this neighbor by going through this node...
        if costs[n] > new_cost:
            # ... update the cost for this node.
            costs[n] = new_cost
            # This node becomes the new parent for this neighbor.
            parents[n] = node
    # Mark the node as processed.
    processed.append(node)
    # Find the next node to process, and loop.
    node = find_lowest_cost_node(costs)


# 贪心算法
# You pass an array in, and it gets converted to a set.
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:
  best_station = None
  states_covered = set()
  for station, states in stations.items():
    covered = states_needed & states
    if len(covered) > len(states_covered):
      best_station = station
      states_covered = covered

  states_needed -= states_covered
  final_stations.add(best_station)

print(final_stations)




if __name__ == '__main__':
    test_list=[1,3,5,7,9,10,20]
    print(binary_search(test_list,10))

    print(selectionSort([5,3,2,6,10,2,3]))

    print(quicksort([5,3,2,6,10,2,3]))

    bfsearch("you")