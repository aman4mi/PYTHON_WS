import psycopg2
import custom as c
try:
    cur = c.db_connect(user="enterprisedb",
                       password="postgres",
                       host="127.0.0.1",
                       port="5444",
                       database="springbootdb")

    sql = """SELECT * FROM public.student_info;"""

    cur.execute(sql)
    rows = cur.fetchall()

    for row in rows:

        print('fields', [desc[0] for desc in cur.description])
        print('data', rows)

except (Exception, psycopg2.Error) as error:
    print ("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
