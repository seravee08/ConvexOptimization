import numpy as np
import projects as func
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import random
import math
import os
from mpl_toolkits.mplot3d.axes3d import Axes3D
from pylab import *

# ===== Vanila Gradient Descent =====
initial_x  = [2, 2]
iterations = 2000
step_size  = 0.015

func.plain_gradient_descent(iterations, step_size, initial_x)

# ===== Simple Dual Averages (SDA) =====
initial_s   = [0, 0]
initial_x   = [2, 2]
gamma       = 2.5
alpha       = 0.5
iterations  = 200

func.simple_dual_averages(iterations, gamma, alpha, initial_x, initial_s)