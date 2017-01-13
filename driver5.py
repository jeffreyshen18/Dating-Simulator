# Jeffrey Shen, 10153021, T04
# Version Number: 1
# Date of last change: December 8, 2016
# The purpose of this file is to act as the program driver. It enables the program to access the module manager6.py, which acts as the control center.
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
import manager6
#Function does not take any arguments and does not return any arguments. It accesses the manager module, and excecutes the program.
def main():
    manager = manager6.Manager()
    manager.start()
    manager.numRuns()
    manager.numMatches()

main()
