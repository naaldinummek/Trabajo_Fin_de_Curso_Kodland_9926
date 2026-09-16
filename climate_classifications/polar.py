"""Polar Climate (Köppen-Geiger: E)"""

POLAR = {
    "ET": {
        "name": "Tundra",
        "description": "Extremely cold, no trees, short growing season",
        "annual_rainfall": "150-400mm",
        "avg_temperature": "-20 to 0°C",
        "plants": [
            {
                "name": "Arctic Willow (Salix arctica)",
                "description": "Dwarf shrub, extremely cold-hardy, "
                "stabilizes soil",
                "extinction_risk": "Least Concern"
            },
            {
                "name": "Arctic Grass (Alopecurus alpinus)",
                "description": "Low-growing grass, "
                "food source for Arctic wildlife",
                "extinction_risk": "Least Concern"
            }
        ]
    },
    "EF": {
        "name": "Polar Ice Cap",
        "description": "Permanent ice and snow, no vegetation",
        "annual_rainfall": "<100mm",
        "avg_temperature": "<-20°C",
        "plants": [
            {
                "name": "Arctic Moss (Hypnum cupressiforme)",
                "description": "Rare hardy moss, minimal carbon sequestration",
                "extinction_risk": "Least Concern"
            }
        ]
    }
}


def get_polar(code):
    return POLAR.get(code, None)


def list_polar_subclasses():
    return list(POLAR.keys())


def get_polar_plants(code):
    climate = POLAR.get(code)
    return climate["plants"] if climate else []
