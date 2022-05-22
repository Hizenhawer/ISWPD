import dataclasses
from enum import Enum

from array import array


class Color(Enum):
    CZERWONY = 1
    NIEBIESKI = 2
    CZARNY = 3
    ZIELONY = 4


class Route:
    def __init__(self, color, elevation, descent, length, time):
        self.color = color
        self.elevation = elevation
        self.descent = descent
        self.length = length
        self.time = time


data = [
    Route(Color.CZERWONY, 40.0, 168.0, 2.3, (40, 50)),
    Route(Color.ZIELONY, 115.0, 99.0, 2.0, (40, 50)),
    Route(Color.CZERWONY, 55.0, 685.0, 3.5, (105,105)),
    Route(Color.CZERWONY, 11.0, 260.0, 0.9, (45, 35)),
    Route(Color.NIEBIESKI, 7, 127, 1.2, (25,25)),
    Route(Color.CZERWONY, 5, 154, 1.7, (20,20)),
    Route(Color.NIEBIESKI, 297, 566, 3.8, (95,115)),
    Route(Color.CZERWONY, 50, 54, 1.2, (25,25)),
    Route(Color.CZERWONY, 190, 2, 0.6, (20, 30)),
    Route(Color.CZERWONY, 1029, 113, 3.2, (200, 150)),
    Route(Color.ZIELONY, 3, 533, 2.3, (90, 70)),
    Route(Color.CZERWONY, 240, 318, 3.3, (100, 80)),
    Route(Color.CZERWONY, 55, 67, 1, (20,15)),
    Route(Color.CZERWONY, 51, 150, 1, (30, 25)),
    Route(Color.NIEBIESKI, 428, 41, 1.9, (55, 70)),
    Route(Color.NIEBIESKI, 35, 5, 0.4, (10, 10)),
    Route(Color.NIEBIESKI, 21, 7, 0.4, (10,10)),
    Route(Color.NIEBIESKI, 31, 1, 0.2, (5, 5)),
    Route(Color.NIEBIESKI, 8, 14, 0.6, (10, 10)),
    Route(Color.CZARNY, 362, 9, 1.2, (60, 45)),
    Route(Color.CZARNY, 99, 9, 1.3, (30, 25)),
    Route(Color.CZARNY, 64, 2, 0.6, (25, 20)),
    Route(Color.CZARNY, 35, 5, 0.4, (5,5)),
    Route(Color.CZARNY, 317, 9, 4.1, (70, 55))
        ]
training_data = map(lambda x: [x.elevation/1000, x.descent/1000, x.length/10, x.color.value/4], data)
training_results_there = map(lambda x: x.time[0], data)
training_results_return = map(lambda x: x.time[1], data)