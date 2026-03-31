import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])  # True: y = 2x + 1

# Initialize
w = 0.0
b = 0.0
learning_rate = 0.01
epochs = 1000

# Train
for epoch in range(epochs):
    # Forward
    y_pred = w * x + b
    
    # Loss
    loss = ((y - y_pred) ** 2).mean()
    
    # Gradients
    dw = (2/len(x)) * np.sum((y_pred - y) * x)
    db = (2/len(x)) * np.sum(y_pred - y)
    
    # Update
    w = w - learning_rate * dw
    b = b - learning_rate * db
    
    if epoch % 100 == 0:
        print(f"Epoch {epoch}: w={w:.4f}, b={b:.4f}, loss={loss:.4f}")

print(f"\nLearned: y = {w:.4f}x + {b:.4f}")
print(f"True:    y = 2x + 1")