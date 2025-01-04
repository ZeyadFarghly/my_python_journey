travel_log = [
    {
        "country":"france",
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits" : 12,
    },
    {
        "country":"Germany",
        "cities_visited": ["Berlin", "Hamburg", "stuttgart"], 
        "total_visits":5
    },
]
country = input()
visits = int(input())
list_of_cities = eval(input())

def add_new_country(country, visits, list_of_cities, travel_log):
    travel_log.append({
        "country": country,
        "cities_visited": list_of_cities,
        "total_visits": visits,           
    })
add_new_country(country, visits, list_of_cities, travel_log)
print(f"I've been to {travel_log[2]["country"]} {travel_log[2]["total_visits"]} times")
print(f"my favorite city is {travel_log[2]["cities_visited"][0]}")

    