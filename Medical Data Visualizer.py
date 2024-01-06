import sys
sys.path.append('/usr/local/lib/python3.9/site-packages')

import pandas as pd
pd.options.mode.chained_assignment = None
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("medical_examination.csv")

# Compute list of BMI values, then add as new column to df
overweight = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = overweight

# Normalize 'overweight' data
df['overweight'].loc[df['overweight'] <= 25] = 0 # Good
df['overweight'].loc[df['overweight'] > 25] = 1 # Bad

# Normalize cholesterol and glucose data
df['cholesterol'].loc[df['cholesterol'] == 1] = 0 # Good
df['cholesterol'].loc[df['cholesterol'] > 1] = 1 # Bad
df['gluc'].loc[df['gluc'] == 1] = 0 # Good
df['gluc'].loc[df['gluc'] > 1] = 1 # Bad

def draw_cat_plot():

  df_cat = pd.melt(df, value_vars = ["active", "alco", "cholesterol", "gluc", "overweight", "smoke"], id_vars = "cardio")

  sns.set(style = "whitegrid")
  fig = sns.catplot(data = df_cat, kind = "count", x = "variable", y = None, hue = "value", col = "cardio")
  fig.set_ylabels('total')
  fig.savefig('catplot.png')
  
  figfinal = fig.fig
  return figfinal


def draw_heat_map():

    # Filter out incorrect data
    # Diastolic pressure cannot be higher than systolic
    # Height cannot be less than 2.5th percentile
    # Height cannot be more than 97.5th percentile
    # Weight cannot be less than 2.5th percentile
    # Weight cannot be more than 97.5th percentile
    df_filter = df[ (df['ap_lo'] <= df['ap_hi']) & \
                    (df['height'] >= df['height'].quantile(0.025)) & \
                    (df['height'] <= df['height'].quantile(0.975)) & \
                    (df['weight'] >= df['weight'].quantile(0.025)) & \
                    (df['weight'] <= df['weight'].quantile(0.975)) ]

    # Create correlation matrix
    df_filter_corr = df_filter.corr()

    # Create mask to mask upper triangle portion of df_filter_corr
    mask = np.triu(np.ones_like(df_filter_corr, dtype = np.bool))

    # Use seaborn to construct heatmap
    sns.axes_style("white")
    fig, ax = plt.subplots(figsize = (9,7))
    ax = sns.heatmap(df_filter_corr, mask = mask,\
                     annot = True, fmt = '.1f',\
                     vmin = -0.2, square = True)
    fig.savefig('heatmap.png')
    return fig
