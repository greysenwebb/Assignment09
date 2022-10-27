#Name: Kili-Greysen Webb, Ava Berling, Colin Bui, David Burkhart
#email: webbgp@mail.uc.edu, berlinag@mail.uc.edu, buici@mail.uc.edu, burkhadj@mail.uc.edu
#Assignment: Assignment 09
#Course: IS 4010
#Semester/Year: Fall 2022
#Brief Description: This project demonstrates that we can work effectively as a team, use dunder and non dunder methods within classes, and use classes within python
#Citations:N/A
#Anything else that's relevant: This was worked on by Colin Bui


class Government():
        def __init__(self, government_name, government_type, government_founding):
            self.government_name = government_name;
            self.government_type = government_type;
            self.government_founding = government_founding;
        
        def setGovernmentName(self, government_name):
            self.government_name=government_name;
        
        def getGovernmentName(self, government_name):
            return self.government_name
        
        def setGovernmentType(self, government_type):
            self.government_type=government_type;
        
        def getGovernmentType(self, government_type):
            return self.government_type
        
        def setGovernmentFounding(self, government_founding):
            self.government_founding=government_founding;
        
        def getGovernmentFounding(self, government_founding):
            return self.government_founding
        
        def coup(self,government_type):
            government_type="Dictatorship"
            return "The government is now a " + government_type
        
        #dunders:
        
        def __str__(self):
            return "The government is " + self.government_name + ", with the type of " + self.government_type  + ",and founded in " + self.government_founding
    
    
        def __repr__(self):
            return "Government= " + self.government_name + ", " + "Type= " +  self.government_type + "," + "Foundation=" + self.government_founding
        