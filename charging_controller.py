from config import *

def smart_charging_decision(hour, soc):
    if hour in LOW_PRICE_HOURS and soc < SOC_MAX:
        return "charge"
    if soc > SOC_MIN:
        return "discharge"
    return "idle"
