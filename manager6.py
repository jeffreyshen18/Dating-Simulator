# Jeffrey Shen, 10153021, T04
# Version Number: 1
# Date of last change: December 8, 2016
# The purpose of this file is to act as a control center. This file accesses the modules pursuer.py and target.py. The module itself prompts the user
#for the number of interactions, runs for the specified number of interactions, displays a report as each interaction occurs, and displays a report
#at the end of the simulation.
# A program limitation that exists is that the random generation of a decimal from random.random is not truly random, but pseudorandom. Another limitation
#is that the program does not handle errors if the user inputs a string when prompted for number of interactions or probability.
# Todo list: There is no planned future development for this program
# Features implemented: This program prompts the user for input for a the probability of type "x" and type "y" interaction exhibited by the Target
#and the Pursuer, and uses recursion to ensure that the sum of the probabilities for the Target and Pursuer is equal to 1.0 (100%). The user is
#prompted for the desired number of interactions and the program uses recursion to check that the user inputed a number greater than 0 and less
#than 101. After receiving input from the user, the program will generate random probabilities for the interactions of Target and Pursuer, and display
#the resulting interaction between Target and Pursuer for each interaction. The Target and Pursuer will match when their behaviour type is the same.
#After the total number of interactions is completed, the number of matches will be displayed, and a report will be generated for Target statistics,
#Pursuer statistics, and overall statistics.
import random
import pursuer
import target

class Manager:
    # This method creates an instance of the class Pursuer in the module pursuer.py, and takes manager as self. It accesses the modules
    #pursuer and target to retrieve the probabilities of X-type and Y-type behaviour for Pursuer and Target.
    # This method takes the arguments self.pursuer1 and self.target1 and returns the updated values after input.
    def start(self):
        self.pursuer1 = pursuer.Pursuer()
        self.target1 = target.Target()
        print("Entering probabilities for the \"Pursuer\" type of Tim. The sum of the two probabilities must equal 1.0.")
        self.pursuer1.input()
        print("Entering probabilites for the \"Target\" type of Tim. The sum of the two probabilities must equal 1.0")
        self.target1.input()
    # This method takes the user's input for the desired number of turns to run the simulation and uses recursion to check
    #that the user's input is within range.
    # The method takes the argument self.nRuns and returns the updated value after receiving user input.
    def numRuns(self):
        self.nRuns = int(input("Enter number of turns to run simulation (1-100):"))
        if (self.nRuns > 100 or self.nRuns <1):
            print("Please enter a number from 1-100.")
            self.numRuns()
    # This method randomly generates the probabilities of interactions for the Pursuer and Target
    #based on user entered values and then determines the result (match or mis-match) of each interaction
    #and displays a report as each interaction occurs and displays a report at the end of the simulation.
    #This method retrieves information from the modules pursuer.py and target.py to also display the individual
    #statistics for Target and Pursuer.
    # This method takes the arguments self.pursuer1.NumX, self.target1.NumX, self.pursuer1.NumY,self.target1.NumY, self.nRuns
    #then updates and returns the updated values.
    def numMatches(self):
        self.nMatches = 0
        for i in range (1, (self.nRuns+1)):
            pmatch = random.random() < self.pursuer1.percentX
            tmatch = random.random() < self.target1.percentX
            if pmatch == tmatch: #this is true if it's true and true or false and false
                self.nMatches = self.nMatches +1
                if pmatch == True and tmatch == True:
                    self.pursuer1.NumX = self.pursuer1.NumX  + 1
                    self.target1.NumX = self.target1.NumX + 1
                    print("Turn %i Match: Target x, Pursuer x." % i)
                elif pmatch == False and tmatch == False:
                    self.pursuer1.NumY = self.pursuer1.NumY + 1
                    self.target1.NumY = self.target1.NumY + 1
                    print("Turn %i Match: Target y, Pursuer y." % i)
            if pmatch != tmatch:
                if pmatch == True and tmatch == False:
                    self.pursuer1.NumX = self.pursuer1.NumX + 1
                    self.target1.NumY = self.target1.NumY + 1
                    print("Turn %i No match: Target y, Pursuer x." % i)
                elif pmatch == False and tmatch == True:
                    self.pursuer1.NumY = self.pursuer1.NumY + 1
                    self.target1.NumX = self.target1.NumX + 1
                    print("Turn %i No match: Target x, Pursuer y." % i)
        probMatch = (self.nMatches/self.nRuns)*100
        probMismatch = ((self.nRuns-self.nMatches)/self.nRuns)*100
        print("Number of matches:", self.nMatches)
        print("Target Statistics")
        self.target1.getReport()
        print("Pursuer Statistics")
        self.pursuer1.getReport()
        print("Overall Statistics")
        print("\tNumber of matches:", self.nMatches)
        print("\tNumber of mis-matches:", self.nRuns-self.nMatches)
        print("\tTotal Attempts:", self.nRuns)
        print("\tProportion of matches: %0.1f" % probMatch,"%")
        print("\tProportion of mis-matches: %0.1f" % probMismatch,"%")
