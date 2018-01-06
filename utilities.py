import numpy as np
import matplotlib.pyplot as plt

def plot_mnist_result(X, y, prediction):
    # plot 25 random points in a grid
    idx = np.random.choice(np.arange(X.shape[0]), 25, replace=False)
    X_sample = X[idx]
    p_sample = prediction.flatten()[idx]
    y_sample = y.flatten()[idx]
    
    for i in range(25):
        pixels = X_sample[i].reshape((20, 20))
        color = 'green' if p_sample[i] == y_sample[i] else 'red'
        title = p_sample[i] if p_sample[i] != 10 else 0

        plt.subplot(5, 5, i + 1)
        plt.axis('off')
        plt.title(title, color=color)
        plt.subplots_adjust(wspace=2)
        plt.imshow(pixels.T, cmap='gray')

    plt.show()