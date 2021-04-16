##PyBank
import os
import csv

##Read file from Resources/budget_data.csv
dirname = os.path.dirname(__file__)

csvpath = os.path.join(dirname,'Resources','budget_data.csv')

#initialising variables
total = 0
months = 0
change = 0
tot_change = 0
avg_change = 0
previous_net = 0
max_inc = ['', 0]
min_inc = ['', 0]

#open csv file
with open(csvpath,'r') as bankdata:
    reader = csv.reader(bankdata)

    # read header
    header = next(reader)


    # get data from the first row
    row_one = next(reader)
    months += 1
    total += int(row_one[1])
    previous_net = int(row_one[1])


    for row in csv.reader(bankdata):
    
        # Calculate total and total months
        total += int(row[1])
        months += 1

        # Calculate net change
        change = int(row[1]) - previous_net
        tot_change += change


        # Adjust previous_net
        previous_net = int(row[1])


        # Calculate increase
        if change > max_inc[1]:
            max_inc[0] = row[0]
            max_inc[1] = change

        # Calculate decrease
        if change < min_inc[1]:
            min_inc[0] = row[0]
            min_inc[1] = change

# Calculate Average change
avg_change = tot_change / (months-1) 

        

#creating summary table
output = (
    f'\n'
    f'Financial Analysis\n'
    f'----------------------------\n'
    f'Total Months: {months}\n'
    f'Total: ${total}\n'
    f'Average  Change: ${avg_change}\n'
    f'Greatest Increase in Profits: {max_inc[0]} $({max_inc[1]})\n'
    f'Greatest Decrease in Profits: {min_inc[0]} $({min_inc[1]})\n'
)

#printing output to terminal
print(output)

#write output to text file
##Create text file under analysis/pybank_solution.csv
output_path = os.path.join(dirname,'analysis','pybank_analysis.txt')
with open(output_path,'w') as txt_file:
    txt_file.write(output)