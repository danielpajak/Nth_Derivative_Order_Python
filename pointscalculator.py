from indexesprovider import IndexesProvider
from factorsprovider import FactorsProvider


class PointsCalculator:

    @staticmethod
    def calculate_points(points, window_size, derivative_order):

        index_provider = IndexesProvider()
        factors_provider = FactorsProvider()

        indexes = []
        factors = []
        iterator = iter(indexes)

        for i in reversed(range(0, window_size)):
            indexes.append(index_provider.list_provider(window_size, i))
            factors.append(factors_provider.calculate_factors(window_size, derivative_order, next(iterator)))

        indexes = list(reversed(indexes))
        factors = list(reversed(factors))

        result = []

        ind = 0

        size = len(points)

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

            result.append(new_point_value)

        return result
