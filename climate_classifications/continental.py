"""Continental Climate (Köppen-Geiger: D)"""

CONTINENTAL = {
    "Dfa": {
        "name": "Humid Continental Warm",
        "description": "Very cold winters, warm summers, year-round rainfall",
        "annual_rainfall": "600-1000mm",
        "summer_temp": "15-25°C",
        "winter_temp": "-15 to -5°C",
        "plants": [
            {
                "name": "Red Oak (Quercus rubra)",
                "description": "Hardwood deciduous tree, fast-growing, "
                "excellent for reforestation",
                "extinction_risk": "Least Concern"
            },
            {
                "name": "Sugar Maple (Acer saccharum)",
                "description": "Produces maple syrup, beautiful fall colors, "
                "supports wildlife",
                "extinction_risk": "Least Concern"
            }
        ]
    },
    "Dfb": {
        "name": "Humid Continental Cold",
        "description": "Very long and cold winters, short summers",
        "annual_rainfall": "500-800mm",
        "summer_temp": "10-20°C",
        "winter_temp": "-20 to -10°C",
        "plants": [
            {
                "name": "Siberian Spruce (Picea obovata)",
                "description": "Cold-hardy conifer, slow-growing, "
                "important for boreal forests",
                "extinction_risk": "Least Concern"
            }
        ]
    },
    "Dfc": {
        "name": "Subarctic",
        "description": "Extremely cold, short summer, permafrost zones",
        "annual_rainfall": "300-500mm",
        "summer_temp": "0-15°C",
        "winter_temp": "-30 to -20°C",
        "plants": [
            {
                "name": "Scots Pine (Pinus sylvestris)",
                "description": "Hardy boreal pine, slow-growing, "
                "survives extreme cold",
                "extinction_risk": "Least Concern"
            }
        ]
    }
}


def get_continental(code):
    return CONTINENTAL.get(code, None)


def list_continental_subclasses():
    return list(CONTINENTAL.keys())


def get_continental_plants(code):
    climate = CONTINENTAL.get(code)
    return climate["plants"] if climate else []
