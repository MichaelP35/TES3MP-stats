#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates


# Converts date into readable format.
def date2num(fmt, encoding='utf-8'):
    str_converter = dates.strpdate2num(fmt)

    def converter(b):
        s = b.decode(encoding)
        return str_converter(s)
    return converter


# Plots a graph based on data provided by "stats.csv".
# If the dates on "stats.csv" aren't in chronological order, the plot will "zig-zag".
def graph():
    date, servers, players = np.loadtxt('stats.csv',
                                        delimiter=',',
                                        unpack=True,
                                        converters={0: date2num('%Y-%m-%d %H:%M')})

    plt.plot_date(date, players, '-', label='Players')
    plt.plot_date(date, servers, '-', label='Servers')
    plt.ylabel('Count')
    plt.xlabel('Time')
    plt.title('TES3:MP - Player & Server Stats')
    plt.grid(True)
    plt.gcf().autofmt_xdate()
    plt.legend()
    plt.savefig('graph.png')


graph()
