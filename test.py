"""Test with CGS"""

# Instanciate the LinearRegression class 
model= LinearRegression(2)

# Train the model
model.fit(X_train, y_train)

# print the learned theta
print(model.theta)

# Make a prediction on X_test
y_pred_cgs = model.predict(X_test)

print(y_pred_cgs)

# Compute the MSE (Evaluate both, regression and classification)
MSE_cgs = mse(y_test, y_pred_cgs)

MSE_cgs

"""Test with Normal equation"""

# Instanciate the LinearRegression class 
model= LinearRegression(1)

# Train the model
model.fit(X_train, y_train)

# print the learned theta
print(model.theta)

# Make a prediction on X_test
y_pred_normal = model.predict(X_test)

print(y_pred_normal)

# Compute the MSE (Evaluate both, regression and classification)
MSE_normal = mse(y_test, y_pred_normal)

MSE_normal