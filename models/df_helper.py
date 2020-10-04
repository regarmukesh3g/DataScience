#!/usr/bin/env python

import matplotlib.pyplot as plt


class DfHelper:
    """
    Helper class for showing different plots for a dataframe.
    """
    def __init__(self, df):
        """
        Constructor.
        Args:
            df: The dataframe.
        """
        self.df = df

    def show_pie_chart(self, cat_var, head_lim=None):
        """
        Shows Pie chart for a variable
        Args:
            cat_var: Categorical variable for which pie chart to be displayed
            head_lim: head data if required
        """
        var_count = self.df[cat_var].value_counts()
        if head_lim:
            var_head = var_count.head(head_lim)
        else:
            var_head = var_count
        var_sum = var_head.sum()

        def convert_to_count(val):
            return int(val * var_sum / 100)

        plt.pie(var_head, labels=var_head.index.values, autopct=convert_to_count)

    def bar_on_two_num_var(self, cat_var, num_var1, num_var2, head_count=None, labels=None, width=None):
        """
        Shows value of 2 numeric variable means grouped by one categorical variable.
        Args:
            cat_var: Categorical variable on axis-x.
            num_var1: First numerical variable to be presented.
            num_var2: Second numeric variable to be presented.
            head_count: No. of head data to take based on categorical variable.
            labels: Array of title, x-label and y-label.
            width: width of bars in barplot.
        Returns:
            None
        """
        head_data = self.df[cat_var].value_counts()[:head_count]
        cat_data = self.df[self.df[cat_var].isin(head_data.index)]
        var_1_data = cat_data.groupby(cat_var)[num_var1].mean()
        var_1_sorted = var_1_data.sort_values()
        var_2_data = cat_data.groupby(cat_var)[num_var2].mean()
        plt.tick_params(rotation=90)

        if labels is not None:
            plt.title(labels[0])
            plt.xlabel(labels[1])
            plt.ylabel(labels[2])

        plt.bar(var_1_sorted.index, var_1_sorted, align='edge', width=width)
        plt.bar(var_2_data.index, var_2_data, align='edge', width= -width)
        plt.show()
