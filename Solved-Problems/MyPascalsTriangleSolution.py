# This prints the row at n
def pascals_triangle(n):
    fractions = []
    result = [1]
    tmp = 1
    for i in range(1, n+1):
        fractions.append(int(n-i+1)/(n-(n-i)))

    for i in range(0, n):
        tmp = tmp * fractions[i]
        result.append(int(tmp))
