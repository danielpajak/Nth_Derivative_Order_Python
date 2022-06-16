class DataProvider:

    @staticmethod
    def __fill_method(f, x):
        return f(x)

    # example fill method
    @staticmethod
    def calculate_cube(d):
        return float(d ** 3)

    def provide_data(self, size):

        d = -(size // 2)

        array = [self.__fill_method(self.calculate_cube, d) for d in range(d, size // 2)]

        return array
