# Accessing-excel-file-with-multiple-sheets-from-Azure-Blob-Storage
This repository contains the piece of code of how to download the data from an excel file with multiple sheets stored on `Azure Blob Storage`.


In today's blog I will be covering how we can download an excel file with multiple sheets from `Azure Blob storage`.

Accessing such a file on Azure platform  is very easy but what if we want to download this file in our local system or to any other storage? We can achieve this using any programming language but here I'll be specific to python. Python provides specific library to access Azure services using code like `azure.storage.blob`. 

To access an excel file with multiple sheets there is a specific code but this does not work with the file which is stored in the Azure Blob storage. Azure Blob storage stores the file in an object format means when we try to access the file it will give us its object and using which we can access its data.

In this blog I will be covering the following points:

1. A brief introduction to Azure Blob Storage

2. Accessing an excel sheet using python.

**1. A brief introduction to Azure Blob Storage**

Azure is a cloud platform which provides many cloud computing services to the user. One of those services is `Azure Blob Storage`.

The Azure cloud platform is more than 200 products and cloud services designed to help you bring new solutions to life - to solve today's challenges and create the future. Build, run and manage applications across multiple clouds, on-premises and at the edge, with the tools and frameworks of your choice. [1]

`Azure Blob Storage` [2] is a storage service which stores a huge amount of data with high efficiency and security. All the background tasks like security, scalability, management, etc. will be handled by Azure Blob storage.

We can store any kind of data in a blob including text file, image, audio, etc. These files are stored in blob pattern means Blob storage has specific blob size. In case of big files, a file will be stored in multiple blobs, but this detail is hidden from the user. For a user this file seems to be a single file only (not multiple blobs). To access a big file fast, a file is stored in multiple blobs so with the help of parallel computing our goal can be achieved. To get more insights of Blob storage follow this link [3].

**2. Accessing an excel sheet using python**

The code to download access excel file from a blob storage using python is given in the file download_excel_file_from_blob.py:

The `BlobServiceClient` function is used to create a client for the Blob service. This client is basically an object to access your blob storage. Using this client you can perform different operations on Blob. To create a client for a specific blob we need `connection_string` . This string contains the access key of a specific Blob storage account.

Once a `BlobServiceClient` is initialized then we can provide the name of a container where our blob is placed and followed by the blob name where our file is stored.

![Capture](https://user-images.githubusercontent.com/37960364/141776835-1e81165b-4ce0-4931-a8d2-cf99d7915ff4.PNG)

So we must have the name of our respective container and blob. After getting access to a specific blob storage we can now access our file. If the mentioned blob/container is not already present then azure itself creates a new blob/container on the given name.

Now comes the main part, `download_blob`. This module is used to download the data from the given blob. In our case the data is in an excel file with multiple sheets. This `download_blob` module will not actually download the excel sheet to your storage instead it will get the object of that file. This object further is used to read the data as an excel file.

` get_blob_data = pd.ExcelFile(blob_downloader , engine='openpyxl')`

In the above line of code `get_blob_data` will create a pointer for the given file. `get_blob_data` will not contain the data of the file. It contains all the required information including all the sheet names. So now to access the data of a particular sheet we have to read the excel file with the specific sheet name.

We have listed all the sheet names of the given excel file by using `get_blob_data.sheet_names`.

To see the data all together of all the sheets I have stored the data in a data frame using the concat function of pandas library.

`all_sheets_data = pd.concat([all_sheets_data , file], axis = 0)`

Now `all_sheets_data` will hold the complete data from all the excel sheets.

An excel sheet is limited to 100000 rows so to store more data we can store data in multiple sheets and then use it. 

**3. Summary**

In this blog I have explained how we can download the data stored in multiple sheets of an excel file stored on a Azure blob storage account.

**4. References**

[1] https://azure.microsoft.com/en-in/overview/what-is-azure/

[2]https://azure.microsoft.com/en-in/services/storage/blobs/?OCID=AID2200195_SEM_2695a37940b5192cb7f6c2f20e1efae1:G:s&ef_id=2695a37940b5192cb7f6c2f20e1efae1:G:s&msclkid=2695a37940b5192cb7f6c2f20e1efae1

[3] Quickstart: Azure Blob Storage library v12 - Python | Microsoft Docs
