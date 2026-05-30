import matplotlib.pyplot as plt
import numpy as np

def plot_results(soc_history, soh_history, hours_per_day=24, days=60):
    total_hours = len(soc_history)
    time_hours = np.arange(total_hours)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    
    ax1.plot(time_hours, np.array(soc_history) * 100, label='SoC (%)', color='royalblue', linewidth=1.2)
    ax1.axhline(90, color='green', linestyle='--', alpha=0.7, label='Upper limit 90%')
    ax1.axhline(20, color='red', linestyle='--', alpha=0.7, label='Lower limit 20%')
    
    for day in range(days):
        start = day * hours_per_day
        ax1.axvspan(start + 0, start + 6, alpha=0.08, color='navy', label='Low-price period' if day == 0 else "")
        ax1.axvspan(start + 18, start + 22, alpha=0.12, color='orange', label='Peak load period' if day == 0 else "")
    
    ax1.set_title('Battery State of Charge (SoC) over 60 days', fontsize=14)
    ax1.set_ylabel('SoC (%)', fontsize=12)
    ax1.set_ylim(0, 105)
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper right')
    
    ax2.plot(time_hours, np.array(soh_history) * 100, label='SoH (%)', color='darkgreen', linewidth=1.5)
    ax2.set_title('State of Health (SoH) over time', fontsize=14)
    ax2.set_xlabel('Time (hours)', fontsize=12)
    ax2.set_ylabel('SoH (%)', fontsize=12)
    ax2.set_ylim(95, 101)
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.show()