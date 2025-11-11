# Ask for class or work length in minutes.
# Determine hours and minutes length

# Declare a constant of 60 minutes in a hour: 
nMINUTES_IN_HOUR = 60

#1. Input:
iInputtedMinutes = int(input("How many minutes is your class or work shift in whole numbers: "))

#Maths
iHours = iInputtedMinutes//nMINUTES_IN_HOUR
iMinutes = iInputtedMinutes%nMINUTES_IN_HOUR

#Print Results
print(f"{iInputtedMinutes:} minutes is: {iHours} hour(s) and {iMinutes} minutes")
