class IndexesProvider:

    @staticmethod
    def list_provider(window_size, edge_distance):

        indexes = [*range(-edge_distance, window_size - edge_distance)]

        print("indexes: %s" % indexes)

        return indexes
    