# -*- coding: utf-8 -*-
"""

@author: ARVIND
"""

from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot
 

def objective(x1,x2,x1^2,etc):
 return '''polynomial'''
 
# load the dataset
dataframe = read_csv(url, header=None)
data = dataframe.values

x, y = data[:, 4], data[:, -1]

popt, _ = curve_fit(objective, x, y)

a, b = popt //coefficients
'''
print('y = %.5f * x + %.5f' % (a, b))
# plot input vs output
pyplot.scatter(x, y)
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(x), 1)
# calculate the output for the range
y_line = objective(x_line, a, b)
# create a line plot for the mapping function
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.show()
'''