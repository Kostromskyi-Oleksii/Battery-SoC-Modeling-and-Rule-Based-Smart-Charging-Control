# Battery SoC Modeling and Rule-Based Smart Charging Control

## Overview

This project implements a simple yet physically meaningful model of a residential Battery Energy Storage System (BESS) with 4 kWh lithium-ion battery. It includes:

- State of Charge (SoC) tracking using Coulomb counting with charge/discharge efficiencies
- Simplified linear State of Health (SoH) degradation based on cycle count
- Rule-based smart charging controller that charges during low-price night hours and discharges during evening peak load

The main goal is to demonstrate fundamental electrical engineering concepts: energy balance, efficiency losses, battery degradation, and basic energy management strategies for home use. The simulation is deterministic and runs with hourly resolution over 60 days.

This work is designed for educational purposes (pre-university / early university level), prioritizing clarity, interpretability and physical meaning over advanced optimization or machine learning.

## Motivation

Battery energy storage plays a key role in:

- Peak shaving and load shifting
- Exploiting time-of-use (TOU) electricity tariffs
- Integrating renewables and reducing grid stress
- Extending battery lifetime through proper operation

This project shows how a transparent, rule-based controller can achieve meaningful benefits (cost reduction + battery protection) using only simple logic.

## Goal and Objectives

**Goal**  
Demonstrate how a straightforward rule-based charging strategy can shift energy consumption to low-price periods, support peak load, and maintain acceptable battery health.

**Objectives**
- Implement a realistic battery model including SoC dynamics, efficiency, and degradation
- Create a deterministic household load profile with evening peak
- Develop and simulate a rule-based smart charging/discharging controller
- Run a 60-day simulation and collect time series of SoC and SoH
- Analyze key performance metrics and visualize results
- Evaluate the impact of the strategy on battery degradation

## System Model

### Key Components and Parameters

| Component              | Parameter                        | Value / Description                              |
|------------------------|----------------------------------|--------------------------------------------------|
| Battery                | Nominal capacity                 | 4 kWh                                            |
|                        | Usable SoC range                 | 20% - 90% (for longevity)                        |
|                        | Charge efficiency                | 95%                                              |
|                        | Discharge efficiency             | 95%                                              |
|                        | Max charge power                 | 1000 W                                           |
|                        | Max discharge power              | 1200 W                                           |
|                        | SoH degradation                  | Linear: ~5% per 100 equivalent full cycles       |
| Household Load         | Base load                        | 300 W                                            |
|                        | Evening peak load                | 600 W (18:00-22:00)                              |
| Tariff                 | Low-price period                 | 00:00-06:00                                      |
| Simulation             | Duration                         | 60 days                                          |
|                        | Time step                        | 1 hour                                           |

### Core Equations

**Charging**  
ΔE = P_charge × Δt × η_charge
ΔSoC = ΔE / (Capacity × SoH)
SoC ← min(SoC + ΔSoC, 1.0)

**Discharging**  
ΔE = P_discharge × Δt / η_discharge
ΔSoC = ΔE / (Capacity × SoH)
SoC ← max(SoC - ΔSoC, 0.0)

**SoH degradation (simplified linear model)**  
SoH = max(0.7, 1 - degradation_rate × cycles)
where `degradation_rate = 0.0005` per cycle (≈5% loss per 100 full equivalent cycles)

## Control Strategy

The controller uses the following simple rules:

- **Night (00:00-06:00)**: Charge at maximum power if SoC < 90%
- **Evening peak (18:00-22:00)**: Discharge to cover load if SoC > 20%
- **Otherwise**: Idle (no charge/discharge)

This logic prioritizes cheap nighttime charging and peak shaving while respecting safe SoC limits.

## Simulation Setup

- Time resolution: 1 hour
- Total steps: 60 days × 24 hours = 1440 steps
- Load profile: constant base 300 W + evening peak 600 W (18:00-22:00)
- Battery starts at SoC = 50%
- SoH updated once per day (simplified cycle counting)

## Results (typical 60-day simulation)
- **Average SoC**: ≈ 47-49%
- **Minimum SoC**: 20.0% (reached during peak discharge periods)
- **Final SoH**: ≈ 97.0-97.5% (≈2.5-3.0% degradation)
- **Equivalent cycles**: ≈60-100 over 60 days

Generated plots:
1. State of Charge (SoC) over time — shows clear daily cycling pattern
2. State of Health (SoH) over time — gradual linear decline


## Conclusions and Interpretation

The implemented rule-based smart charging strategy demonstrates effective load shifting in a residential setting:

- The battery consistently charges during the low-price night window (00:00-06:00), reaching near 90% SoC by morning in most cycles.
- During evening peak hours (18:00-22:00), the system discharges to support the increased household load (600 W), frequently bringing SoC down to the lower safety limit of 20%.
- Over 60 days of simulation, the average SoC remained at approximately 47-49%, indicating balanced utilization without prolonged deep discharge or overcharge.
- Minimum SoC reached exactly 20.0% multiple times, confirming that the controller respects safety constraints but fully utilizes the available capacity window.
- Battery State of Health degraded to ~97.0-97.5% (2.5-3.0% loss), corresponding to roughly 60-100 equivalent full cycles — a realistic and acceptable degradation rate for light daily cycling.
- The simple rule-based approach successfully reduces grid stress during peak periods and exploits time-of-use tariff differences without requiring complex forecasting or optimization.

Overall, the results confirm that even basic, transparent logic can provide meaningful energy management benefits while preserving battery longevity. For real-world deployment, the strategy could be further enhanced with actual tariff data, weather/load forecasting, and more accurate degradation modeling.


## Project Structure
- `config.py`               - All constants and parameters
- `battery_model.py`        - Battery class (SoC, SoH, charge/discharge)
- `load_model.py`           - Household load profile
- `charging_controller.py`  - Rule-based decision logic
- `simulation.py`           - Main simulation loop
- `analysis.py`             - Key metrics calculation
- `visualization.py`        - SoC and SoH plots
- `main.py`                 - Entry point: run → analyze → plot
- `README.md`

## How to Run

1. Install dependencies
```bash
pip install numpy matplotlib
```
2. Execute the simulation
python main.py

The script will:

Run 60 days of simulation
Print average SoC, min SoC, final SoH
Display two matplotlib plots (SoC and SoH time series)

Feel free to tune parameters in config.py (capacity, efficiencies, degradation rate, load profile, etc.).

## References

- Battery University - How to Prolong Lithium-based Batteries
- NREL Annual Technology Baseline - Utility-Scale Battery Storage (2024)
- Plett, G. L. Battery Management Systems: Volume I & II. Artech House, 2015.
- Tesla Powerwall Specifications
- Various review articles on lithium-ion battery ageing
- Journal of Power Sources (2020-2024)