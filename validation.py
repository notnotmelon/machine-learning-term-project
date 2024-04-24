import sklearn

csv_path = 'filtered_data.csv'

import pandas as pd

data = pd.read_csv(csv_path)

X = data.drop('IncidentSize', axis=1)
X['bias'] = 1
y = data['IncidentSize']

from sklearn.linear_model import SGDRegressor

model = SGDRegressor(max_iter=5000, alpha=0, penalty=None, learning_rate='constant', eta0=0.00003)
model.fit(X, y)

print(f'Score: {model.score(X, y)}')
print(f'Final weights: {model.coef_}')
our_weights = [-9.67e-02, -5.05e-03, 2.77e-02, -5.03e-02, -2.56e-01, 5.46e-04, 1.49e-03, -4.19e-05]
print(f'Comparision to our weights: {our_weights}')

error = sklearn.metrics.mean_squared_error(y, model.predict(X))
print(f'Mean squared error of scikit: {error}')

our_rmse = 0
for i in range(len(y)):
    our_rmse += (y[i] - sum([X.iloc[i][j] * our_weights[j] for j in range(len(our_weights))])) ** 2
print(f'Mean squared error of our weights: {our_rmse}')

print(f'Error delta between our weights and scikit: {our_rmse - error}')