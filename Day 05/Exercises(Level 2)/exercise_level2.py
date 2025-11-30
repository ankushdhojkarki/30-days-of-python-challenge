'''
1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Sort the list and find the min and max age
Add the min age and the max age again to the list
Find the median age (one middle item or two middle items divided by two)
Find the average age (sum of all items divided by their number )
Find the range of the ages (max minus min)
Compare the value of (min - average) and (max - average), use abs() method

'''
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(f"Minimum Age: {min(ages)}")
print(f"Maximum Age: {max(ages)}")

ages.append(min(ages))
ages.append(max(ages))
print(ages)

length_ages = len(ages)
middle_index1 = length_ages//2-1
middle_index2 = length_ages//2
median = (ages[middle_index1]+ages[middle_index2])/2
print(median)

sum_ages = sum(ages)
count_ages = len(ages)
average_age = sum_ages/count_ages
print(average_age)

age_range = max(ages)-min(ages)
print(age_range)

min_age = min(ages)
max_age = max(ages)
diff_min = abs(min_age - average_age)
diff_max = abs(max_age - average_age)
print(f"|Min - Avg|: {diff_min}")
print(f"|Max - Avg|: {diff_max}")

#2.Find the middle country(ies) in the countries list
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

middle_country_index = len(countries)//2
middle_country = countries[middle_country_index]
print(middle_country)

#2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
length_countries = len(countries)
print(length_countries)

cutoff_index = (length_countries+1)//2
first_half = countries[:cutoff_index]
second_half = countries[cutoff_index:]
print(first_half)
print(f"{'-'*70}")
print(second_half)

#3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

new_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us, *scandic = new_list
print(f"First three countries: {ch, ru, us}")
print(f"Scandic countries: {scandic}")