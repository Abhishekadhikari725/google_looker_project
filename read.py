import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

class READ:
    records_master = []
    checker_list = []
    master_list =[]
    scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = Credentials.from_service_account_file("E:\Python\googel_looker_project\key.json", scopes=scope)

    def __init__(self, master_file, new_file,current_folder_id) -> None:
        self.master_file = master_file
        self.new_file = new_file
        self.last_row_master = None
        self.current_folder_id=current_folder_id
        self.master()
        self.new()

    def master(self):
        file = gspread.authorize(READ.creds)
        workbook = file.open(self.master_file)  # Use self.master_file
        sheet = workbook.sheet1
        self.last_row_master = len(sheet.col_values(1))
        data_range = f'A1:AI{self.last_row_master}'
        data = sheet.get(data_range)
        for row in data:
            READ.master_list.append(row)  
        READ.checker_list.append(self.master_list[-1])
        return None

    def new(self):
        file = gspread.authorize(READ.creds)
        workbook = file.open(self.new_file)  # Use self.new_file
        sheet = workbook.sheet1
        last_row = len(sheet.col_values(1))
        data_range = f'A2:AI{last_row}'
        data = sheet.get(data_range)
        for row in data:
            if row not in READ.master_list:
                if row not in READ.records_master:  # Check if the row content is not in master_list
                    READ.records_master.append(row)
         
    
    
