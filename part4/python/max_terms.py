
def max_terms(N):
    results = []
    to_subtract = N
    i = 1
    if N == 1 or N == 2:
        results.append(N)
    else:
        while to_subtract - i >= i + 1:
            results.append(i)
            to_subtract -= i
            i += 1
        else:
            results.append(to_subtract)
    print(len(results))
    for elem in results:
        print(elem, end=' ')

max_terms(int(input()))