import numpy as np
import matplotlib.pyplot as plt

def point_on_hilbert_curve(n, p):
    """Generate (x, y) position for point p on a Hilbert curve of order n."""
    if n == 0:
        return (0, 0)
    
    x, y = point_on_hilbert_curve(n-1, p//4)
    if p % 4 == 0:  # bottom-left quadrant
        return (y, x)
    elif p % 4 == 1:  # bottom-right quadrant
        return (x, y + 2**(n-1))
    elif p % 4 == 2:  # top-right quadrant
        return (x + 2**(n-1), y + 2**(n-1))
    elif p % 4 == 3:  # top-left quadrant
        return (2**n - y - 1, 2**(n-1) - x - 1)

def utilization_to_color(utilization):
    """Map utilization value to a color."""
    if utilization == 0:
        return (0, 0, 0)  # black for no utilization
    else:
        # Linear interpolation between blue and red
        r = utilization / 256
        return (r, 0, 1-r)

def generate_hilbert_image(utilizations, n):
    """Generate an image of the Hilbert curve with given utilizations."""
    size = 2**n
    image = np.zeros((size, size, 3))
    
    for p, utilization in enumerate(utilizations):
        x, y = point_on_hilbert_curve(n, p)
        image[y, x] = utilization_to_color(utilization)
    
    return image

# Testing with a random utilization for a 4096x4096 image (n=12 for the Hilbert curve)
n = 12
utilizations = np.random.randint(0, 257, size=2**(2*n))  # 0 to 256 inclusive
image = generate_hilbert_image(utilizations, n)

# Plotting
plt.figure(figsize=(10, 10))
plt.imshow(image)
plt.axis('off')
plt.show()
