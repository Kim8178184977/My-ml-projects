import matplotlib.pyplot as plt
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error
import numpy as np

diabetes = datasets.load_diabetes()


#dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])

dibeties_x = diabetes.data

dibeties_x_test = dibeties_x[:-30]
dibeties_x_train = dibeties_x[-30:]

dibeties_y_test = diabetes.target[:-30]
dibeties_y_train = diabetes.target[-30:]

model = linear_model.LinearRegression()

model.fit(dibeties_x_train,dibeties_y_train)

model_y_pridiction = model.predict(dibeties_x_test)

plt.scatter(dibeties_x_test,dibeties_y_test)

plt.plot(dibeties_x_test,model_y_pridiction)

plt.show()

print(mean_squared_error(dibeties_y_test,model_y_pridiction))

print(model.coef_)
print(model.intercept_)