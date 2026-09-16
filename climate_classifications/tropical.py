"""Tropical Climate (Köppen-Geiger: A)"""

TROPICAL = {
    "Af": {
        "name": "Tropical Rainforest",
        "description": "Year-round rainfall, no dry season",
        "annual_rainfall": ">2000mm",
        "avg_temperature": "24-28°C",
        "plants": [
            {
                "name": "Mahogany (Swietenia macrophylla)",
                "description": (
                    "Large hardwood tree, valuable for timber and agroforestry"
                ),
                "extinction_risk": "Vulnerable"
            },
            {
                "name": "Cacao (Theobroma cacao)",
                "description": (
                    "Medium tree producing chocolate beans, provides shade "
                    "for other crops"
                ),
                "extinction_risk": "Least Concern"
            },
            {
                "name": "Rubber Tree (Hevea brasiliensis)",
                "description": (
                    "Fast-growing tree producing natural rubber, used in "
                    "reforestation"
                ),
                "extinction_risk": "Least Concern"
            }
        ]
    },
    "Am": {
        "name": "Tropical Monsoon",
        "description": "Short dry season (1-2 months), high rainfall",
        "annual_rainfall": "1500-2000mm",
        "avg_temperature": "25-27°C",
        "plants": [
            {
                "name": "Teak (Tectona grandis)",
                "description": "Premium hardwood, drought-resistant, "
                "used for furniture and construction",
                "extinction_risk": "Least Concern"
            },
            {
                "name": "Cedar (Cedrela odorata)",
                "description": "Aromatic hardwood, fast-growing,"
                " valued for timber",
                "extinction_risk": "Vulnerable"
            }
        ]
    },
    "Aw": {
        "name": "Tropical Savanna",
        "description": "Pronounced dry season (4-6 months), moderate rainfall",
        "annual_rainfall": "1000-1500mm",
        "avg_temperature": "25-26°C",
        "plants": [
            {
                "name": "Mopane (Colophospermum mopane)",
                "description": "Drought-resistant tree,"
                " provides food for livestock and wildlife",
                "extinction_risk": "Least Concern"
            },
            {
                "name": "Acacia (Acacia senegal)",
                "description": "Nitrogen-fixing tree, produces gum arabic,"
                " tolerates extreme drought",
                "extinction_risk": "Least Concern"
            }
        ]
    }
}


def get_tropical(code):
    """Returns info for a specific tropical climate"""
    return TROPICAL.get(code, None)


def list_tropical_subclasses():
    """Lists all tropical subclasses"""
    return list(TROPICAL.keys())


def get_tropical_plants(code):
    """Returns plants for a subclass"""
    climate = TROPICAL.get(code)
    return climate["plants"] if climate else []
