# rent_freeze_analysis.py

def rent_freeze_impact(
    apartments=2_324_000,
    #Information from nyc.com
    avg_rent=3599,
    #Information from apartments.com
    increase_rate=3,
    #Information from cbs news
    years=1
):
    """
    Calculates total tenant savings and landlord revenue loss
    for a rent freeze.
    """
    increase_per_month = avg_rent * increase_rate
    increase_per_year = increase_per_month * 12

    total_lost_revenue_per_year = increase_per_year * apartments
    total_lost_revenue = total_lost_revenue_per_year * years

    return total_lost_revenue  # same for tenants saved & landlords lost


if __name__ == "__main__":
    loss = rent_freeze_impact()
    print("Total money saved by tenants:", loss)
    print("Total money lost by landlords:", loss)