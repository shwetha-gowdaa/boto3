import boto3

# Initialize the S3 client
client = boto3.client('s3')

# Create the bucket
try:
    response = client.create_bucket(
        Bucket='botobucket212',  # Replace with your unique bucket name
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1',  # Set your desired region
        },
    )
    print("Bucket created successfully:", response)
except Exception as e:
    print("Error:", e)
