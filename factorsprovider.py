import numpy as np


class FactorsProvider:

    @staticmethod
    def calculate_factors(window_size, derivative_order, points):

        matrix = np.zeros((window_size, window_size))

        for k, point in enumerate(points):
            for x in range(window_size):
                temp = point ** x
                matrix[x][k] = temp

        inverse_matrix = np.linalg.inv(matrix)

        factorial_matrix = np.zeros((window_size, 1))

        factorial_matrix[derivative_order][0] = np.math.factorial(derivative_order)

        output_matrix = inverse_matrix.dot(factorial_matrix)

        result = output_matrix.flatten()
        factors = result.tolist()

        print("factors: %s" % factors, end='\n\n')

        return factors
