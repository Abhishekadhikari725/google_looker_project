# Ice-Cream Factory Data Integration Project

This project is designed to automate the process of extracting data from Google Sheets or CSV files and appending it to a dashboard built on Google Looker Studio. The integration is performed using a Google service account, operating within the owner's Google Drive folder.

## Key Features

- **Data Sources**: 
  - Google Sheets
  - CSV Files

- **Target**: 
  - Google Looker Studio Dashboard

- **Technologies Used**: 
  - Google Cloud Functions
  - Google Cloud Scheduler
  - Google Drive API
  - Google Sheets API

## Project Workflow

1. **Data Extraction**:
    - The program fetches data from either a Google Sheet or a CSV file stored in a specific folder in Google Drive.

2. **Data Processing**:
    - The data is processed and formatted as required for the Looker Studio dashboard.

3. **Data Upload**:
    - The processed data is appended to the Looker Studio dashboard.

4. **Automation**:
    - The entire workflow is automated using Google Cloud Scheduler to ensure that the data is updated at regular intervals.

## Folder Structure

- The program operates within a designated folder named `ice-cream factory` on Google Drive.
- All functions related to data extraction, processing, and uploading are executed within this folder.

## Google Cloud Integration

- **Service Account**: 
  - A Google service account is used to manage permissions and authenticate API requests.
  
- **Google Cloud Functions**:
  - Functions are deployed to handle data extraction, processing, and uploading.
  
- **Google Cloud Scheduler**:
  - Scheduled tasks ensure that the data in the dashboard is updated regularly.

## Deployment

- The project is deployed on Google Cloud Functions to leverage serverless computing and ensure scalability.

## Client-Specific Customizations

- This project is tailored for a specific client, ensuring that all their requirements are met.
- Customizations include folder locations, data formats, and specific update schedules.

## Benefits

- **Automation**: 
  - Eliminates the need for manual data updates.
  
- **Scalability**: 
  - Utilizes Google Cloud’s infrastructure for scalable and reliable performance.
  
- **Customization**: 
  - Tailored to meet the unique needs of the client.

## Getting Started

1. **Setup Google Cloud**:
    - Ensure Google Cloud Functions and Scheduler are enabled in your Google Cloud project.
    
2. **Service Account**:
    - Create and configure a service account with the necessary permissions.
    
3. **Folder Setup**:
    - Create the `ice-cream factory` folder in Google Drive and ensure it is accessible by the service account.
    
4. **Deployment**:
    - Deploy the Google Cloud Functions and set up the Google Cloud Scheduler to run the functions at desired intervals.

## Conclusion

This project streamlines the data integration process, ensuring that the Looker Studio dashboard is always up-to-date with the latest data from Google Sheets or CSV files. The use of Google Cloud services provides a robust and scalable solution tailored to the client’s needs.
