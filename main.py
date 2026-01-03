from simulation import run_simulation
from analysis import analyze
from visualization import plot_results

soc, soh = run_simulation()
results = analyze(soc, soh)

for k, v in results.items():
    print(f"{k}: {v}")

plot_results(soc, soh)
