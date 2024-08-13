import ctypes
import numpy as np
import matplotlib.pyplot as plt

mandelbrot = ctypes.CDLL('./mandelbrot.so')
mandelbrot.mandelbrot.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int]
mandelbrot.mandelbrot.restype = ctypes.c_int



def generate_fractal(width, height, x_min, x_max, y_min, y_max, max_iter):
    real = np.linspace(x_min, x_max, width)
    imag = np.linspace(y_min, y_max, height)
    fractal = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            fractal[i, j] = mandelbrot.mandelbrot(real[j], imag[i], max_iter)

    return fractal

fractal_image = generate_fractal(800, 800, -2.0, 1.0, -1.5, 1.5, 1000)
plt.imshow(fractal_image, cmap='inferno', extent=(-2.0, 1.0, -1.5, 1.5))
plt.show()
