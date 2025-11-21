# Zohran Mamdani's Policy Impact Simulator

A small Python project that simulates the economic impact of two policy ideas:

1. **Rent Freeze** – estimates how much tenants save and how much landlords lose if rents are frozen.
2. **Free Buses** – estimates how much passengers save, how much ticket revenue the MTA loses, and how much taxi drivers might lose when buses become free.

## How it works

The project uses simple assumptions (number of units, fares, trips per day, etc.) and basic math to estimate:

- Tenant savings
- Landlord revenue loss
- MTA ticket revenue loss
- Taxi driver income loss

It then visualizes the results using `matplotlib`.

## Project Structure

```text
nyc-policy-impact-simulator/
├── rent_freeze_analysis.py
├── free_buses_analysis.py
├── main.py
├── requirements.txt
├── README.md
└── images/
    ├── rent_freeze_impact.png
    └── free_buses_impact.png



Sources: NYC.gov, MTA, CBS News, WSJ, NY Times and more