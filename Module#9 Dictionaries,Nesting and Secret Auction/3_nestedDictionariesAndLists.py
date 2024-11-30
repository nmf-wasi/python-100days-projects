#list
cities=["Tokyo", "Berlin", "Seoul"]

#list in list
citiesOfCountries = [
    ["Tokyo","Kyoto"],
    ["Aukland" "Wellington"], 
    ["Seoul", "Gangnam"]
]

# dictionary
tours = {
    "Japan":"Tokyo",
    "NewZaland":"Aukland",
    "sKorea":"Seoul" 
}

# list in dictionary
tours = {
    "Japan":["Tokyo","Kyoto"],
    "NewZaland":["Aukland","Wellington"],
    "sKorea":["Seoul", "Gangnam"] 
}

# dictionary in list
cities=[
    {
        "country":"japan",
        "city":["Tokyo","Kyoto"],
        "attractions": ["Mt. Fuji", "Shibuya Crossing", "Tokyo Tower"]
    },
    {
        "country":"Australia",
        "city":["Melbourne","Sydney"],
        "attractions": ["SydneyOpera", "optusStadium"]
    },
    {
        "country":"sKorea",
        "city":["Seoul", "Gangnam"],
        "attractions": ["Gyeongbokgung Palace", "N Seoul Tower", "Myeongdong"]
    }
]
# dictionary in dictionary
visitedCities={
    "Japan":{
        "visitCount":"3",
        "cities":["Tokyo","Kyoto"],
        "attractions" : ["Mt. Fuji", "Shibuya Crossing", "Tokyo Tower"]
    },
    "Australia":{
        "visitCount":"4",
        "cities":["Melbourne","Sydney"],
        "attractions": ["SydneyOpera", "optusStadium"]
    },
    "sKorea":{
        "visitCount":"1",
        "cities":["Seoul", "Gangnam"],
        "attractions": ["Gyeongbokgung Palace", "N Seoul Tower", "Myeongdong"]
    }
}


