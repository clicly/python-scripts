import pandas as pandas
from matplotlib import pyplot as pyplot


def get_single_graph(weight_array):
    pyplot.ion()
    pyplot.figure(0)
    dataframe = pandas.DataFrame({"x": range(0, weight_array.__len__()), "y": weight_array})
    pyplot.plot("x", "y", data=dataframe, marker=".", color="blue")
    pyplot.show()


def get_date_graph(date_array, weight_array, last):
    pyplot.ion()
    pyplot.figure(1)
    pyplot.plot(date_array[(date_array.__len__() - 1) - last:], weight_array[(weight_array.__len__() - 1) - last:])
    pyplot.gcf().autofmt_xdate()
    pyplot.show()
