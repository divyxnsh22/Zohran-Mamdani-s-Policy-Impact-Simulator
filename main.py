# main.py

from rent_freeze_analysis import rent_freeze_impact
from free_buses_analysis import free_buses_impact
import matplotlib.pyplot as plt
import os


# 1) Rent freeze results
rent_loss_1y = rent_freeze_impact(years=1)
rent_loss_3y = rent_freeze_impact(years=3)

print("=== Rent Freeze Impact ===")
print("1-year freeze - tenants saved / landlords lost:", rent_loss_1y)
print("3-year freeze - tenants saved / landlords lost:", rent_loss_3y)

# Plot rent freeze comparison
plt.figure()
years = [1, 3]
losses = [rent_loss_1y, rent_loss_3y]
plt.plot(years, losses, marker="o")
plt.title("Rent Freeze: Total Tenant Savings vs Duration")
plt.xlabel("Years of Freeze")
plt.ylabel("Dollars")
plt.grid(True)
plt.savefig("images/rent_freeze_impact.png", bbox_inches="tight")
# plt.show()


# 2) Free buses results
ps, mta, taxi = free_buses_impact()

print("\n=== Free Buses Impact (Per Year) ===")
print("Passenger savings:", ps)
print("MTA ticket revenue loss:", mta)
print("Taxi drivers' revenue loss:", taxi)

# Plot free buses impact
plt.figure()
labels = ["Passengers Saved", "MTA Lost", "Taxi Lost"]
values = [ps, mta, taxi]
plt.bar(labels, values)
plt.title("Impact of Free Buses (Per Year)")
plt.ylabel("Dollars")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("images/free_buses_impact.png", bbox_inches="tight")
# plt.show()

print("\nPlots saved in the 'images/' folder.")