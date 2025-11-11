#Asking for name
sName = input("What is your name: ")
#Asking for weight
fEarthWeight = float(input("What is your weight: "))

#Planet Conversion Factors
fMERCURY_FACTOR = 0.38
fVENUS_FACTOR = 0.91
fMOON_FACTOR = 0.165
fMARS_FACTOR = 0.38
fJUPITER_FACTOR = 2.34
fSATURN_FACTOR = 0.93
fURANUS_FACTOR = 0.92
fNEPTUNE_FACTOR = 1.12
fPLUTO_FACTOR = 0.066

#Maths
fWeightOnMercury = fEarthWeight * fMERCURY_FACTOR
fWeightOnVenus = fEarthWeight * fVENUS_FACTOR
fWeightOnMoon = fEarthWeight * fMOON_FACTOR
fWeightOnMars = fEarthWeight * fMARS_FACTOR 
fWeightOnJupiter = fEarthWeight * fJUPITER_FACTOR 
fWeightOnSaturn = fEarthWeight * fSATURN_FACTOR 
fWeightOnUranus = fEarthWeight * fURANUS_FACTOR 
fWeightOnNeptune = fEarthWeight * fNEPTUNE_FACTOR 
fWeightOnPluto = fEarthWeight * fPLUTO_FACTOR 

#Printing Results
print (f"{sName} here are your weights on the Solar System's planets:")
print (f"Weight on Mercury is: {fWeightOnMercury:>10.2f}")
print (f"Weight on Venus is:   {fWeightOnVenus:>10.2f}")
print (f"Weight on Moon is:    {fWeightOnMoon:>10.2f}")
print (f"Weight on Mars is:    {fWeightOnMars:>10.2f}")
print (f"Weight on Jupiter is: {fWeightOnPluto:>10.2f}")
print (f"Weight on Saturn is:  {fWeightOnSaturn:>10.2f}")
print (f"Weight on Uranus is:  {fWeightOnUranus:>10.2f}")
print (f"Weight on Neptune is: {fWeightOnNeptune:>10.2f}")
print (f"Weight on Pluto is:   {fWeightOnPluto:>10.2f}")

