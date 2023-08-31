# Financial Analysis setup
import os
import csv

csv_file = "Module-3-Challenge---Python\\PyBank\\Resources\\budget_data.csv"

# Month count code
month_count = 0
with open (csv_file) as budget_data:
    csv_reader = csv.reader(budget_data, delimiter=',')
    for month in csv_reader:
        month_count += 1

print("Total Months:", month_count)

# Total value calculation code
column_index = 1 #defined the column index
total = 0
with open (csv_file, "r") as budget_data:
    csv_reader = csv.reader(budget_data, delimiter=',')
    next(csv_reader) #skipped the header row
    for row in csv_reader:
        value = float(row[column_index])
        total += value
total_value_int = int(total) #removed decimals by converting to int. 

print("Total", total_value_int)

# Average change calculation code

column_index = 1 #defined the column index
with open (csv_file, "r") as budget_data:
    csv_reader = csv.reader(budget_data, delimiter=',')
    next(csv_reader) #skipped the header row

    prev_value = None #Lines to intiate the tracking of these variables
    total_change = 0
    row_count = 0

    for row in csv_reader:
        value = float(row[column_index]) #this line is used to extract the value from the column index and convert it to a float
        if prev_value is not None : # this line is used to skip the first line of row which does not have a previos value and track the change of subsequent rows
            change = value - prev_value
            total_change += change
            row_count += 1

        prev_value = value # this line is used to update the previous value 
    if row_count > 0: #line added to make the answer an int instead of text. Why cannot I simply remove this line. 
        average_change = total_change / row_count #average change calculation
        print  ("Average Change : $",average_change)

# Max increase calculation code

column_index = 1 #defined the profit column index
with open (csv_file, "r") as budget_data:
    csv_reader = csv.reader(budget_data, delimiter=',')
    next(csv_reader) #skipped the header row
   
    prev_value = None #Lines to intiate the tracking of these variables
    max_increase = float('-inf') #initialized with negative infinity to make sure that any posotive values enountered in the code are higher than the initial value
    max_increase_date = ""
    
    for row in csv_reader:
        date = row[0]
        value = float(row[column_index])

        if prev_value is not None:
            change = value - prev_value
            if change > max_increase:
                max_increase = change
                max_increase_date = date

        prev_value = value

    if max_increase_date:
        print("Greatest Increase in Profits:", max_increase_date, "($", max_increase, ")")


# Max decrease calculation code

column_index = 1 #defined the profit column index
with open (csv_file, "r") as budget_data:
    csv_reader = csv.reader(budget_data, delimiter=',')
    next(csv_reader) #skipped the header row
   
    prev_value = None #Lines to intiate the tracking of these variables
    max_decrease = float('inf') #initialized with  infinity to make sure that any negative values enountered in the code are lower than the initial value
    max_decrease_date = ""
    
    for row in csv_reader:
        date = row[0]
        value = float(row[column_index])

        if prev_value is not None:
            change = value - prev_value
            if change < max_decrease:
                max_decrease = change
                max_decrease_date = date

        prev_value = value

    if max_decrease_date:
        print("Greatest Decrease in Profits:", max_decrease_date, "($", max_decrease, ")")



