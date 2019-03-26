import csv
import xlrd


def get_excel_data(file_name):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    book = xlrd.open_workbook(file_name)
    # get the frist sheet
    sheet = book.sheet_by_index(0)
    # iterate through the sheet and get data from rows in list
    for row_idx in range(1, sheet.nrows):  #iterate 1 to maxrows
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    return rows

def get_csv_data(file_name):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    data_file = open(file_name, "r")
    # create a CSV Reader from CSV file
    reader = csv.reader(data_file)
    # skip the headers
    next(reader, None)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows