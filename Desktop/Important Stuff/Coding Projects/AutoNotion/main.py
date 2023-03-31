from __future__ import print_function
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tkinter import *
from tkinter import ttk

import NotionAPI
import os.path


# Information on the integration, databases and spreadsheet

database_id = '76b974da090a47439640a2845d4ba7fb'
token = 'secret_WwmU9iObdjb8JpPY2ma1XuZxDYB7EefddmftQmLdw95'

read_headers = {
    'Authorization': 'Bearer ' + token,
    'Notion-Version': '2022-06-28'
}

write_headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}


# Defining a class for the components

class Component:
    '''
    Represents a component in the component spreadsheet

    Atributes:
    - value: the value of the resistence or capacitance of the component
    - package: tha package in which the component comes
    - power: component's nominal rated power
    - tolerance: component's nominal rated tolerance
    - voltage: component's maximum voltage of operation
    - status: component's purchase status
    '''

    def __init__(self, value, package, power='', tolerance='', voltage=''):
        self.value = value
        self.package = package
        self.power = power
        self.tolerance = tolerance
        self.voltage = voltage
        self.status = 'Comprado'

        if 'R' in value:
            self.type = 'Resistor'
            self.location = 'Gaveta 1'

        elif 'F' in value:
            self.type= 'Capacitor'
            self.location = 'Gaveta 2'

        elif 'A' in self.value:
            self.type = 'Fusível'
            self.location = 'Gaveta 3'


    def insert(self, database_id, headers):
        '''
        Inserts a component into the targeted Notion database

        Parameters:
        - type: resistor or capacitor
        - location: where the component will be stored in the workshop
        - all the others are the class atributes
        '''

        NotionAPI.add_component(
            database_id, 
            headers, 
            self.type, 
            self.value,
            self.location, 
            self.power, 
            self.tolerance, 
            self.voltage, 
            self.package, 
            self.status
            )
        
        return None


# Google sheets API
# If modifying these scopes, delete the file token.json.

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.

SAMPLE_SPREADSHEET_ID = '1QZLgKDrMrbdaRkwFr51DyTt1aittmminl2t3RQspC4c'
SAMPLE_RANGE_NAME = 'Página1!A1:E'


def connect():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    global values
    creds = None

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in.

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        # for row in values:
        #     # Print columns A and E, which correspond to indices 0 and 4.
        #     print(row)

    except HttpError as err:
        print(err)


# Function that wil get called when the button is pressed on the user interface

def press_button():
    '''
    Function that gets called when the button is pressed on the user interface.
    Creates a component object for each row in the values list, then inserts them
    into the targeted Notion database. Takes no parameters and returns nothing.
    '''

    connect()

    for row in values:
        component = Component(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4]
        )

        component.insert(database_id, write_headers)

    return None


# Graphical user interface

root = Tk()
root.geometry("300x200")
root.resizable(False, False)

window = ttk.Frame(root, padding=10)

enter_dbId_label = ttk.Label(root, anchor=CENTER, font=("Helvetica", 10), 
                             text='Press submit to insert items into the database')                         
submit_button = ttk.Button(root, text='Submit', command=press_button)

enter_dbId_label.pack()
submit_button.pack()

root.mainloop()





