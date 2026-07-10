

import numpy as np
import matplotlib.pyplot as plt

# Gaussian Kernel
def kernel(x, xi, tau):
    return np.exp(-np.sum((x - xi) ** 2) / (2 * tau ** 2))

# Locally Weighted Regression
def lwr(x, X, y, tau):

    W = np.diag([kernel(x, X[i], tau) for i in range(len(X))])

    theta = np.linalg.inv(X.T @ W @ X) @ X.T @ W @ y

    return x @ theta

# Generate dataset
np.random.seed(42)

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x) + 0.1 * np.random.randn(100)

# Add bias term
X = np.c_[np.ones(x.shape), x]

# Test data
x_test = np.linspace(0, 2 * np.pi, 200)
X_test = np.c_[np.ones(x_test.shape), x_test]

tau = 0.5

# Predictions
y_pred = np.array([lwr(i, X, y, tau) for i in X_test])

# Plot
plt.figure(figsize=(10, 6))

plt.scatter(x, y,
            color='red',
            label='Training Data',
            alpha=0.7)

plt.plot(x_test, y_pred,
         color='blue',
         label='LWR Fit (tau=0.5)',
         linewidth=2)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Locally Weighted Regression')

plt.legend()
plt.grid(alpha=0.3)

plt.show()