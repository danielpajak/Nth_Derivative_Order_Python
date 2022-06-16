from dataprovider import DataProvider
from pointscalculator import PointsCalculator
import matplotlib.pyplot as plt

data_provider = DataProvider()

input_data = data_provider.provide_data(200)

points_calculator = PointsCalculator()

window_size = 11

derivative_order = 2

output = points_calculator.calculate_points(input_data, window_size, derivative_order)

print("input data: %s" % input_data, end='\n\n')
print("output data: %s" % output)

output = [round(x, 2) for x in output]
fig, axs = plt.subplots(2)
axs[0].plot(input_data)
axs[0].set_title("Original Data")
axs[1].plot(output)
axs[1].set_title("Derivative %s" % derivative_order)
plt.tight_layout(pad=3.0)
plt.show()
