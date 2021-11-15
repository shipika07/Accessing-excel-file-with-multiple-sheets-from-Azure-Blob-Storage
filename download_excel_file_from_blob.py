from azure.storage.blob import BlobServiceClient
import openpyxl
import os
import pandas as pd


def download_all_sheets(container_name, blob_name): 
    connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name) 
    blob_downloader = blob_client.download_blob()
    get_blob_data = pd.ExcelFile(blob_downloader , engine='openpyxl')
    all_sheets_data = pd.DataFrame()
    for sheet in get_blob_data.sheet_names:
    	file = pd.read_excel(get_blob_data , engine = 'openpyxl', sheet_name = sheet)
    	all_sheets_data = pd.concat([all_sheets_data , file], axis = 0)
    return all_sheets_data
