from CountriesPackage import Countries
from PoliticianPackage import Politicians

#Demonstrating the Countries class works as intended
USA=Countries("United States of America","North America",332403650)
print(USA)
print(repr(USA))

print(Countries.plague(USA,USA.country_name,USA.country_population))

#Demonstrating the Politicians class works as intended 

Joe=Politicians("Joe Biden", "President of the United States", 51.3)

print(Joe)
print(repr(Joe))

print(Politicians.politicianScandal(Joe,Joe.politicianName,Joe.politicianVotePercent))