def compute_trace(matrix):
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]
    return trace

trace = compute_trace([[1, 3.2], [3, -7.1]])
print(trace)