calculate_fare = lambda distance: 200 + (distance * 50)

distance = float(input("Enter distance (km): "))
total_fare = calculate_fare(distance)

print("\nBase Fare: 200 KES")
print(f"Distance: {distance} km")
print("Cost per km: 50 KES")
print(f"Total Fare: {total_fare} KES")
