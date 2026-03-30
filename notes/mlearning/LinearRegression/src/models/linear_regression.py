import numpy as np
import matplotlib.pyplot as plt

class LinearRegressionScratch:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        self.loss_history = []  # To track learning
    
    def fit(self, X, y):
        """Train the model from scratch"""
        n_samples, n_features = X.shape
        
        # Initialize weights to zero (or random small numbers)
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Training loop - YOU write this!
        for iteration in range(self.n_iterations):
            # Step 1: Forward pass (make predictions)
            y_predicted = np.dot(X, self.weights) + self.bias
            
            # Step 2: Calculate LOSS (YOU define this!)
            loss = np.mean((y - y_predicted) ** 2)  # Mean Squared Error
            self.loss_history.append(loss)
            
            # Step 3: Calculate GRADIENTS (YOU calculate this!)
            # Gradient of loss with respect to weights
            dw = -2 * np.dot(X.T, (y - y_predicted)) / n_samples
            # Gradient of loss with respect to bias
            db = -2 * np.mean(y - y_predicted)
            
            # Step 4: Update weights (Gradient Descent - YOU write this!)
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            
            # Print progress every 100 iterations
            if iteration % 100 == 0:
                print(f"Iteration {iteration}: Loss = {loss:.4f}")
        
        return self
    
    def predict(self, X):
        """Make predictions"""
        return np.dot(X, self.weights) + self.bias