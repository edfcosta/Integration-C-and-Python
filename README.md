# Integration-C-and-Python
# Python and C integration for working on programming language concepts at the Federal University of Pelotas

#Fractal Mandelbrot Application 

## Overview

This project's main objective is the integration of two programming languages: C and Python. The choice of 
these languages ​​aims to take advantage of their respective advantages: the versatility and ease of use of 
Python to build the user interface and to generate the Mandelbrot fractal image, offering a graphical 
visualization of the fractal. On the other hand, the implementation of fractal calculations is done in C, 
to perform calculations efficiently and quickly. The interaction between Python and C is done through the 
ctypes library, allowing Python to call C functions and use the results transparently.

## Project Structure
├── README.md # This file
├── Makefile # Instructions for building and running the project
├── mandelbrot.c # C source code for computing the Mandelbrot set
├── mandelbrot.so # Compiled shared library (generated after build) for Linux
├── main.py # Python script for the user interface and display


## Requirements

- **Python 3.x**
- **GCC (GNU Compiler Collection)** for compiling the C code
- **Matplotlib** for rendering the fractal
- **Numpy** for numerical operations

You can install the Python dependencies using:
- pip install matplotlib numpy

## For Build This Project

cd <path>/mandelbrot/
make 
make run
