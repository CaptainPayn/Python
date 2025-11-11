#Inputs of investment, interest rate, and time
fPrincipalInvestment = float(input("Enter the starting principal: "))
fInterestRate = float(input("Enter the annual interest rate: "))/100
fCompounding = float(input("How many times per year is the interest compounded? "))
fNumberOfPeriods = int(input("For how many years will the account earn interest? "))

#Formula FV=PV(1+r/m)**mt
fFutureValue = fPrincipalInvestment*(1+fInterestRate/fCompounding)**(fCompounding*fNumberOfPeriods)

#Display of calculation of future value
print(f"At the end of {fNumberOfPeriods} years you will have ${fFutureValue:,.2f}")

