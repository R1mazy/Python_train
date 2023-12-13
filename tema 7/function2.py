def manhattan_metric(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
def euclidean_metric(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def compute_nearest_neighbour(p1, points):
    result_manhattan = min(points, key=lambda p: manhattan_metric(p1, p))
    result_euclidean = min(points, key=lambda p: euclidean_metric(p1, p))
    return result_manhattan, result_euclidean

print(compute_nearest_neighbour((0, 0), ((1, 5), (3, 4))))