# Tuple of the top 10 safest cities
SAFEST_CITIES = (
    "Tokyo, Japan",
    "Singapore, Singapore",
    "Osaka, Japan",
    "Amsterdam, Netherlands",
    "Sydney, Australia",
    "Toronto, Canada",
    "Washington D.C., United States",
    "Copenhagen, Denmark",
    "Seoul, South Korea",
    "Melbourne, Australia"
)

country = input("Enter the country to search for: ").strip()

count = 0

print("\nMatching cities:")
for index, city in enumerate(SAFEST_CITIES, start=1):
    if country.lower() in city.split(", ")[1].lower():
        print(f"  Number {index} of 10: {city}")
        count += 1


if count == 0:
    print(f"\nThere are 0 cities in {country} among the top 10 SAFEST cities in the world")
else:
    print(f"\nThere {'is' if count == 1 else 'are'} {count} {'city' if count == 1 else 'cities'} in {country} among the top 10 SAFEST cities in the world")
