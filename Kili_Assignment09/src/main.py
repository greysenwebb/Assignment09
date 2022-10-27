#Name: Kili-Greysen Webb, Ava Berling, Colin Bui, David Burkhart
#email: webbgp@mail.uc.edu, berlinag@mail.uc.edu, buici@mail.uc.edu, burkhadj@mail.uc.edu
#Assignment: Assignment 09
#Course: IS 4010
#Semester/Year: Fall 2022
#Brief Description: This project demonstrates that we can work effectively as a team, use dunder and non dunder methods within classes, and use classes within python
#Citations:N/A
#Anything else that's relevant: This was worked on by Greysen Webb


from CountriesPackage import Countries
from PoliticianPackage import Politicians
from GovernmentPackage import Government

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

#Demonstrating the Government class works as intended

USAGov=Government("Federal Government of the United States","Federal Democratic Republic", "1776")

print(USAGov)
print(repr(USAGov))

print(Government.coup(USAGov,USAGov.government_type))
