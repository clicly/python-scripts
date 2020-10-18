import openpyxl

# -------------------------
# VARIABLES
yearly_rate = 0.03
payment_begin = 170_000 # amount of money to be payed 
payment_rate = 1_500 # amount of money to be payed per month
years = 20 # limit you want to save
net_worth = 0 # your current savings
file_name = 'investment_calculation'
# -------------------------
# CONSTANTS
index_row = 1
months_of_the_year = 12
monthly_rate = yearly_rate / months_of_the_year
file_extension = '.xlsx'
file = file_name + file_extension
# -------------------------

def create_header():
    return ['Laufzeit (in Monaten)', 'Restkapital', 'Tilgung', 'Tilgung kumuliert','Zins', 'Zins kumuliert']

def create_mock_data():
    return [[1, 148000, 1.1, 375, 1.1, 375, 1], [1, 148000, 1.1, 375, 1.1, 375, 1]]

def create_data():
    global payment_begin
    global payment_rate
    global monthly_rate
    global years
    global months_of_the_year
    global net_worth

    data = []

    for month in range(1, years * months_of_the_year):
        if len(data) == 0:
            capital_remaining = payment_begin + (payment_begin * monthly_rate) - payment_rate - net_worth
            acquittance = payment_begin - capital_remaining
            acquittance_accumulated = acquittance
            payment_rate_local = payment_rate - acquittance
            payment_rate_local_accumulated = payment_rate_local

            data.append([month, capital_remaining, acquittance, acquittance_accumulated, payment_rate_local, payment_rate_local_accumulated])
        else:
            last_entry = data[len(data) - 1]

            capital_remaining = last_entry[1] + (last_entry[1] * monthly_rate) - payment_rate
            acquittance = last_entry[1] - capital_remaining
            acquittance_accumulated = acquittance + last_entry[3]
            payment_rate_local = payment_rate - acquittance
            payment_rate_local_accumulated = payment_rate_local + last_entry[5] 

            if (capital_remaining > 0):
                data.append([month, capital_remaining, acquittance, acquittance_accumulated, payment_rate_local, payment_rate_local_accumulated])
            else:
                data.append([str(month / months_of_the_year), ' YEARS'])
                break

    return data

def create_excel():
    global file
    
    # create new blank workbook
    workbook = openpyxl.Workbook()

    # get blank work sheet
    sheet = workbook['Sheet']
    
    data = []

    # fill with header
    data.append(create_header())
    # fill with data
    for entry in create_data():
        data.append(entry)
    # insert data to excel
    insert_excel(sheet, data)

    # save file from computers memory to hard drive
    workbook.save(file)

def insert_excel(sheet, data):
    global index_row

    # Write values to excel file
    for row in data:
        for ndx, column in enumerate(row):
            sheet.cell(row=index_row, column=ndx +1).value = column 
        index_row += 1

if __name__ == "__main__":

    print('Started calculation...')

    # Define example house calculation
    # TODO
    # (Optional) Import house calculation variables
    # TODO
    # Ask user for input for each variable
    # TODO
    # Validate variables
    # TODO
    # (Optional) Save variables for later usage
    # TODO
    # CHANGE SAVING RATE AFTER YEAR...
    # TODO

    # Create excel file
    create_excel()

    print('Finished calculation...')
