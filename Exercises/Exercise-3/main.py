import os
import gzip
import boto3

s3 = boto3.client('s3')
BUCKET_NAME = "commoncrawl"

current_folder = os.path.dirname(__file__)
download_folder = os.path.join(current_folder, "downloads")
gz_file_1 = os.path.join(download_folder, "wet.paths.gz")
extracted_file = os.path.join(download_folder, "wet.paths")

def main():
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    s3.download_file(BUCKET_NAME, 'crawl-data/CC-MAIN-2022-05/wet.paths.gz', gz_file_1)
    os.system(f"gzip -d {gz_file_1}")

    with open(extracted_file, "rt") as f:
        first_line = f.readline().strip()
        gz_file_2 = os.path.join(download_folder, os.path.basename(first_line))
        s3.download_file(BUCKET_NAME, first_line, gz_file_2)

    with gzip.open(gz_file_2, "rt") as f:
        for line in f:
            print(line.strip())

if __name__ == "__main__":
    main()