def split_data(X,Y, train_size):
  # ADD YOUR CODES
  # shuffle the data before splitting it
  train_index = int(float(train_size) * len(X))
  X, Y = shuffle(X,Y)

  
  X_train, X_test = X[:train_index], X[train_index:]
  y_train, y_test = Y[:train_index], Y[train_index:]
  return X_train, X_test, y_train , y_test

# Split (X,y) into X_train, X_test, y_train, y_test
X_train, X_test, y_train, y_test= split_data(X,y, 0.8)
