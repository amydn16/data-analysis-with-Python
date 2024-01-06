import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Use Matplotlib to create scatter plot and linear regression from data
def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    # Get data for year and CSIRO adjusted sea level
    x1 = df['Year'].tolist() # Make x1 into a list
    y1 = df['CSIRO Adjusted Sea Level'].tolist() # Repeat with y1

    # Form scatter plot for year and CSIRO adjusted sea level
    fig, ax = plt.subplots()
    ax.scatter(x1, y1, color = 'b', linewidths = 0.5,\
               label = 'Original CSIRO adjusted data')

    # Use SciPy to get line of best fit for whole dataset
    [slope, yintercept, rval, pval, stderr] = stats.linregress(x1,y1)

    # Extend timeline to the year 2050 
    x2 = x1 + [item for item in range(x1[-1] + 1, 2051)]
    x2 = np.array(x2) # Convert list into array

    # Plot line of best fit, which extends to the year 2050
    ax.plot(x2, yintercept + slope*x2, color = 'r', linewidth = 2,\
            label = 'Line of best fit for CSIRO data')

    # Get line of best fit for entire NOAA data
    df_noaa = df.dropna(axis = 0, how = 'any') # Drop rows without NOAA data
    x3 = df_noaa['Year'].tolist()
    y3 = df_noaa['NOAA Adjusted Sea Level'].tolist()
    [slope, yintercept, rval, pval, stderr] = stats.linregress(x3,y3)

    # Plot line of best fit for NOAA data, which extends to the year 2050
    x3 = x3 + [item for item in range(x3[-1] + 1, 2051)]
    x3 = np.array(x3)
    ax.plot(x3, yintercept + slope*x3, color = 'g', linewidth = 2,\
            label = 'Line of best fit for NOAA data')

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in sea level')
    ax.legend()
    fig.savefig('Scatter_plot.png')

    figfinal = fig.fig
    return figfinal