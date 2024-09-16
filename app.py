import itertools
import random

# Traveling Salesman Problem (TSP)

'''
def traveling_salesman_problem(graph, start):
  """
  Solves the Traveling Salesman Problem using brute force.

  Args:
    graph: A 2D list representing the distances between cities.
           graph[i][j] is the distance between city i and city j.
    start: The starting city (index).

  Returns:
    A tuple containing:
      - The shortest distance found.
      - The corresponding route (list of city indices).
  """
  num_cities = len(graph)
  cities = range(num_cities)
  shortest_distance = float('inf')
  shortest_route = None

  for route in itertools.permutations(cities):
    if route[0] != start:
      continue  # Ensure the route starts from the specified city

    total_distance = 0
    current_city = start
    for next_city in route:
      total_distance += graph[current_city][next_city]
      current_city = next_city
    total_distance += graph[current_city][start]  # Return to the starting city

    if total_distance < shortest_distance:
      shortest_distance = total_distance
      shortest_route = route

  return shortest_distance, shortest_route
'''

def tsp_nearest_neighbor(graph, start):
    num_cities = len(graph)
    unvisited = set(range(num_cities))
    unvisited.remove(start)
    current_city = start
    total_distance = 0
    route = [start]

    while unvisited:
        nearest_city = min(unvisited, key=lambda city: graph[current_city][city])
        total_distance += graph[current_city][nearest_city]
        current_city = nearest_city
        unvisited.remove(current_city)
        route.append(current_city)

    total_distance += graph[current_city][start]  # Return to the starting city
    return total_distance, route

# generate a random graph
num_cities = 100
max_distance = 100
rand_graph = [[random.randint(1, max_distance) if i != j else 0 for j in range(num_cities)] for i in range(num_cities)]
print(rand_graph)
'''
# Example usage:
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
'''
start_city = 0

#shortest_distance, shortest_route = traveling_salesman_problem(rand_graph, start_city)
shortest_distance, shortest_route = tsp_nearest_neighbor(rand_graph, start_city)

print("Shortest distance:", shortest_distance)
print("Shortest route:", shortest_route)