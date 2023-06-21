
"""


@author: ARVIND
"""

from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

X = //input
Y = // output


poly = PolynomialFeatures(degree=2)
X_ = poly.fit_transform(X)
predict_ = poly.fit_transform(predict)

clf = linear_model.LinearRegression()
clf.fit(X_, vector)
print clf.predict(predict_)