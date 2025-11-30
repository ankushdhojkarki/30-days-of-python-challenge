#3. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# countries = [
#   'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 
#   'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 
#   'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 
#   'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 
#   'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 
#   'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 
#   'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 
#   'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 
#   'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 
#   'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 
#   'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 
#   'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 
#   'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 
#   'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 
#   'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 
#   'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 
#   'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 
#   'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 
#   'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 
#   'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 
#   'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 
#   'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 
#   'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 
#   'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 
#   'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
# ]

# countries_with_land = []

# for country in countries:
#     if "land" in country:
#         countries_with_land.append(country)
# print(f"Countries containing 'land': {countries_with_land}")

#2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# given_list = ['banana', 'orange', 'mango', 'lemon']

# for i in given_list[::-1]:
#     print(i)

#3. Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world


countries = [
    {'name': 'India', 'languages': ['Hindi', 'English', 'Tamil'], 'population': 1463865525},
    {'name': 'China', 'languages': ['Mandarin'], 'population': 1416096094},
    {'name': 'United States', 'languages': ['English', 'Spanish'], 'population': 347275807},
    {'name': 'Indonesia', 'languages': ['Indonesian'], 'population': 285721236},
    {'name': 'Pakistan', 'languages': ['Urdu', 'English', 'Punjabi'], 'population': 255219554},
    {'name': 'Nigeria', 'languages': ['English', 'Hausa'], 'population': 237527782},
    {'name': 'Brazil', 'languages': ['Portuguese'], 'population': 212812405},
    {'name': 'Bangladesh', 'languages': ['Bengali'], 'population': 175686899},
    {'name': 'Russia', 'languages': ['Russian'], 'population': 143997393},
    {'name': 'Ethiopia', 'languages': ['Amharic'], 'population': 135472051},
    {'name': 'Mexico', 'languages': ['Spanish'], 'population': 131946900},
    {'name': 'Japan', 'languages': ['Japanese'], 'population': 123103479},
    {'name': 'Egypt', 'languages': ['Arabic'], 'population': 118365995},
    {'name': 'Philippines', 'languages': ['Filipino', 'English'], 'population': 116786962},
    {'name': 'United Kingdom', 'languages': ['English', 'Welsh'], 'population': 69551332},
    {'name': 'France', 'languages': ['French'], 'population': 66650804},
    {'name': 'Germany', 'languages': ['German'], 'population': 84075075},
    {'name': 'South Africa', 'languages': ['Zulu', 'Xhosa', 'Afrikaans'], 'population': 64747319},
    {'name': 'Canada', 'languages': ['English', 'French'], 'population': 40126723},
    {'name': 'Thailand', 'languages': ['Thai'], 'population': 69950850},
    {'name': 'Finland', 'languages': ['Finnish', 'Swedish'], 'population': 5540720},
    {'name': 'Iceland', 'languages': ['Icelandic'], 'population': 371720},
    {'name': 'Poland', 'languages': ['Polish'], 'population': 37950000},
    {'name': 'Switzerland', 'languages': ['German', 'French', 'Italian'], 'population': 8600000},
    {'name': 'Netherlands', 'languages': ['Dutch'], 'population': 17500000}
]


# --- 3A: Total Number of Unique Languages ---
print("================================================================")
print("3A. Total Number of Unique Languages")
print("================================================================")

all_languages = set()

# Outer loop iterates through each country dictionary
for country in countries:
    # Inner loop iterates through the list of languages for the current country
    for language in country['languages']:
        all_languages.add(language)

total_languages = len(all_languages)
print(f"Total number of unique languages in the data: {total_languages}\n")

# --- 3B: Ten Most Spoken Languages ---
print("================================================================")
print("3B. Ten Most Spoken Languages (Based on Country Count)")
print("================================================================")

language_counts = {}

# 1. Loop to count each language's frequency
for country in countries:
    for language in country['languages']:
        # Update the count in the dictionary
        if language in language_counts:
            language_counts[language] += 1
        else:
            language_counts[language] = 1

# 2. Convert dictionary to a list of tuples for sorting (using list comprehension for efficiency)
# Format: [(count, language_name), ...]
sorted_languages = [(count, language) for language, count in language_counts.items()]

# Python's list sort is highly efficient
sorted_languages.sort(reverse=True) # Sort in descending order by count

# 3. Loop to extract and print the top 10
print("Rank | Language | Country Count")
print("-" * 35)

for i in range(10):
    if i < len(sorted_languages):
        count, language = sorted_languages[i]
        print(f"{i+1:<4} | {language:<15} | {count}")
    else:
        break

# --- 3C: 10 Most Populated Countries ---
print("\n================================================================")
print("3C. 10 Most Populated Countries")
print("================================================================")

# Create a copy of the list to sort
sorted_countries = list(countries)

# Sort the list by 'population' in descending order
# The lambda function tells the sort method to use the 'population' value for comparison.
sorted_countries.sort(key=lambda country: country['population'], reverse=True)

print("Rank | Country | Population")
print("-" * 40)

# Loop to extract and print the top 10
for i in range(10):
    if i < len(sorted_countries):
        country_name = sorted_countries[i]['name']
        population = sorted_countries[i]['population']
        
        # Format population for readability
        formatted_population = f"{population:,}"
        
        print(f"{i+1:<4} | {country_name:<15} | {formatted_population}")
    else:
        break
