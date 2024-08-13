#include <complex.h>

int mandelbrot(double real, double imag, int max_iter) {
    double complex z = 0 + 0 * I;
    double complex c = real + imag * I;
    int n = 0;
    while (cabs(z) <= 2 && n < max_iter) {
        z = z * z + c;
        n++;
    }
    return n;
}
