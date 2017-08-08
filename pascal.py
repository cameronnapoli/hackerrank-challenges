# Generate a list of lists containing pascals triangle

# generate a pascals triangle of size n
def pascal(p):
    soln = []
    for i in range(1,p+1):
        if i == 1:
            soln.append([1])
        else:
            next = []
            prev = [0] + soln[-1] + [0]
            for i in range(len(prev)-1):
                next.append(prev[i] + prev[i+1])
            soln.append(next)
    return soln

assert pascal(3) == [[1], [1, 1], [1, 2, 1]]
