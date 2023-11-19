import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

# Importing the data. The data that is not selected below is commented out to preserve ocmputational time
noCol_data = sp.io.loadmat('./schlieren_data/fsss_afterNoColumns.mat')
# col_data = sp.io.loadmat('./schlieren_data/fsss_afterColumns.mat')
# firstWaves_data = sp.io.loadmat('./schlieren_data/fsss_firstWaves.mat')

# The selected data to study
data = noCol_data

# Generating a mesh-grid with the given x- and y-values
x = data['x']
y = data['y']
X,Y = np.meshgrid(y,x)

# Collecting the gradient data
gradX = data['gradX']
gradY = data['gradY']

# Titles used for the plotting gradient in x- and y-direction
title_x = 'Free surface gradient component in the x-direction.'
title_y = 'Free surface gradient component in the y-direction.'

# Creating the function to animate the gradient. 
def animate(grad, title):
  fig, ax = plt.subplots()

  for i in range(len(grad[0][0])):
    # Clearing the last timestep
    ax.clear()
    # Selecting the data for the timestep
    gt = grad[:,:,i]
    # The max and min contour values are found. Used for the color intensity.
    max_val = max(gt.flatten())
    min_val = min(gt.flatten())
    # Plotting the contour plot
    plt.contourf(X, Y, gt, 40, cmap='bwr')
    # Specifying the max and min values
    plt.clim(min_val, max_val)
    # Naming the axis
    plt.ylabel('x - axis')
    plt.xlabel('y - axis')
    # Adding the given title, as well as stating the timestep
    plt.title(f'Time = {i}. ' + title)
    # Controlling the speed of the animation
    plt.pause(0.01)

# Preforming the animation
animate(gradX, title_x)
