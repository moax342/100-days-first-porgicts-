travel_log = [
    {
        "country": "france",
        "visits": 12,
        "cities": ["paris", "Lialle", "Dijan"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(city, number_of_visits, cities):
    travel_log.append({
        "country": city,
        "visits": number_of_visits,
        "cities": cities
    })


add_new_country("Russa", 12, ["Moscow", "Saint petersperg", "keev"])
print(travel_log)
