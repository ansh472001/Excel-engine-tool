import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(df, chart_type, column1=None, column2=None):
    if chart_type == 'PIE':
        if column1 is not None:
            df[column1].value_counts().plot.pie(autopct='%1.1f%%')
            plt.title(f'Pie chart for {column1}')
            plt.ylabel('')
            plt.show()
        else:
            print("Error: column1 is required for pie chart.")
    elif chart_type == 'BAR':
        if column1 is not None:
            df[column1].value_counts().plot.bar()
            plt.title(f'Bar chart for {column1}')
            plt.ylabel('Counts')
            plt.show()
        else:
            print("Error: column1 is required for bar chart.")
    elif chart_type == 'HISTOGRAM':
        if column1 is not None:
            df[column1].plot.hist()
            plt.title(f'Histogram for {column1}')
            plt.xlabel(column1)
            plt.show()
        else:
            print("Error: column1 is required for histogram.")
    elif chart_type == 'LINE':
        if column1 is not None and column2 is not None:
            df.plot.line(x=column1, y=column2)
            plt.title(f'Line chart for {column1} vs {column2}')
            plt.xlabel(column1)
            plt.ylabel(column2)
            plt.show()
        else:
            print("Error: Both column1 and column2 are required for line chart.")
    elif chart_type == 'SCATTER':
        if column1 is not None and column2 is not None:
            df.plot.scatter(x=column1, y=column2)
            plt.title(f'Scatter plot for {column1} vs {column2}')
            plt.xlabel(column1)
            plt.ylabel(column2)
            plt.show()
        else:
            print("Error: Both column1 and column2 are required for scatter plot.")
    elif chart_type == 'HEATMAP':
        if column1 is not None and column2 is not None:
            pivot_table = df.pivot_table(index=column1, columns=column2, aggfunc='size', fill_value=0)
            sns.heatmap(pivot_table, annot=True, fmt="d")
            plt.title(f'Heatmap for {column1} vs {column2}')
            plt.xlabel(column2)
            plt.ylabel(column1)
            plt.show()
        else:
            print("Error: Both column1 and column2 are required for heatmap.")
    elif chart_type == 'BOX':
        if column1 is not None:
            sns.boxplot(x=df[column1])
            plt.title(f'Box plot for {column1}')
            plt.xlabel(column1)
            plt.show()
        else:
            print("Error: column1 is required for box plot.")
    else:
        print("Error: Invalid chart type.")
