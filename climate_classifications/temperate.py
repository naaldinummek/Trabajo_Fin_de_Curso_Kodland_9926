"""Temperate Climate (Köppen-Geiger: C)"""

TEMPERATE = {
    "Csa": {
        "name": "Hot Mediterranean",
        "description": "Hot dry summer, mild wet winter",
        "annual_rainfall": "600-900mm",
        "avg_temperature": "15-20°C",
        "plants": [
            {
                "name": "Olive Tree (Olea europaea)",
                "description": "Drought-resistant, long-lived, "
                "produces oil and fruit",
                "extinction_risk": "Least Concern"
            },
            {
                "name": "Stone Pine (Pinus pinea)",
                "description": "Mediterranean pine, produces edible seeds, "
                "drought-tolerant",
                "extinction_risk": "Least Concern"
            }
        ]
    },
    "Csb": {
        "name": "Warm Mediterranean",
        "description": "Dry summer but cool, moderate rainfall",
        "annual_rainfall": "700-1000mm",
        "avg_temperature": "12-18°C",
        "plants": [
            {
                "name": "Holm Oak (Quercus ilex)",
                "description": "Evergreen oak, drought and frost-tolerant, "
                "provides acorns",
                "extinction_risk": "Least Concern"
            }
        ]
    },
    "Cfa": {
        "name": "Humid Subtropical",
        "description": "Year-round rainfall, hot summers",
        "annual_rainfall": "1000-1500mm",
        "avg_temperature": "18-25°C",
        "plants": [
            {
                "name": "Bay Laurel (Laurus nobilis)",
                "description": "Aromatic evergreen, "
                "used for culinary and medicinal purposes",
                "extinction_risk": "Least Concern"
            }
        ]
    },
    "Cfb": {
        "name": "Oceanic",
        "description": "Temperate, no dry season, mild winters",
        "annual_rainfall": "800-1200mm",
        "avg_temperature": "8-17°C",
        "plants": [
            {
                "name": "European Beech (Fagus sylvatica)",
                "description": "Deciduous hardwood, shade-tolerant, "
                "produces beech nuts",
                "extinction_risk": "Least Concern"
            }
        ]
    }
}


def get_temperate(code):
    return TEMPERATE.get(code, None)


def list_temperate_subclasses():
    return list(TEMPERATE.keys())


def get_temperate_plants(code):
    climate = TEMPERATE.get(code)
    return climate["plants"] if climate else []
