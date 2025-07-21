import os
import requests

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

current_folder = os.path.dirname(__file__)
download_folder = os.path.join(current_folder, "downloads")

def main():
    if not os.path.exists(download_folder):
       os.makedirs(download_folder)

    for url in download_uris:
        try:
            response = requests.get(url)
            print(response.raise_for_status())
            file_name = os.path.basename(url)
            file_path = os.path.join(download_folder, file_name)

            with open(file_path, "wb") as f:
                f.write(response.content)
            os.system(f"unzip -qq {file_path} -d {download_folder}")
            print(f"Successfully download and extract file {file_name}")
            os.system(f"rm -rf {file_path}")
            print(f"Deleted file {file_name}")

        except Exception as e:
            print(f"Error: {e}")
        

if __name__ == "__main__":
    main()
