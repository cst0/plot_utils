#!/usr/bin/env python3
import math
from sys import path

path.append("..")
from utils.convert import numparse
import pygal
from pint import UnitRegistry


if __name__ == "__main__":
    ureg = UnitRegistry()
    length_datapoints = []
    with open("../data/distances.txt", "r") as f:
        for line in f.readlines():
            dist_in = ureg.Quantity(numparse(line), ureg.inches)
            length_datapoints.append(dist_in.to(ureg.meters))
    expected = ureg.Quantity(1, ureg.meters)
    err_m = [x.magnitude for x in length_datapoints]
    avg_m = sum(err_m) / len(err_m)
    offset_meter_data = [x - avg_m for x in err_m]
    boxplot = pygal.Box(legend_at_bottom=True)
    boxplot.add("linear goal error (meters, shifted to average)", offset_meter_data)
    boxplot.render_to_file("distances.svg")

    angular_datapoints = []
    with open("../data/rotation_distances.txt", "r") as f:
        for line in f.readlines():
            dist_in = numparse(line)
            # wheel distance from robot center is 20cm
            # so angle of rotation, given these measurements as distance between two wheel positions,
            # becomes 2 * arcsin((l/2)/20)
            angular_datapoints.append(
                ureg.Quantity(2 * math.asin((dist_in / 2) / 20), ureg.radians).to(
                    ureg.degrees
                )
            )
    expected = ureg.Quantity(20, ureg.degrees)
    err_d = [x.magnitude for x in angular_datapoints]
    avg_d = sum(err_d) / len(err_d)
    offset_angle_data = [x - avg_d for x in err_d]
    boxplot = pygal.Box(legend_at_bottom=True)
    boxplot.add("angular goal error (degrees, shifted to average)", offset_angle_data)
    boxplot.render_to_file("rotation_distances.svg")
