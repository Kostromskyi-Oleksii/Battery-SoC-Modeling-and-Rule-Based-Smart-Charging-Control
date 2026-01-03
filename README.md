# Battery SoC Modeling and Rule-Based Smart Charging Control

## Overview
This project implements a physically meaningful battery energy storage system (BESS) model with State of Charge (SoC) tracking, simplified State of Health (SoH) degradation, and a transparent rule-based smart charging controller.  
The focus is on demonstrating core Electrical Engineering principles in home energy management, battery operation, and basic control strategies.

The project is designed as a pre-university Electrical Engineering study, prioritizing interpretability, educational value, and fundamental physical modeling over complex machine learning approaches.

## Motivation
Battery storage is increasingly critical in electric vehicles, renewable energy integration, peak shaving, and smart grids.  
Effective battery management requires understanding:
- Energy balance and efficiency losses during charge/discharge
- Long-term degradation mechanisms
- Intelligent control strategies to reduce costs and extend battery life

This work uses a simple, rule-based controller to preferentially charge during low-price periods while maintaining safe operation, highlighting how basic logic can achieve meaningful energy and cost optimization.

## System Model

### Components and Parameters

| Component                  | Parameter                              | Value / Description                                      |
|----------------------------|----------------------------------------|----------------------------------------------------------|
| Battery                    | Nominal capacity                       | 4 kWh                                                    |
|                            | Usable SoC range                       | 20% – 90% (to protect battery life)                      |
|                            | Charge/discharge efficiency            | 95% (round-trip ~90%)                                    |
|                            | Maximum charge/discharge power         | 1000 W                                                   |
|                            | SoH degradation model                  | Linear: 3% loss per 100 equivalent full cycles           |
| Household Load             | Base power                             | 300 W                                                    |
|                            | Evening peak                           | 600 W (18:00–22:00)                                      |
| Electricity Pricing        | Low-price window                       | 00:00–06:00 (assumed cheaper tariff)                     |
| Simulation                 | Duration                               | 60 days                                                  |
|                            | Time resolution                        | 1 hour                                                   |

### Key Electrical and Physical Relations
- SoC update via Coulomb counting:  
  ΔSoC = (P × Δt × η) / Capacity (with η = 0.95 for charge, 1/0.95 for discharge)  
- Energy balance each hour: battery supplies deficit or absorbs excess capacity  
- Safe operation: charging/discharging blocked outside 20–90% SoC  
- Cycle counting: equivalent full cycles based on cumulative discharged energy  

## Control Strategy
Rule-based smart charging logic:
- During low-price night hours (00:00–06:00): charge at maximum power if SoC < 90%  
- During evening peak load: discharge to support load if SoC > 20%  
- Otherwise: idle or minimal action to maintain SoC within safe bounds  

This simple strategy reduces electricity costs while protecting battery health.

## Simulation Approach
- Hourly time steps over 60 days (1440 steps total)  
- Deterministic load profile (no randomness for clear cause-effect demonstration)  
- Metrics tracked: SoC trajectory, equivalent cycles, final SoH, minimum SoC  

## Key Results
Typical output from a 60-day simulation:

- **Average SoC**: **47.8%**  
- **Minimum SoC**: **20.0%** (reaches lower bound during peak support)  
- **Final SoH**: **97.0%** (3% degradation due to cycling)  
- **Equivalent full cycles**: ~100 over 60 days  

Two plots are generated:
1. State of Charge over time (clear daily cycling pattern visible)
2. State of Health gradual linear decline

Interpretation:  
The rule-based controller successfully shifts charging to night hours, supports evening peaks, and keeps SoC within safe limits while incurring moderate cycling degradation.

## Analysis and Conclusions
- The simple night-charging strategy effectively reduces peak grid draw and exploits tariff differences.  
- Battery operates safely within defined SoC window, reaching bounds only when needed.  
- Linear degradation model shows realistic long-term capacity fade due to cycling.  
- Recommendations:  
  - Prioritize night charging in real systems with time-of-use tariffs.  
  - Limit depth of discharge to extend life (current usable range already conservative).  
  - Combine with solar generation for greater self-consumption and grid independence.

## Limitations
- Deterministic load (no stochastic consumer behavior).  
- Simplified linear SoH degradation (real batteries exhibit nonlinear, temperature- and DoD-dependent aging).  
- No calendar aging or self-discharge.  
- Assumed constant efficiency (real efficiency varies with SoC and power).  
- No real electricity price data or cost calculation.

## Project Structure
- `config.py`              - All system parameters and constants  
- `battery_model.py`       - Battery class with SoC/SoH tracking and physical methods  
- `load_model.py`          - Deterministic hourly household load profile  
- `charging_controller.py` - Rule-based decision logic  
- `simulation.py`          - Main hourly simulation loop  
- `analysis.py`            - Calculation of key metrics  
- `visualization.py`       - Plots of SoC and SoH over time  
- `main.py`                - Entry point (runs simulation, prints results, displays plots)  
- `README.md`              - This file

## How to Run
1. Install required libraries:
```bash
pip install numpy matplotlib
python main.py
```

The program will:

Simulate 60 days of operation
Print average SoC, minimum SoC, and final SoH
Display two plots showing SoC and SoH evolution over time

Feel free to modify parameters in config.py to explore different battery sizes, load patterns, or control rules!
Possible Extensions

Integrate real time-of-use electricity prices and calculate actual cost savings
Implement nonlinear or cycle-depth-dependent degradation models
Add photovoltaic generation for solar + storage analysis
Replace rule-based control with model predictive control (MPC) or linear programming
Introduce stochastic load variations
Add temperature effects and thermal modeling
Export detailed results to CSV and generate additional visualizations