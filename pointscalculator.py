from indexesprovider import IndexesProvider
from factorsprovider import FactorsProvider
import numpy as np


class PointsCalculator:

    @staticmethod
    def calculate_points(points, window_size, derivative_order):

        index_provider = IndexesProvider()
        factors_provider = FactorsProvider()

        size = len(points)

        indexes = np.zeros((window_size, window_size))
        factors = np.zeros((window_size, window_size))

        index = window_size - 1
        for i in reversed(range(0, window_size)):
            indexes[index] = index_provider.list_provider(window_size, i)
            factors[index] = factors_provider.calculate_factors(window_size, derivative_order, indexes[index])
            index -= 1

        result = np.zeros(size)

        ind = 0

        for s in range(size):
            new_point_value = 0.0
            if s < window_size // 2:
                for i in range(window_size):
                    new_point_value += points[s + int(indexes[ind][i])] * factors[ind][i]
                ind += 1
            elif s + window_size // 2 > size - 1:
                ind += 1
                for i in range(window_size):
                    new_point_value += points[s + int(indexes[ind][i])] * factors[ind][i]
            else:
                for i in range(window_size):
                    new_point_value += points[s + int(indexes[window_size // 2][i])] * factors[window_size // 2][i]

            result[s] = new_point_value

        return result
