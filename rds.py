import boto3

def create_rds_instance():
    # Define RDS parameters
    rds_client = boto3.client('rds')
    db_instance_identifier = 'exlservice'
    db_name = 'lucky'
    db_instance_class = 'db.t2.micro'  # Choose an appropriate instance class
    engine = 'postgres'  # Specify the database engine
    master_username = 'lucky1225'
    master_password = 'roZes@123'
    allocated_storage = 30  # Specify the storage size in GB
    availability_zone = 'us-west-21'  # Specify the preferred availability zone
    backup_retention_period = 7  # Specify the backup retention period in days
    preferred_backup_window = '01:00-02:00'  # Specify the preferred backup window
    port = 5432  # Specify the port number
    multi_az = True  # Enable Multi-AZ deployment
    publicly_accessible = False  # Set to True if you want the instance to be publicly accessible

    # Create RDS instance
    response = rds_client.create_db_instance(
        DBName=db_name,
        DBInstanceIdentifier=db_instance_identifier,
        AllocatedStorage=allocated_storage,
        DBInstanceClass=db_instance_class,
        Engine=engine,
        MasterUsername=master_username,
        MasterUserPassword=master_password,
        AvailabilityZone=availability_zone,
        BackupRetentionPeriod=backup_retention_period,
        PreferredBackupWindow=preferred_backup_window,
        Port=port,
        MultiAZ=multi_az,
        PubliclyAccessible=publicly_accessible
    )

    # Print response
    print(response)

# Call the function to create the RDS instance
create_rds_instance()
