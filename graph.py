import numpy as np
import matplotlib.pyplot as plt

def barGraph(labels, title_label, y_label, title, values, width):
    fig, ax = plt.subplots()

    ax.bar(labels, values, width, label=title_label)

    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend()

    plt.show()


def histo2d(conn):
    sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind='scatter')

