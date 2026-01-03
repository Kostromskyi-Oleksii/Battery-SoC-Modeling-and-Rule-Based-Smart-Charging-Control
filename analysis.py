import numpy as np

def analyze(soc, soh):
    return {
        "average_soc": np.mean(soc),
        "final_soh": soh[-1],
        "minimum_soc": np.min(soc)
    }
