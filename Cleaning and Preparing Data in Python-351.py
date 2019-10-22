## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`

from csv import reader

opened_file = open('artworks.csv')
read_file = reader(opened_file)
moma = list(read_file)

num_rows = len(moma[1:])

## 2. Reading our MoMA Data Set ##

# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('children.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format

children = list(read_file)

# remove the first row of the data, which
# contains the column names
children = children[1:]

# Write your code here
opened_file = open('artworks.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
moma = list(read_file)

# remove the first row of the data, which
# contains the column names
moma = moma[1:]


## 3. Replacing Substrings with the replace Method ##

age1 = "I am thirty-one years old"

age2 = age1.replace('one', 'two')

## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again

opened_file = open('artworks.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

for art in moma:
    nationality = art[2]
    gender = art[5]
    
    nationality = nationality.replace("(", "")
    nationality = nationality.replace(")", "")
    gender = gender.replace("(", "")
    gender = gender.replace(")", "")
    
    art[2] = nationality
    art[5] = gender


## 5. String Capitalization ##

for art in moma:
    gender = art[5]
    gender = gender.title()
    
    if not gender:
        gender = "Gender Unknown/Other"
    
    art[5] = gender
    
    nationality = art[2]
    nationality = nationality.title()
    
    if not nationality:
        nationality = "Nationality Unknown"
        
    art[2] = nationality

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

for art in moma:
    beginDate = art[3]
    endDate = art[4]
    
    art[3] = clean_and_convert(beginDate)
    art[4] = clean_and_convert(endDate)

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(s):
    for c in s:
        if c in bad_chars:
            s = s.replace(c, "")
    return s;

stripped_test_data = []

for data in test_data:
    stripped_test_data.append(strip_characters(data))

## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def process_date(s):
    if "-" in s:
        arr = s.split("-")
        return round((int(arr[0]) + int(arr[1])) / 2)
    else:
        return int(s)

processed_test_data = []

for data in stripped_test_data:
    processed_test_data.append(process_date(data))   

print(processed_test_data)


for art in moma:
    date = art[6]
    date = strip_characters(date)
    date = process_date(date)
    art[6] = date