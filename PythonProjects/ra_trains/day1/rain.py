#!/usr/bin/env python3

rain = { }

while True:
    city_name = input("Enter city: ").strip()
    if not city_name:
        break

    mm_rain = int(input("Enter mm rain: "))
    rain[city_name] = rain.get(city_name, 0) + mm_rain
        
for city, mm_rain in rain.items():
    print(f"{city}: {mm_rain}")


# # City: Tel Aviv
# # Rain: 5
# # City: Jerusalem
# # Rain: 10
# # City: Tel Aviv
# # Rain: 2
# # City: <enter>

# Jerusalem: 10
# Tel Aviv: 7
 
