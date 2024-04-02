from io import BytesIO
from read import READ
from append import APPEND
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from datetime import datetime 

def main():
    try:
        
        master_file_name = "master"  # Replace with the actual name of the master file
        drive_folder_name = "Icecream_Factory_Data"  # Replace with the name of the Google Drive folder
        credentials_file = "E:\Python\googel_looker_project\key.json"  # Replace with the path to your service account credentials JSON file
        sucess=[]
        date_of_creation_main= str


        # Connect to Google Drive using service account credentials
        creds = Credentials.from_service_account_file(credentials_file)
        drive_service = build('drive', 'v3', credentials=creds)
        # Connect to Google Drive using service account credentials
        READ.drive_service = build('drive', 'v3', credentials=creds) 
        # Replace 'file_path' with the path to your Python file


        try: 
            # Get the folder ID by searching for the folder
            folder_id = None
            response = drive_service.files().list(q=f"name='{drive_folder_name}' and mimeType='application/vnd.google-apps.folder'", fields="files(id)").execute()
            folders = response.get('files', [])
            if folders:
                folder_id = folders[0]['id']

            if not folder_id:
                print(f"Folder '{drive_folder_name}' not found in Google Drive.")
                return

            # List files in the folder
            response = drive_service.files().list(q=f"'{folder_id}' in parents and name='{master_file_name}'", fields="files(id, name, createdTime, modifiedTime, size)").execute()
            files = response.get('files', [])

            if not files:
                print(f"File '{master_file_name}' not found in '{drive_folder_name}' folder.")
                return
                
            # Get the file's metadata
            file_metadata = files[0]
            
            # Print or use the file's metadata as needed
            date_of_creation_main = file_metadata['modifiedTime']
            print(f"I am date of master modification in drive {date_of_creation_main}")
        except Exception as e:
            print("An error occurred while getting metadata :", str(e))
        
        with open("meta.txt", 'r') as file:
                master_date_previous=file.readline()
        master_date_previous= datetime.fromisoformat(master_date_previous.replace("Z", "+00:00"))



        # Get the ID of the Google Drive folder
        folder_id = None
        response = drive_service.files().list(q=f"name='{drive_folder_name}' and mimeType='application/vnd.google-apps.folder'", fields="files(id)").execute()
        folders = response.get('files', [])
        if folders:
            folder_id = folders[0]['id']

        if not folder_id:
            print(f"Folder '{drive_folder_name}' not found in Google Drive.")
            return

        # List files in the folder
        response = drive_service.files().list(q=f"'{folder_id}' in parents", fields="files(id, name, createdTime, modifiedTime)").execute()
        files = response.get('files', [])
        

        if not files:
            print(f"No files found in '{drive_folder_name}' folder.")
            return
        
        # Keep track of processed file names and date
        processed_files = set()

        # Iterate over the files in the folder
        for file in files:
            file_name = file['name']
            file_date_of_modified= file['modifiedTime']
            file_date = datetime.fromisoformat(file_date_of_modified.replace("Z", "+00:00"))
            if file_date>master_date_previous and file_name!= "master": # Process each file only once
                print(f"I am date of {file_name} modified {file_date}.")
                print(f"I am date of master modified previously {master_date_previous}")
                print(f"Reading {file_name}.")
                file_id = file['id']
                # Read the contents of the file
                request = drive_service.files().export_media(fileId=file_id, mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                file_data = request.execute()
               # Process the file data
                with BytesIO(file_data) as fh:
                    # Reading data from the new file
                    reader = READ(master_file_name, file_name,folder_id)
                    last_line = reader.last_row_master
                    # Appending records to the master file
                processed_files.add(file_name)
                sucess.append({True,file_name})
            else:
                sucess.append([False,file_name])
        files_name_updated=[]
        for result, file in sucess:
            if result:
                files_name_updated.append(file)
        if len(files_name_updated)>0:
            try:
                appender = APPEND(master_file_name, reader.records_master)
                if appender.result(last_line):
                    for file in files_name_updated:
                        if files_name_updated != "master":
                            print(f"Records from '{file}' appended to master file successfully.")
                    # Updating meta time in the file meta.txt
                    with open("meta.txt", 'w') as file:
                        current_utc_time=datetime.utcnow()
                        file.write(current_utc_time.strftime("%Y-%m-%dT%H:%M:%SZ"))
                        print(f"I am current time {current_utc_time}")
                else:
                    print(f"Error occurred while appending records from '{file_name}' to master file.")
            except Exception as e:
                print(f"An error occurred in filename {file_name}:",end="")
                if str(e)=="list index out of range":
                    print( " Once data has been already updated so aborted.")
                else:
                    print(str(e))   
        else:
            print("All files are upto date nothing to update in master-sheet.")         
                  
    except Exception as e:
        print("An error occurred:",end="")
        if str(e)=="list index out of range":
            print( " Once data has been already updated so aborted.")
        else:
            print(str(e))

if __name__ == "__main__":
    main()


