#Name: Kili-Greysen Webb, Ava Berling, Colin Bui, David Burkhart
#email: webbgp@mail.uc.edu, berlinag@mail.uc.edu, buici@mail.uc.edu, burkhadj@mail.uc.edu
#Assignment: Assignment 09
#Course: IS 4010
#Semester/Year: Fall 2022
#Brief Description: This project demonstrates that we can work effectively as a team, use dunder and non dunder methods within classes, and use classes within python
#Citations:N/A
#Anything else that's relevant: This was worked on by Ava Berling

class Countries():
        def __init__(self, country_name, country_continent, country_population):
            self.country_name=country_name;
            self.country_continent=country_continent;
            self.country_population=country_population;
        
        def set_CountryName(self, country_name):
            self.country_name=country_name;
        
        def get_CountryName(self,country_name):
            return self.country_name
        
        def set_ContinentName(self, country_continent):
            self.country_continent=country_continent
            
        def get_ContinentName(self, country_continent):
            return country_continent
        
        def check_population(self, country_population):
            if country_population < 0:
                print ("The population cannot be less than 0")
            else:
                self.country_population = country_population
                
        def set_population(self, country_population):
            self.check_population(country_population)
        
        def decrease_population(self, country_population):
            new_total=country_population/2
            return new_total
        
        def plague(self, country_name, country_population):
            return "The country " + country_name + "'s population decreased by half at " + str(self.decrease_population(country_population))
    
    #dunder methods
        def __str__(self):
        #prints a pretty sring representation of the object. easier is read in the output
            return "The country is " + self.country_name + ", located on the continent of " + self.country_continent + " and has a population of " + str(self.country_population)
    
        def __repr__(self):
        #returns a string representation of the object
            return "Country= " + self.country_name + ", " + "Continent= " +  self.country_continent + ", " + "Population= " + str(self.country_population)
        
        