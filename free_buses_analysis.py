# free_buses_analysis.py

def free_buses_impact(
    bus_trips_per_day=1_400_000,
    #Infromation from MTA
    avg_bus_fare=2.90,
    #Infromation from MTA
    taxi_trips_per_day=800_000,
    #Infromation from MTA
    avg_taxi_fare=15,
    percent_taxi_users_switch_to_bus=0.10,
    days_per_year=365
):
    """
    Calculates passenger savings, MTA loss, and taxi driver loss
    when buses are made free.
    """
    passenger_savings_per_year = bus_trips_per_day * avg_bus_fare * days_per_year
    mta_loss_per_year = passenger_savings_per_year

    taxi_trips_lost_per_day = taxi_trips_per_day * percent_taxi_users_switch_to_bus
    taxi_revenue_lost_per_year = taxi_trips_lost_per_day * avg_taxi_fare * days_per_year

    return passenger_savings_per_year, mta_loss_per_year, taxi_revenue_lost_per_year


if __name__ == "__main__":
    ps, mta, taxi = free_buses_impact()
    print("Passenger savings per year:", ps)
    print("MTA ticket revenue loss per year:", mta)
    print("Taxi drivers' revenue loss per year:", taxi)