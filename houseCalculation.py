import openpyxl, os

# VARIABLES
yearly_rate = 0.03
payment_begin = 150_000 # amount of money to be payed in general
payment_rate = 1_500 # amount of money to be payed per month
years = 20 # limited years you want to save
net_worth = 60000 # your current savings
export_file_name = 'investment_calculation' # name of the exported file
output_directory = os.path.expanduser("~") + "/Downloads/" # directory of the exported file

# CONSTANTS
index_row = 1
months_of_the_year = 12
monthly_rate = yearly_rate / months_of_the_year
file_extension = '.xlsx'
file = export_file_name + file_extension

# -----------------------------------------------------------------

def create_doc_data(wb_row_header, wb_row_data):
    doc_data = []

    doc_data.append(wb_row_header)
    for row in wb_row_data:
        doc_data.append(row)

    return doc_data

def create_wb_header():
    return ['Laufzeit (in Monaten)', 'Restkapital', 'Tilgung', 'Tilgung kumuliert','Zins', 'Zins kumuliert']

def create_wb_data():
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

def get_mock_data():
    # NOTE: Mock data was only needed for testing purpose
    #       and will remain unused in the future
    return [[1, 148000, 1.1, 375, 1.1, 375, 1], [1, 148000, 1.1, 375, 1.1, 375, 1]]

def generate_excel_file():
    global file
    global output_directory
    
    workbook = openpyxl.Workbook()
    sheet = workbook['Sheet']

    wb_row_header = create_wb_header()
    wb_row_data = create_wb_data()
    wb_doc_data = create_doc_data(wb_row_header, wb_row_data)
    insert_into_excel_sheet(sheet, wb_doc_data)

    os.chdir(output_directory)
    workbook.save(file)

def insert_into_excel_sheet(sheet, data):
    global index_row

    for row in data:
        for ndx, column in enumerate(row):
            sheet.cell(row=index_row, column=ndx+1).value = column 
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

    generate_excel_file()

    print('Finished calculation...')
