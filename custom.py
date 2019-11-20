import psycopg2


def print_func(par):
    print "Hello : ", par
    return


def row_print_func(params):
    print params
    return


def db_connect(user, password, host, port, database):

    connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)

    cursor = connection.cursor()
   
    return cursor
