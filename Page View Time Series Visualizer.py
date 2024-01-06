import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Use the date column as index for DataFrame and parse data by date
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 'date', parse_dates = True)

# Filter out days when page views were in top or bottom 2.5th percentile
df = df[ (df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]

# Make line chart using Matplotlib
def draw_line_plot():

    # Set figure size and what to plot on each axis
    # Make plot; set title and labels for axes; save plot
    fig, ax = plt.subplots(figsize = (20,10))
    ax.plot(df.index.values, df['value'], color = 'red')
    ax.set(xlabel = 'Date', ylabel = 'Page Views', \
           title = 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig.savefig('line_plot.png')
    return fig


# Make bar chart using Seaborn
def draw_bar_plot():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Make copy of df
    df_bar = df.copy().reset_index()    

    # Get dates from df, split into months and years
    df_bar['year'] = [item.year for item in df_bar.date]
    df_bar['month'] = [item.strftime('%B') for item in df_bar.date]

    df_av = df_bar.groupby(['year', 'month'])['value'].mean().reset_index()

    # Use seaborn to construct bar plot and sort legend by order of months
    sns.set(style = 'whitegrid')
    fig, ax = plt.subplots(1, figsize=(10, 7))
    sns.barplot(x = 'year', y = 'value', hue = 'month', hue_order = months, data = df_av)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    fig.savefig('bar_plot.png')
    return fig


# Make box plot using Seaborn
def draw_box_plot():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    df_box = df.copy().reset_index()

    # Get dates from df, split into months and years
    df_box['year'] = [item.year for item in df_box.date]
    df_box['month'] = [item.strftime('%b') for item in df_box.date]
    df_box = df_box.reset_index()          

    # Use Matplotlib to set size of subplots
    sns.set(style = 'whitegrid') # Plot has 1 row and 2 columns
    fig, axes = plt.subplots(1,2, figsize = (20,7))

    # Use Seaborn to construct adjacent yearly and monthly box plots
    sns.boxplot(x = 'year', y = 'value', data = df_box, ax = axes[0])
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')

    sns.boxplot(x = 'month', y = 'value', data = df_box, order = months, ax = axes[1])
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    fig.savefig('box_plot.png')
    return fig
