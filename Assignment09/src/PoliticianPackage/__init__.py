'''
'''

class Politicians():
        def __init__(self, politicianName, politicianTitle, politicianVotePercent):
            self.politicianName = politicianName;
            self.politicianTitle = politicianTitle;
            self.politicianVotePercent = politicianVotePercent;
        
        def setPoliticianName(self, politicianName):
            self.politicianName=politicianName;
        
        def getPoliticianName(self,politicianName):
            return self.politicianName
        
        def setPoliticianTitle(self, politicianTitle):
            self.politicianitle=politicianTitle
        
        def getPoliticianTitle(self,politicianTitle):
            return self.politicianTitle
        
        def checkVotePercent(self, politicianVotePercent):
            if politicianVotePercent > 100:
                print("A politician cannot receive more than 100% of a vote.")
            elif politicianVotePercent<0:
                print("A politician cannot receive less than 0% of a vote.")
            else:
                self.politicianVotePercent = politicianVotePercent
            
        
        def losingVotes(self, politicianVotePercent):
            new_vote = politicianVotePercent/2
            return new_vote
            
        def politicianScandal(self, politicianName, politicianVotePercent):
            return politicianName + " had their vote percentage decrease to " + str(self.losingVotes(politicianVotePercent)) + " percent after their recent scandal."
        
        #dunder:
        
        def __str__(self):
            return "The politician is " + self.politicianName + ", with the title of " + self.politicianTitle + " and received a vote of " + str(self.politicianVotePercent) + " percent"
    
    
        def __repr__(self):
            return "Politician= " + self.politicianName + ", " + "Title= " +  self.politicianTitle + ", " + "Vote Percent= " + str(self.politicianVotePercent)