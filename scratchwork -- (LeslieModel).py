
#import numpy as np
from numpy import linalg as np
import numpy as num

def print_2Dmatrix(A):
    for x in A:
        print(*x, sep="  ")

if __name__ == '__main__':

    generations = 3
    age_groups = 4
    initial_population_vector = []
    #Leslie_matrix = [[0 for x in range(age_groups)] for y in range(age_groups)]
    Leslie_matrix= num.zeros([age_groups,age_groups])
    fecundity_vector = []
    prob_survival_vector = []


    prob_survival_vector = [0.9, 0.9, 0.8]
    fecundity_vector= [0.05, 0.5, 0.45,0.2]
    initial_population_vector = [10, 12,8,6]

    for i in range(0,age_groups):
        Leslie_matrix[0][i] = fecundity_vector[i]
        if i > 0:
            Leslie_matrix[i][i-1] = prob_survival_vector[i-1]
    print("Leslie Matrix:")
    print_2Dmatrix(Leslie_matrix)
    print()

    Population = num.zeros([generations + 1,age_groups])
    print_2Dmatrix(Population)
    print()

    First_iteration = []
    First_iteration = num.matmul(Leslie_matrix, initial_population_vector)

    for i in range(0,age_groups):
        Population[0][i] = initial_population_vector[i]

    print_2Dmatrix(Population)

    iteration = []

    for j in range(1, generations+1):
        iteration = num.matmul(np.matrix_power(Leslie_matrix,j),initial_population_vector)
        for k in range(0,age_groups):
            Population[j][k] = iteration[k]

    print()
    print_2Dmatrix(Population)

    #
    # Second_iteration = []
    # Second_iteration = matmul(Leslie_matrix, First_iteration)
    #
    # Third_iteration = []
    # Third_iteration = matmul(Leslie_matrix, Second_iteration)
    #
    # print(initial_population_vector)
    # print()
    # print(First_iteration)
    # print()
    # print(Second_iteration)
    # print()
    # print(Third_iteration)
