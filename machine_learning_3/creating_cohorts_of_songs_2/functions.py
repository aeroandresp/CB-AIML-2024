# Functions for main script

import matplotlib.pyplot as plt
import seaborn as sns

# box_plot_outlier will print box plots of
# numerical data (no objects) to detect
# outliers in data set
def box_plot_outlier(df, columns, show_plots):
    for col in columns:
        # print(col, 'is', df[col].dtypes)
        if df[col].dtypes != 'object':
            sns.boxplot(y=col, data=df)
            plt.title('Box Plot')
            plt.xlabel('All Data')
            plt.ylabel(col)
            if show_plots:
                plt.show()

def remove_outliers_iqr(df, columns, q1, q3, threshold):
    for col in columns:
        # print(col, 'is', df[col].dtypes)
        if df[col].dtypes != 'object':
            # calculate IQR for column Height
            Q1 = df[col].quantile(q1)
            Q3 = df[col].quantile(q3)
            IQR = Q3 - Q1

            # identify outliers
            outliers = df[(df[col] < Q1 - threshold * IQR) | (df[col] > Q3 + threshold * IQR)]
            # print('Outliers in', col, 'are as follows:', outliers)

            # drop rows containing outliers
            df = df.drop(outliers.index)
    return df
