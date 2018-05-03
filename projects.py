import numpy as np
import matplotlib.pyplot as plt
import time
import random
import math

# ===== Vanila Gradient Descent =====
def plain_gradient_descent(iterations, step_size, initial_x):

    x       = initial_x
    x_seq   = [initial_x[0]]
    y_seq   = [initial_x[1]]
    z_seq   = [initial_x[0] * initial_x[1]]
    counter = 0

    while counter < iterations:
        counter = counter + 1   
        gradient = [-x[1], x[0]]
        x = [x[0] + step_size * gradient[0], x[1] + step_size * gradient[1]]

        x_seq.append(x[0])
        y_seq.append(x[1])
        z_seq.append(x[0] * x[1])

    draw_functions(x_seq, y_seq, z_seq)

# ===== Simple Dual Averages (SDA) =====
def simple_dual_averages(iterations, gamma, alpha, initial_x, initial_s):

    s_k         = initial_s
    x           = initial_x
    counter     = 0
    beta_seq    = [1, 1]

    x_seq = [initial_x[0]]
    y_seq = [initial_x[1]]
    z_seq = [initial_x[0] * initial_x[1]]

    while counter < iterations:
        gradient = [-x[1], x[0]]
        s_k      = [s_k[0] + gradient[0], s_k[1] + gradient[1]]

        if (counter < 2):
            beta = beta_seq[counter]
        else:
            beta = beta_seq[counter - 1] + 1.0 / beta_seq[counter - 1]
            beta_seq.append(beta)

        beta_p = gamma * beta
        new_u  = -s_k[0] * 1.0 / (alpha * beta_p)
        new_v  = -s_k[1] * 1.0 / ((1 - alpha) * beta_p)
        x = [new_u, new_v]

        x_seq.append(x[0])
        y_seq.append(x[1])
        z_seq.append(x[0] * x[1])

        counter  = counter + 1

    draw_functions(x_seq, y_seq, z_seq)

# ===== Draw the 3D functions =====
def draw_functions(x_seq, y_seq, z_seq):

    fig = plt.figure(figsize=(10,7))
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    # Make data.
    X = np.arange(-5, 5, 0.10)
    Y = np.arange(-5, 5, 0.10)
    X, Y = np.meshgrid(X, Y)
    Z = X * Y

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    xline = np.linspace(-2, 2, 1000)
    yline = np.linspace(-2, 2, 1000)
    zline = np.multiply(xline, yline)
    ax.plot3D(x_seq, y_seq, z_seq, 'red')

    surf = ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
    plt.show()