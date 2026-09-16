"""Arid Climate (Köppen-Geiger: B)"""

ARID = {
    "BWh": {
        "name": "Hot Desert",
        "description": "Hot desert with minimal rainfall",
        "annual_rainfall": "<250mm",
        "avg_temperature": ">18°C",
        "plants": [
            {
                "name": "Algarrobo (Prosopis alba)",
                "description": "Drought-tolerant hardwood, "
                "provides shade and firewood",
                "extinction_risk": "Least Concern"
            },
            {
                "name": "Date Palm (Phoenix dactylifera)",
                "description": "Produces fruit, extremely drought-resistant, "
                "adapts to poor soils",
                "extinction_risk": "Least Concern"
            }
        ]
    },
    "BWk": {
        "name": "Cold Desert",
        "description": "Cold desert with minimal rainfall",
        "annual_rainfall": "<250mm",
        "avg_temperature": "<18°C",
        "plants": [
            {
                "name": "Queñoa (Polylepis australis)",
                "description": "Highest altitude tree species, "
                "extremely cold-hardy",
                "extinction_risk": "Endangered"
            }
        ]
    },
    "BSh": {
        "name": "Hot Steppe",
        "description": "Hot semi-arid grassland with moderate rainfall",
        "annual_rainfall": "250-500mm",
        "avg_temperature": ">18°C",
        "plants": [
            {
                "name": "Thornbush (Acacia caven)",
                "description": "Nitrogen-fixing shrub, drought-resistant, "
                "provides firewood",
                "extinction_risk": "Least Concern"
            }
        ]
    },
    "BSk": {
        "name": "Cold Steppe",
        "description": "Cold semi-arid grassland with moderate rainfall",
        "annual_rainfall": "250-500mm",
        "avg_temperature": "<18°C",
        "plants": [
            {
                "name": "Pinyon Pine (Pinus pinyon)",
                "description": "Cold-hardy pine, produces edible seeds, "
                "drought-tolerant",
                "extinction_risk": "Least Concern"
            }
        ]
    }
}


def get_arid(code):
    return ARID.get(code, None)


def list_arid_subclasses():
    return list(ARID.keys())


def get_arid_plants(code):
    climate = ARID.get(code)
    return climate["plants"] if climate else []
