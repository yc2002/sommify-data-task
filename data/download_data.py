import requests
import os

# Provide the URL of the Blob you want to download
blob_url = "https://sommify.blob.core.windows.net/sommify-task/titles.csv"
output_file_path = os.path.join(os.path.dirname(__file__), "titles.csv")

# Send a GET request to download the Blob
response = requests.get(blob_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the content of the response to a file
    with open(output_file_path, "wb") as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print("Failed to download the file. Status code:", response.status_code)
