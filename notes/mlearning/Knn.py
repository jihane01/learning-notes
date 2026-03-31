import numpy as np
from collections import Counter

class KNNFromScratch:
    def __init__(self, k=3):
        """
        k: number of neighbors to look at
        """
        self.k = k
        self.X_train = None
        self.y_train = None
    
    def fit(self, X, y):
        """
        KNN doesn't actually "learn" anything!
        It just stores the data.
        """
        self.X_train = X
        self.y_train = y
    
    def euclidean_distance(self, a, b):
        """Calculate distance between two points"""
        return np.sqrt(np.sum((a - b) ** 2))
    
    def predict(self, X_new):
        """
        Predict class for new points
        """
        predictions = []
        
        for point in X_new:
            # Step 1: Calculate distance to ALL training points
            distances = []
            for i, train_point in enumerate(self.X_train):
                dist = self.euclidean_distance(point, train_point)
                distances.append((dist, self.y_train[i]))
            
            # Step 2: Sort by distance (smallest first)
            distances.sort(key=lambda x: x[0])
            
            # Step 3: Take K nearest neighbors
            k_nearest = distances[:self.k]
            
            # Step 4: Get their labels
            labels = [label for (dist, label) in k_nearest]
            
            # Step 5: Majority vote
            most_common = Counter(labels).most_common(1)[0][0]
            predictions.append(most_common)
        
        return np.array(predictions)


# ============================================
# DEMONSTRATION
# ============================================

# Simple data: [Engine Size, Price]
X_train = np.array([
    [2.0, 25000],  # Sedan
    [2.5, 28000],  # Sedan
    [3.0, 35000],  # SUV
    [3.5, 38000],  # SUV
    [2.2, 26000],  # Sedan
    [3.2, 36000],  # SUV
])

y_train = np.array(['Sedan', 'Sedan', 'SUV', 'SUV', 'Sedan', 'SUV'])

# New car to predict
X_new = np.array([[2.8, 32000]])  # What is this?

# Create and train model
knn = KNNFromScratch(k=3)
knn.fit(X_train, y_train)

# Predict
prediction = knn.predict(X_new)
print(f"New car prediction: {prediction[0]}")