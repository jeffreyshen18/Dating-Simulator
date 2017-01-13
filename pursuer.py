# Jeffrey Shen, 10153021, T04
# Version Number: 1
# Date of last change: December 8, 2016
# The purpose of this file is to get the user's input for the probability of a X-type behaviour occuring during an interaction for Pursuer
#and the probability of a Y-type behaviour occuring during an interaction for Pursuer, implementing recursion to ensure that the probability is
#within range (0.1-1.0), and printing a report for the Pursuer statistics at the end of the simulation.
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

class Pursuer:
    # This method initializes an instance of a class.
    # This method contains four arguments (self.percentX, self.percentY, self.NumX, self.NumY)
    def __init__(self):
        self.percentX = ""
        self.percentY = ""
        self.NumX = 0
        self.NumY = 0
    # This method takes the user's input for the probabilities of X-type behaviour and Y-type behaviour for the ,
    #and uses recursion to handle if the input is out of range.
    # This method contains two arguments (self.percentX and self.percentY). It updates and returns the the arguments after user input.
    def input(self):
        self.percentX = float(input("\tEnter the probability that X-type of behaviours will occur during an interaction during the date:"))
        self.percentY = float(input("\tEnter the probability that Y-type of behaviours will occur during an interaction during the date:"))
        if (self.percentX + self.percentY) != 1.0:
            print("Error: the two probabilities equals %0.1f (must sum to 1.0). Please re-enter the values." % (self.percentX+self.percentY))
            self.input()
    # This method generates a report for the total number of X-type behaviours and Y-type behaviours for Pursuer after the simulation is run.
    # This method contains two arguments (self.NumX and self.NumY)
    def getReport(self):
        print("\tNumber of X's:", self.NumX)
        print("\tNumber of Y's:", self.NumY)
