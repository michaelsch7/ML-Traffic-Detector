import requests
import time
import boto3

def printCollegeDrive():
    pics = 0
    s3_bucket = 'bucket' 
    s3_prefix = 'prefix'  

    s3 = boto3.client('s3')

    while True and pics < 3:
        
        url = "https://511la.org/map/Cctv/b24--1"
        response = requests.get(url)
        s3_key = f"{s3_prefix}{pics}_img_I10_collegeDr.jpg"
        print(f"Uploading {s3_key} to S3...")
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=response.content)
        pics += 1
        time.sleep(11)

if __name__ == "__main__":
    printCollegeDrive()

