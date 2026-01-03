import matplotlib.pyplot as plt

def plot_results(soc, soh):
    plt.figure()
    plt.plot(soc)
    plt.title("State of Charge over Time")
    plt.xlabel("Hour")
    plt.ylabel("SoC")
    plt.grid()
    plt.show()

    plt.figure()
    plt.plot(soh)
    plt.title("State of Health over Time")
    plt.xlabel("Hour")
    plt.ylabel("SoH")
    plt.grid()
    plt.show()
