# Import the boto3 library
import boto3


# Instantiate a boto3 resource for S3 and name your bucket
s3 =boto3.resource("S3")
bucket_name='dct-crud1'
# Check if bucket exists
all_my_buckets=bucket_name
# Create the bucket if it does NOT exist

# Create 'file_1' and 'file_2'

# UPLOAD 'file_1' to the new bucket


# READ and print the file from the bucket

# UPDATE 'file_1' in the bucket with new content from 'file_2'


# DELETE the file from the bucket


# DELETE the bucket (the bucket should be empty.)
