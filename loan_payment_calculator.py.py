interest_title = 'Interest Rate'
monthly_title = 'Monthly Payment'
total_title = 'Total Payment'

loan = float(input('Enter loan amount, for example 120000.95: '))
years = int(input('Enter number of years as an integer, for example 5: '))

interest = 5.000

print(f'{interest_title:<20s}{monthly_title:20s}{total_title:<20s}')
while interest <= 8.00:

    monthly = (loan * (interest/1200)) / (1 - (1/((1+(interest/1200))**(years*12))))

    total = monthly * years * 12
    print(f'{interest:<20.3f}{monthly:<20.2f}{total:<20.2f}')
    interest += .125