#so basically we created a s3 trigger to list the files in rds.
## in this we will be creating an API to get the data from the object.
## so we have created an GET-API with this lambdafunction and tested with // default/get-data?id=9

import boto3
import pymysql 
import json

s3_client = boto3.client('s3')

#db endpoint
rds_host  = <your mysql endpoint>
name = "admin"
password = "mysqlpassword"
db_name = <your db name>

def lambda_handler(event, content):
    result= []
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        select = ("""select * from BUCKET_OBJECTS where id= %s """)
        id = (event['id'])
        cur.execute(select,id)
        #conn.commit()
        #cur.close()
        #for row in cur:
        #    result.append(list(row))
        #print ("Data from RDS...")
        #print (result)
        result = cur.fetchall();
        print (result)
        bucket_rds = result [0]
        
    client = boto3.client('s3')    
    bucket_name = bucket_rds[1]
    #print("fav bucket: ",bucket_name)
    bucket_object = bucket_rds[2]
    file_object = client.get_object(Bucket=bucket_name, Key=bucket_object)
    file_content = file_object['Body'].read().decode('utf-8')
    return {
        'statusCode': 200,
        'body': json.dumps('file content data from S3 bucket: {}'.format(file_content))
    }
        
        
     
    # TODO: write code...
