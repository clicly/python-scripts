import pandas
from matplotlib import pyplot as pyplot
from datetime import datetime

def display_graph(date_array, count_arr):
    """
    Creates a diagram with dates (x-axis) and wpm (y-axis).
    """
    pyplot.ion()
    pyplot.figure(1)
    pyplot.plot(date_array, count_arr)
    pyplot.gcf().autofmt_xdate()
    pyplot.show(block=True)

if __name__ == "__main__":
    with open('data.txt') as f:
        # Format in data.txt is e.g.: 31.10.2020	38 

        lines = f.readlines()
        x = [line.split()[0] for line in lines] # dates
        y = [line.split()[1] for line in lines] # word per minute

        date_array = [datetime.now().strptime(date, '%d.%m.%Y').date() for date in x]
        wpm_array = [int(wpm) for wpm in y]

        display_graph(date_array, wpm_array)