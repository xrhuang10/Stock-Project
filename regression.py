from main import training_data, regression_type
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Standardize the training data
training_data = training_data.reshape(-1, 1)
sc = StandardScaler()
pre_processed_training_data = sc.fit_transform(training_data)

# Creating X values (Index positions as dates)
X_train = np.arange(len(training_data)).reshape(-1, 1)  # [[0], [1], [2], ...]
y_train = training_data  # Actual values (High prices)

if regression_type == 'linear':
    # Train the Linear Regression model
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # Extend X values slightly beyond the last data point
    num_future_points = 3  # Number of future predictions
    X_extended = np.arange(len(training_data) + num_future_points).reshape(-1, 1)
    y_pred_extended = regressor.predict(X_extended)  # Predict for extended range

    # Plot the actual data points
    plt.scatter(X_train, y_train, color='red', label="Actual Data")

    # Plot the extended regression line
    plt.plot(X_extended, y_pred_extended, color='blue', linestyle='-', label="Extended Line of Best Fit")

    # Labels and title
    plt.title('Linear Regression: High vs Index (Standardized)')
    plt.xlabel('Index')
    plt.ylabel('Standardized High')
    plt.legend()
    plt.show()

elif regression_type == 'polynomial':
    # Use Polynomial Regression (degree 4 in this case)
    poly_reg = PolynomialFeatures(degree=4)
    X_poly = poly_reg.fit_transform(X_train)  # Apply polynomial features to X_train
    lin_reg_2 = LinearRegression()
    lin_reg_2.fit(X_poly, y_train)  # Fit the model using polynomial features of X_train and y_train

    # Predict using the polynomial model
    X_grid = np.arange(min(X_train), max(X_train), 0.1)
    X_grid = X_grid.reshape((len(X_grid), 1))  # Prepare the grid for smoother curve plotting

    # Plotting actual data points
    plt.scatter(X_train, y_train, color='red', label="Actual Data")

    # Plot the polynomial regression curve
    plt.plot(X_grid, lin_reg_2.predict(poly_reg.transform(X_grid)), color='blue', label="Polynomial Fit")

    # Labels and title
    plt.title('Polynomial Regression: High vs Index')
    plt.xlabel('Index')
    plt.ylabel('High')
    plt.legend()
    plt.show()