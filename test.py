import gspread
import pandas

cred_file = "river-surf-377412-6b78a4bb3246.json"
gc = gspread.service_account(cred_file)
print(gc)
database = gc.open("data")   #Establish the connection.
print(database)

worksheet = database.worksheet("Sheet1") #Selecting a worksheet
print(worksheet)

#list all the worksheets
list_wks = database.worksheets()
print(list_wks)

# database.add_worksheet("yash","100","30") #creating new sheet in Gsheet panel
print(database.url)
print(worksheet.get_all_records())

n = worksheet.col_values(2) # counting the row values and column values of entire Gsheet
print(len(n)) 

# update or add data in Gsheet 
# new_name = "Vaibhav Purohit"
# new_age = 23
# worksheet.update_cell(3,1,new_name)
# worksheet.update_cell(3,2,new_age)

worksheet.delete_row(5)
print("Data has been deleted!"),