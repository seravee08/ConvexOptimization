import os
import math
import time
import random
import numpy as np
import projects as func
import matplotlib.pyplot as plt

from pylab import *
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# ===== Vanila Gradient Descent =====
initial_x  = [2, 2]
iterations = 2000000
step_size  = 0.015
epsilon    = 1e-3

timer_start = time.time()
func.plain_gradient_descent(iterations, step_size, initial_x, epsilon)
print("Time taken for gradient descent: ", time.time() - timer_start)

# ===== Simple Dual Averages (SDA) =====
initial_s   = [0, 0]
initial_x   = [2, 2]
gamma       = 2.5
alpha       = 0.5
iterations  = 2000000
epsilon     = 1e-3

timer_start = time.time()
func.simple_dual_averages(iterations, gamma, alpha, initial_x, initial_s, epsilon)
print("Time taken for SDA: ", time.time() - timer_start)