## Summary

In this project, I used Google Cloud service account credentials.

## How to get the `service account credentials` file

1. Open the GCP Console
2. Activate the Google Sheets API
3. Open the Credentials page for the Google Sheets API
4. Create a new service account
5. Open the service account
6. Create a new private-pair-key (JSON)
7. Download the file and place it in the project root named `gsheets_creds.json`

## Allow spreadsheet access

1. Search for "Service Accounts" in the GCP search bar and open it
2. Copy the service account email
3. Open the spreadsheet you want and share it with the service account email (Editor access required)

## Get your google sheets spreadsheet ID

1. Access your spreadsheet.
2. Copy the link 

The link should be something like: "https://docs.google.com/spreadsheets/d/<ID>/edit?gid=0#gid=0". Copy the ID part of the link and place it in .env file.