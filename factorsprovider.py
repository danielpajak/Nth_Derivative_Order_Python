import numpy as np


class FactorsProvider:

    @staticmethod
    def calculate_factors(window_size, derivative_order, points):

        matrix = np.zeros((window_size, window_size))

        for k, point in enumerate(points):
            for x in range(window_size):
                matrix[x][k] = point ** x

        factorial_matrix = np.zeros((window_size, 1))

        factorial_matrix[derivative_order][0] = np.math.factorial(derivative_order)

        output_matrix = np.linalg.solve(matrix, factorial_matrix)

        factors = output_matrix.flatten().tolist()

        print("factors: %s" % factors, end='\n\n')

        return factors
