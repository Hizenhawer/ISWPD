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
    Route("Chata pod Rysmi ↔ Nad Žabím potokom", (49.174566, 20.087209), (49.163224, 20.070969), Color.RED, 55.0, 685.0, 3.5, (105,105)),
    Route("Chata pod Rysmi ↔ Rysy", (49.174566, 20.087209), (49.179432, 20.088132), Color.RED, 11.0, 260.0, 0.9, (45, 35)),
    Route("Nad Žabím potokom ↔ Rázcestie nad Popradským plesom", (49.163224, 20.070969), (49.154219, 20.077634), Color.BLUE, 7, 127, 1.2, (25,25)),
    Route("Trigan ↔ Štrbské Pleso, rázcestie pred Heliosom", (49.136647, 20.067202), (49.118546, 20.062473), Color.RED, 5, 154, 1.7, (20,20)),
    Route("Schronisko PTTK w Dolinie Pięciu Stawów Polskich ↔ Odejście na Kępę", (49.213583, 20.048490), (49.203817, 20.071030), Color.BLUE, 297, 566, 3.8, (95,115)),
    Route("Morskie Oko ↔ Morskie Oko, pod Czarnym Stawem", (49.201182, 20.070832), (49.193521, 20.070379), Color.RED, 50, 54, 1.2, (25,25)),
    Route("Morskie Oko, pod Czarnym Stawem ↔ Czarny Staw Pod Rysami", (49.193521, 20.070379), (49.190374, 20.073700), Color.RED, 190, 2, 0.6, (20, 30)),
    Route("Czarny Staw Pod Rysami ↔ Rysy", (49.190374, 20.073700), (49.179432, 20.088132), Color.RED, 1029, 113, 3.2, (200, 150)),
    Route("Przełęcz pod Kopą Kondracką ↔ Schronisko PTTK na Hali Kondratowej", (49.234471, 19.938800), (49.249647, 19.951727), Color.GREEN, 3, 533, 2.3, (90, 70)),
    Route("Kasprowy Wierch, odejście szlaku czerwonego ↔ Przełęcz pod Kopą Kondracką", (49.231336, 19.980478), (49.234329, 19.938812), Color.RED, 240, 318, 3.3, (100, 80)),
    Route("Liliowe ↔ Sucha Przełęcz", (49.229677, 19.985526), (49.225189, 19.992538), Color.RED, 55, 67, 1, (20,15)),
    Route("Świnicka Przełęcz ↔ Liliowe", (49.220934, 20.003782), (49.225189, 19.992538), Color.RED, 51, 150, 1, (30, 25)),
    Route("Tablica S. Bronikowskiego ↔ Zawrat", (49.209922, 20.026695), (49.219088, 20.016392), Color.BLUE, 428, 41, 1.9, (55, 70)),
    Route("Dolina Pięciu Stawów Polskich, pod Kozim Wierchem ↔ Dolina Pięciu Stawów Polskich, Niżnie Solnisko", (49.210598, 20.035276), (49.209721, 20.029995), Color.BLUE, 35, 5, 0.4, (10, 10)),
    Route("Dolina Pięciu Stawów Polskich, Zagon Niżni ↔ Dolina Pięciu Stawów Polskich, pod Kozim Wierchem", (49.212627, 20.039901), (49.210598, 20.035276), Color.BLUE, 21, 7, 0.4, (10,10)),
    Route("Siklawa ↔ Dolina Pięciu Stawów Polskich, Zagon Niżni", (49.212372, 20.042302), (49.212627, 20.039901), Color.BLUE, 31, 1, 0.2, (5, 5)),
    Route("Schronisko PTTK w Dolinie Pięciu Stawów Polskich ↔ Siklawa", (49.213583, 20.048490), (49.212372, 20.042302), Color.BLUE, 8, 14, 0.6, (10, 10)),
    Route("Zielony Staw Gąsienicowy ↔ Świnicka Przełęcz", (49.227815, 20.002395), (49.220934, 20.003782), Color.BLACK, 362, 9, 1.2, (60, 45)),
    Route("Kolejka krzesełkowa Gąsienicowa, stacja dolna ↔ Zielony Staw Gąsienicowy", (49.237123, 19.996603), (49.227815, 20.002395), Color.BLACK, 99, 9, 1.3, (30, 25)),
    Route("Hala Gąsienicowa ↔ Kolejka krzesełkowa Gąsienicowa, stacja dolna", (49.241466, 20.001760), (49.237123, 19.996603), Color.BLACK, 64, 2, 0.6, (25, 20)),
    Route("Stacja IMGW ↔ Hala Gąsienicowa", (49.244041, 20.006104), (49.241466, 20.001760), Color.BLACK, 35, 5, 0.4, (5,5)),
    Route("Psia Trawka ↔ Murowaniec, odejście szlaku czarnego", (49.269761, 20.036569), (49.243763, 20.008351), Color.BLACK, 317, 9, 4.1, (70, 55))
        ]
