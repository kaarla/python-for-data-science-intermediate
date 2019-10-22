## 1. Reading our MoMA Data Set ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below

for art in moma:
    date = art[6]
    if date != "":
        date = int(date)
    art[6] = date
    

## 2. Calculating Artist Ages ##

ages = []

for art in moma:
    date = art[6]
    birth = art[3]
    age = 0
    
    if date != "":
        date = int(date)
    
    if birth != "":
        birth = int(birth)
        age = date - birth
    ages.append(age)
    
final_ages = []

for ag in ages:
    final_age = "Unknown"
    if ag > 20:
        final_age = ag
    
    final_ages.append(final_age)
        
        
    

## 3. Converting Ages to Decades ##

# The ages variable is available
# from the previous screen

decades = []

for age in ages:
    if age == "Unknown":
        decade = age
    else:
        decade = str(age)[:-1] + "0s"
        #decade = decade
        #decade = decade + "0s"
    
    decades.append(decade)
    

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen

decade_frequency = {}

for decade in decades:
    if decade in decade_frequency:
        decade_frequency[decade] += 1
    else:
        decade_frequency[decade] = 1

## 5. Inserting Variables Into Strings ##

artist = "Pablo Picasso"
birth_year = 1881

template = "{name}'s birth year is {year}"

output = template.format(name=artist, year=birth_year)

print(output)

## 6. Creating an Artist Frequency Table ##

artist_freq = {}

for art in moma:
    artist = art[1]
    
    if artist in artist_freq:
        artist_freq[artist] += 1
    else:
        artist_freq[artist] = 1

## 7. Creating an Artist Summary Function ##

def artist_summary(name):
    value = artist_freq[name]
    template = "There are {value} artworks by {name} in the data set"
    return template.format(value = value, name = name)

henry_sum = artist_summary("Henri Matisse")

print(henry_sum)

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

template = "The population of {country} is {popu:,.2f} million"

for c in pop_millions:
    name = c[0]
    pop = c[1]
    
    print(template.format(country=name, popu=pop))

## 9. Challenge: Summarizing Artwork Gender Data ##

gender_freq = {}

for art in moma:
    gender = art[5]
    if gender in gender_freq:
        gender_freq[gender] += 1
    else:
        gender_freq[gender] = 1

for gen in gender_freq:

    template = "There are {quant:,} artworks by {gender} artists"
    
    print(template.format(quant=gender_freq[gen], gender=gen))