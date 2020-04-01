def mat_mul(L):
    ''' Calculating minimum mumber of multiplications it needs for a given input of matrices
    L ==>(input) list of dimensions of the matrix
    (output) list of number of multiplication for each k
    '''


    min_cost = [0] * len
    # For matrix L[i], it has dimension of L[i-1] (row) * L[i] (column)
    
    ## loop going over all the indexes in the list
    for k in len(1, len(L)-1):

        opt_1 = mat_mul(L[1] * L[k])
        
        opt_2 = L[k+1] * L[-2]
        cost = L[0] * L[k+1] * L[-1] + opt_1 + opt_2
        if min_cost > cost:
            min_cost = cost

    return(cost)


def opt_function(i, j):
    L=[]
    for k in range(i, j):
        L.append(matmul_f(i, k, j))

    min(L)
    
    
