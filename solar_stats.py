from solar_objects import Star, Planet
from math import sqrt
from solar_main import*
import numpy as np
import matplotlib.pyplot as plt
from solar_main import get_physical_time

def add_stats(object, star):
    global physical_time
    v = sqrt(object.Vx**2 + object.Vy**2)
    distance = sqrt((object.x - star.x)**2 + (object.y - star.y)**2)
    time = get_physical_time()
    stat = [v,distance,time]
    object.stats.append(stat)


def build_gr(stats_filename):
    with open('stats.txt', 'r') as out_file:
        for line in out_file:
            l = eval(line)
            time = []
            v = []
            r = []
            for i in range(len(l)):
                v.append(l[i][0])
                r.append(l[i][1])
                time.append(l[i][2])

        plt.scatter(v, r)
        plt.show()

