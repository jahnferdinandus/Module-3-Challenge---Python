# Financial Analysis setup
import os
import csv

CSV_PATH = os.path.join("Resources", "budget_data.csv")
OUTPUT_PATH = os.path.join("analysis","analysis.txt")
MONTH_IND = 0
PROFIT_IND = 1

# Total Months
month_count = 0
total_profit = 0
prev_profit = None #Lines to intiate the tracking of these variables
total_change = 0
max_increase = float('-inf') #initialized with negative infinity to make sure that any posotive values enountered in the code are higher than the initial value
max_decrease = float('inf') #initialized with  infinity to make sure that any negative values enountered in the code are lower than the initial value
print(__file__)

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as budget_data:
    csv_reader = csv.reader(budget_data)
    next(csv_reader) #skipped the header row
    #Total Profit/Loss
    for row in csv_reader:
        month_count += 1
        date = row[MONTH_IND]
        current_profit = int(row[PROFIT_IND])
        total_profit += current_profit
        
        #Profit Change
        if prev_profit is not None : # this line is used to skip the first line of row which does not have a previos value and track the change of subsequent rows
            change = current_profit - prev_profit
            total_change += change
            #Max Increase
            if change > max_increase:
                max_increase = change
                max_increase_date = date
            #Max Decrease
            if change < max_decrease:
                max_decrease = change
                max_decrease_date = date
        prev_profit = current_profit # this line is used to update the previous value 

#Average Change
average_change = total_change / (month_count-1) #average change calculation

#Formatting
formatted_total = "${:.0f}".format(total_profit)
formatted_average_change = "${:.2f}".format(average_change)
formatted_max_increase = "${:.0f}".format(max_increase)
formatted_max_decrease = "${:.0f}".format(max_decrease)

#Text Output
output_txt = (
    f"Total Months: {month_count}\n" 
    f"Total {formatted_total}\n"
    f"Average Change : {formatted_average_change}\n"
    f"Greatest Increase in Profits: {max_increase_date} ({formatted_max_increase})\n"
    f"Greatest Decrease in Profits: {max_decrease_date} ({formatted_max_decrease})\n"
)

with open(OUTPUT_PATH, "w") as output_file:
    output_file.write(output_txt)
print(output_txt)
