import pymysql

import sys



REGION = 'us-east-1a'



rds_host  = "mydatabase.cpuko4ntuuir.us-east-1.rds.amazonaws.com"

name = "admin"

password = "admin1234"

db_name = "S3BUCKETS"



def save_events(event):

    """

    This function fetches content from mysql RDS instance

    """

    result = []

    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)

    with conn.cursor() as cur:

        ##cur.execute("""insert into  BUCKET_OBJECTS (ID ,bname, fname) values( %s, '%s' '%s')""" % (event['id'],event['bname'], event['fname']))

        #sql = (""" INSERT INTO `BUCKET_OBJECTS` (`id`, `bname`, `fname`) VALUES (%s,%s,%s)""")

        #val = (event['id'],event['bname'], event['fname'])

        x = "null"

        y = "Sample-bucket"

        z = "sample-filename"

        val = ( x,y,z)

        #cur.execute(sql,val)

        

        select = ("""select * from BUCKET_OBJECTS where id= %s """)

        where = (event['id'])

        cur.execute(select,where)

        conn.commit()

        cur.close()

        for row in cur:

            result.append(list(row))

        print ("Data from RDS...")

        print (result)

        return(result)

        

def main(event, context):

    save_events(event)

        





# event = {

#   "id": 777,

#   "name": "appychip"

# }

# context = ""

# main(event, context)


