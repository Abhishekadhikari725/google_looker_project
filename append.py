import gspread
from oauth2client.service_account import ServiceAccountCredentials
from read import READ

class APPEND:
    def __init__(self, master_file, new_records) -> None:
        self.master_file = master_file
        self.new_records = new_records
        self.append_to_master(master_file, new_records)
    
    @staticmethod
    def append_to_master(master_file, new_records):
        scope = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name("E:\\Python\\googel_looker_project\\key.json", scopes=scope)
        file = gspread.authorize(creds)
        workbook = file.open(master_file)
        sheet = workbook.sheet1

        # Get the last row in the master sheet
        last_row = len(sheet.col_values(1))
        check_if_todo = READ.checker_list[0]

        if check_if_todo != new_records[-1]:
            # Prepare the range to update
            update_range = f'A{last_row + 1}:AI{last_row + len(new_records)}'

            # Prepare the values to update
            values = new_records

            # Update the range with the new values
            sheet.update(update_range, values)

            print("Data is updated now in master sheet.")
        else:
            print("Data is already updated in master sheet.")
    
    def result(self, last_line):
        if len(self.new_records) == last_line:
            return False
        return True


