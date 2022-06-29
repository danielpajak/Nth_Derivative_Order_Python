import numpy as np


class FactorsProvider:

    @staticmethod
    def calculate_factors(window_size, derivative_order, points):

        ndarray = np.zeros((window_size, window_size))
        matrix = np.matrix(ndarray)

        for k, point in enumerate(points):
            for x in range(window_size):
                matrix.itemset((x, k), point ** x)

        ndarray = np.zeros((window_size, 1))
        factorial_matrix = np.matrix(ndarray)

        factorial_matrix.itemset((derivative_order, 0), np.math.factorial(derivative_order))

        output_matrix = matrix.I @ factorial_matrix

        factors = output_matrix.A1

        print("factors: %s" % factors, end='\n\n')

        return factors
