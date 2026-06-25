
#calculate the taxi based on person salary
salary=int(input("enter your salary:"))
if salary<=250000:
    print("taxi is 0")
elif salary<=500000:
    taxi=salary-250000
    print("calculated taxi is",(taxi*5)/100)
elif salary<=1000000:
    taxi=salary-500000
    print("calculated taxi is",(250000*5)/100+(taxi*7)/100)
else:
    taxi=salary-1000000
    print("calculated taxi is",(250000*5)/100+(500000*7)/100+(taxi*10)/100)
