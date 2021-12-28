# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def updated_damages():
    lst = []
    for costs in damages:
        if costs == "Damages not recorded":
            lst.append(costs)
        elif "M" in costs:
            costs = (float(costs[:-1])*1000000)
            lst.append(int(costs))
        elif "B" in costs:
            costs=(float(costs[:-1])*1000000000)
            lst.append(int(costs))
    return lst

# write your construct hurricane dictionary function here:
def construct_dict():
    lst = dict()
    for x in range(len(names)):
        lst[names[x]] = {"Name": names[x], "Month": months[x], "Year": years[x], "Max Sustained Wind": max_sustained_winds[x], "Areas Affected": areas_affected[x], "Damage": damages[x], "Deaths":deaths[x]}
    return lst

# write your construct hurricane by year dictionary function here:
def construct_dict_year():
    lst = dict()
    for x in range(len(names)):
        lst[years[x]] = {"Name": names[x], "Month": months[x], "Year": years[x], "Max Sustained Wind": max_sustained_winds[x], "Areas Affected": areas_affected[x], "Damage": damages[x], "Deaths":deaths[x]}
    return lst

# write your count affected areas function here:
def area_count():
    lst = dict()
    for group in areas_affected:
        for location in group:
            if location not in lst:
                lst[location] = 1
            else:
                lst[location] += 1
    return lst
# print(area_count())

# write your find most affected area function here:
def mosaff_area():
    max = 0
    for value in area_count().values():
        if value > max:
            max = value
    inv = {v: k for (k, v) in area_count().items()}
    x = inv.get(max)
    return x + " was the most heavily affected after being hit by " + str(max) + " hurricanes."
# print(mosaff_area())

# write your greatest number of deaths function here:
def ded_dict():
    ded = dict()
    for x in range(len(names)):
        ded[names[x]]= deaths[x]
    return ded
# print(ded_dict())

def most_affected():
    max = 0
    for data in deaths:
        if data > max:
            max = data
    x = deaths.index(max)
    name = names[x]
    return(f"Hurricane {name} caused the greatest number of deaths, taking up to {max} lives.")
# print(most_affected())

# write your catgeorize by mortality function here:
def mortality():
    mortality_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for x in range(len(deaths)):
        if deaths[x] < 100:
            mortality_dict[1].append(names[x])
        elif 100 < deaths[x] < 500:
            mortality_dict[2].append(names[x])
        elif 500 < deaths[x] < 1000:
            mortality_dict[3].append(names[x])
        elif 1000 < deaths[x] < 10000:
            mortality_dict[4].append(names[x])
        elif 10000 < deaths[x]:
            mortality_dict[5].append(names[x])
    return mortality_dict

# print(mortality())

# write your greatest damage function here:
def greatest_damage():
    listed_damages=[]
    for data in updated_damages():
        if data != "Damages not recorded":
            listed_damages.append(data)
    max = 0
    for data in listed_damages:
        if data > max:
            max = data
    names_damages = dict()
    for x in range(len(names)):
        names_damages[updated_damages()[x]]=names[x]
    name = names_damages.get(max)
    out = construct_dict()[name]["Damage"]
    place = construct_dict()[name]["Areas Affected"]
    return f"${out} was the most in recorded damages caused by Hurricane {name} which hit:\n {place}" 
# print(greatest_damage())

# write your catgeorize by damage function here:
def damage_category():
    dmg_scale_dict = {0:[], 1:[], 2:[], 3:[], 4:[]}
    listed_damages=[]
    for data in updated_damages():
        if data != "Damages not recorded":
            listed_damages.append(data)
        else:
            listed_damages.append(0)
    for x in range(len(names)):
        if listed_damages[x] < 100000000:
            dmg_scale_dict[1].append(names[x])
        elif  100000000 < listed_damages[x] < 1000000000:
            dmg_scale_dict[2].append(names[x])
        elif  1000000000 < listed_damages[x] < 10000000000:
            dmg_scale_dict[3].append(names[x])
        elif listed_damages[x] > 50000000000:
            dmg_scale_dict[4].append(names[x])
    return dmg_scale_dict
# print(damage_category())

# year with most hurricanes
def unlucky_year():
    max = 1
    for x in range(len(areas_affected)):
        if len(areas_affected[x]) > max:
            max = len(areas_affected[x])
            year = years[x]
    return f"There were {max} hurricanes in {year}, that is the most in one year."
print(unlucky_year())