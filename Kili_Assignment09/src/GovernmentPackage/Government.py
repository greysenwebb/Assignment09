'''
'''
class Government():
        def __init__(self, government_name, government_type, government_leaders):
            self.government_name = government_name;
            self.government_type = government_type;
            self.government_leaders = government_leaders;
        
        def setGovernmentName(self, government_name):
            self.government_name=government_name;
        
        def getGovernmentName(self, government_name):
            return self.government_name
        
        def setGovernmentType(self, government_type):
            self.government_type=government_type;
        
        def getGovernmentType(self, government_type):
            return self.government_type
        
        def checkLeaders(self, government_leaders):
            if government_leaders < 1:
                print ("This Government has no leaders")
            else:
                self.government_leaders=government_leaders
            
        
        #dunders:
        
        def __str__(self):
            return "The government is " + self.government_name + ", with the type of " + self.government_type  + ",and led by " + self.government_leaders
    
    
        def __repr__(self):
            return "Government= " + self.government_name + ", " + "Type= " +  self.government_type + "," + "Leaders=" + self.government_leaders
        
        