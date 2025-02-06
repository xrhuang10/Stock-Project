from main import training_data, regression_type
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
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
    X_extended = np.arange(len(training_data)*1.5).reshape(-1, 1)
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

    # Extend X values slightly beyond the last data point
    num_future_points  = 3
    X_extended = np.arange(0, len(training_data)*1.1, 0.1).reshape(-1, 1)
    X_poly_extended = poly_reg.transform(X_extended)
    y_pred_extended = lin_reg_2.predict(X_poly_extended)  # Predict for extended range

    

    # Plot the actual data points
    plt.scatter(X_train, y_train, color='red', label="Actual Data")

    # Plot the extended regression line
    plt.plot(X_extended, y_pred_extended, color='blue', linestyle = '-', label="Extended Polynomial Fit")

    # Labels and title
    plt.title('Linear Regression: High vs Index (Standardized)')
    plt.xlabel('Index')
    plt.ylabel('Standardized High')
    plt.legend()
    plt.show()


elif regression_type == 'svm':
    y_train = y_train.flatten()  # Convert y_train to 1D array
    svr = SVR(kernel='rbf')  # Radial basis function (RBF) kernel
    svr.fit(X_train, y_train)  # Train the model

    # Extend X values slightly beyond the last data point for future predictions
    num_future_points = 3  # Number of future predictions
    X_extended = np.arange(0, len(training_data)*1.1, 0.1).reshape(-1, 1)  # Finer steps for smoother curve

    # Predict using the SVM model
    y_pred_extended = svr.predict(X_extended)

    # Plotting actual data points
    plt.scatter(X_train, y_train, color='red', label="Actual Data")

    # Plot the extended SVM regression curve
    plt.plot(X_extended, y_pred_extended, color='blue', label="SVM Fit")

    # Labels and title
    plt.title('Support Vector Machine Regression: High vs Index')
    plt.xlabel('Index')
    plt.ylabel('High')
    plt.legend()
    plt.show()


elif regression_type == 'decision_tree':
    y_train = y_train.flatten()
    # Use Decision Tree Regression
    regressor = DecisionTreeRegressor(random_state=0, max_depth=3, min_samples_split=4, min_samples_leaf=2)
    regressor.fit(X_train, y_train)  # Train the model

    # Extend X values slightly beyond the last data point for future predictions
    num_future_points = 3  # Number of future predictions
    X_extended = np.arange(0, len(training_data)* 1.1, 0.1).reshape(-1, 1)  # Finer steps for smoother curve

    # Predict using the Decision Tree model
    y_pred_extended = regressor.predict(X_extended)

    # Plotting actual data points
    plt.scatter(X_train, y_train, color='red', label="Actual Data")

    # Plot the extended Decision Tree regression curve
    plt.plot(X_extended, y_pred_extended, color='blue', label="Decision Tree Fit")

    # Labels and title
    plt.title('Decision Tree Regression: High vs Index')
    plt.xlabel('Index')
    plt.ylabel('High')
    plt.legend()
    plt.show()


elif regression_type == 'random_forest':
    y_train = y_train.flatten()
    regressor = RandomForestRegressor(n_estimators=10, random_state=0, max_depth=30, min_samples_split=4, min_samples_leaf=2)
    regressor.fit(X_train, y_train)  # Train the model

    # Extend X values slightly beyond the last data point for future predictions
    num_future_points = 3  # Number of future predictions
    X_extended = np.arange(0, len(training_data) * 1.1, 0.1).reshape(-1, 1)  # Finer steps for smoother curve

    # Predict using the Random Forest model
    y_pred_extended = regressor.predict(X_extended)

    # Plotting actual data points
    plt.scatter(X_train, y_train, color='red', label="Actual Data")

    # Plot the extended Random Forest regression curve
    plt.plot(X_extended, y_pred_extended, color='blue', label="Random Forest Fit")

    # Labels and title
    plt.title('Random Forest Regression: High vs Index')
    plt.xlabel('Index')
    plt.ylabel('High')
    plt.legend()

    # Ensure the plot is displayed
    plt.show()

    
print('successful commit')