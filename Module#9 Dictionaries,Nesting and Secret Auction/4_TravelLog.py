# Instructions
# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries. Your job is to create a function that can add new countries to this list.
# Write a function that will work with the following line of code on line 21 to add the entry for Brazil to the travel_log.
# add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])
# DO NOT modify the travel_log directly. The goal is to create a function that modifies it.
# Example: 
# Input
# Brazil
# 5
# ["Sao Paulo", "Rio de Janeiro"]
# Output:
# I've been to Brazil 5 times.
# My favourite city was Sao Paulo.
# Hint
# Look at the function call above to see what the name of the function should be.
# The inputs for the function are positional arguments. The order is very important.
# Feel free to choose your own parameter names.


country = input("Enter Country name") # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
def add_new_country(name, numOfVisit, cities):
  newCountry={}
#   taking a new emptry dictionary
  newCountry["country"]=name
#   assigning countryName with the keyword country
  newCountry["visits"]=numOfVisit
#   assigning numOfVisit with the keyword visits
  newCountry["cities"]=cities
#   assigning cities with the keyword cities  
  travel_log.append(newCountry)
#   appending the travel_log list with another entry called "newCountry"
  
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")