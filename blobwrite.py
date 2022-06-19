import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Quick start code goes here
    connect_str = "DefaultEndpointsProtocol=https;AccountName=storageborleanovidiu;AccountKey=LJOfwMFNBhUc949vVfM2k/utJIyS/E8tHaN+F5ro/9xzM3fnKrRUs53TCzbmY7S52DDz3HcEvh4BHu8H/Nuacw==;EndpointSuffix=core.windows.net"
    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create a unique name for the container
    container_name = "ovidiuborleandumitrucont"

    # Create the container
    container_client = blob_service_client.create_container(container_name)



except Exception as ex:
    print('Exception:')
    print(ex)

