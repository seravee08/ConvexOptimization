# ConvexOptimization

This repository is created for the convex optimization projects. The repo contains a main file and a
python file with all functions. 

The programs are tested to run under:
Windows 10 64bit
Python 3.5 64bit

The program implements two functions:
- vanila function using gradient descent to solve minmax saddle point
- dual averaging method for saddle point

Time taken:
- gradient descent: 37.381s with precision 1e-3
- SDA: 68.378 with precision 1e-3

The SDA can perform much faster with a large gamma parameter. For showcase purpose,
a small gamma is used in the implementation.

Parameter settings:
- gradient descent
  - initial_x = [2, 2]
  - step_size = 0.015
- SDA
  - initial_s = [0, 0]
  - initial_x = [2, 2]
  - gamma = 2.5
  - alpha = 0.5
  
The simple dual averages method is taken from this paper:
https://poseidon01.ssrn.com/delivery.php?ID=665084071084094099085085092069091074057022040093022044117126112105125092093080076074107049044100122125039001073001121094112117038023052012006121093084068120120047006060021090074126085075027069106121069119027092022074117008105010091100072127022125&EXT=pdf
