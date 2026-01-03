from battery_model import Battery
from load_model import get_load
from charging_controller import smart_charging_decision
from config import *

def run_simulation():
    battery = Battery(BATTERY_CAPACITY_WH, INITIAL_SOC)
    soc_history = []
    soh_history = []

    for day in range(SIMULATION_DAYS):
        for hour in range(HOURS_PER_DAY):
            decision = smart_charging_decision(hour, battery.soc)
            load = get_load(hour)

            if decision == "charge":
                battery.charge(MAX_CHARGE_POWER, DT, CHARGE_EFFICIENCY)
            elif decision == "discharge":
                battery.discharge(load, DT, DISCHARGE_EFFICIENCY)

            soc_history.append(battery.soc)
            soh_history.append(battery.soh)

        battery.update_soh(DEGRADATION_PER_CYCLE)

    return soc_history, soh_history
