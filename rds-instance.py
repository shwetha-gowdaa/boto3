import boto3

rds_client = boto3.client('rds', region_name='ap-south-1')

try:
    response = rds_client.create_db_instance(
        DBInstanceIdentifier='mydbinstance',
        DBInstanceClass='db.m5.large',
        Engine='mysql',
        EngineVersion='8.0.39',
        MasterUsername='admin',
        MasterUserPassword='Password123!',
        DBName='mydatabase',
        AllocatedStorage=20,
        PubliclyAccessible=False,
        MultiAZ=False,
        StorageType='gp2',
        BackupRetentionPeriod=7,

    )

    print("RDS instance creation initiated:")
    print(response)

except Exception as e:
    print(f"An error occurred: {e}")
