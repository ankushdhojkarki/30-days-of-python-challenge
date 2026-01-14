#15. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
# Sort countries by name, by capital, by population
countries_data = [
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": ["Pashto", "Uzbek", "Turkmen"],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    },
    {
        "name": "Estonia",
        "capital": "Tallinn",
        "languages": ["Estonian"],
        "population": 1315944,
        "flag": "https://restcountries.eu/data/est.svg",
        "currency": "Euro"
    },
    {
        "name": "Finland",
        "capital": "Helsinki",
        "languages": ["Finnish", "Swedish"],
        "population": 5491817,
        "flag": "https://restcountries.eu/data/fin.svg",
        "currency": "Euro"
    },
    {
        "name": "China",
        "capital": "Beijing",
        "languages": ["Chinese"],
        "population": 1377422166,
        "flag": "https://restcountries.eu/data/chn.svg",
        "currency": "Chinese yuan"
    },
    {
        "name": "India",
        "capital": "New Delhi",
        "languages": ["Hindi", "English"],
        "population": 1295210000,
        "flag": "https://restcountries.eu/data/ind.svg",
        "currency": "Indian rupee"
    },
    {
        "name": "Iceland",
        "capital": "Reykjavik",
        "languages": ["Icelandic"],
        "population": 334300,
        "flag": "https://restcountries.eu/data/isl.svg",
        "currency": "Icelandic króna"
    }
]
sorted_by_name = sorted(countries_data, key=lambda c: c['name'])
sorted_by_capital = sorted(countries_data, key=lambda c: c.get('capital', ''))
sorted_by_population = sorted(countries_data, key=lambda c: c['population'], reverse=True)

# Sort out the ten most spoken languages by location.
def most_spoken_languages(data, limit=10):
    language_counts = {}
    for country in data:
        for lang in country['languages']:
            language_counts[lang] = language_counts.get(lang, 0) + 1
    sorted_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:limit]
print(most_spoken_languages(countries_data, 10))


# Sort out the ten most populated countries.
def most_populated_countries(data, limit=10):
    sorted_pop = sorted(data, key=lambda c: c['population'], reverse=True)
    return [{'country': c['name'], 'population': c['population']} for c in sorted_pop[:limit]]

top_ten_pop = most_populated_countries(countries_data, 10)
for i, country in enumerate(top_ten_pop, 1):
    print(f"{i}. {country['country']}: {country['population']:,}")
