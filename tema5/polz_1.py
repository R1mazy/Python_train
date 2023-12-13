def compute_m_dist(point_1, point_2=(0, 0)):
    x1, y1 = point_1
    x2, y2 = point_2
    return abs(x1 - x2) + abs(y1 - y2)

distance = compute_m_dist((2, 3))
print(distance)