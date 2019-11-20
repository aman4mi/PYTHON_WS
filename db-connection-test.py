import psycopg2

try:
    connection = psycopg2.connect(user="enterprisedb",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5444",
                                  database="springbootdb")

    cursor = connection.cursor()

    sql="""SELECT id, course_id, course_title, created_by, created_on, dept_name, semester_info, student_id, student_name
	FROM public.student_info;"""
  
    cursor.execute(sql)
    rows = cursor.fetchall()
  #  for id, course_id, course_title, created_by, created_on, dept_name, semester_info, student_id, student_name in rows:
        #print "id=",row[0], "course_id=",row[1],"course_title=", row[2], "created_by=",row[3], "created_on=",row[4],"dept_name=", row[5], "semester_info=",row[6], "student_id=",row[7], "student_name=",row[8]

    print "id,  course_id,  course_title,  created_by,   created_on,  dept_name,  semester_info,  student_id,  student_name"
    for row in rows:
        r1=row[1]
        r2=row[2]
        r3=row[3]
        r4=row[4]
        r5=row[5]
        r6=row[6]
        r7=row[7]
        r8=row[8]
        if r1=='':
            r1="\t"
        if r2=='':
            r2="\t"
        if r3=='':
            r3="\t\t"
        if r4=='':
            r4="\t\t"
        if r5=='':
            r5="\t\t\t"
        if r6=='':
            r6="\t\t\t"
        if r7=='':
            r7="\t\t\t"
        if r8=='':
            r8="\t\t\t"

        print row[0], r1, r2, r3, r4, r5, r6, r7, r8
       
except (Exception, psycopg2.Error) as error:
    print ("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")