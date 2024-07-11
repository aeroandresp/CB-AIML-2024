# Functions for main script

import matplotlib.pyplot as plt
import seaborn as sns

# box_plot_outlier will print box plots of
# numerical data (no objects) to detect
# outliers in data set
def box_plot_outlier(df, columns, show_plots):
    for col in columns:
        # print(col, 'is', df1[col].dtypes)
        if df[col].dtypes != 'object':
            sns.boxplot(y=col, data=df)
            plt.title('Box Plot')
            plt.xlabel('All Data')
            plt.ylabel(col)
            if show_plots:
                plt.show()
