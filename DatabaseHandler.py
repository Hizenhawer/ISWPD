from enum import Enum


class Color(Enum):
    RED = 1
    BLUE = 2
    BLACK = 3
    GREEN = 4


class Route:
    def __init__(self, label, start_point, end_point, color, elevation, descent, length, time):
        self.label = label
        self.start_point = start_point
        self.end_point = end_point
        self.color = color,
        self.elevation = elevation
        self.descent = descent,
        self.length = length,
        self.time = time


data = [
    Route("Schronisko PTTK Na Hali Miziowej ↔ Las Suchowarski", (49.540217, 19.318807), (49.534830, 19.343204), Color.RED, 40.0, 168.0, 2.3, (40, 50)),
    Route("Odbočka Zimnej cesty na Štrbské Pleso ↔ Trigan", (49.151894, 20.076688), (49.136647, 20.067202), Color.GREEN, 115.0, 99.0, 2.0, (40, 50)),
        ]
