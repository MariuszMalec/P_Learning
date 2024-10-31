#pip install psycopg2-binary
#w visual studio code start : python3 ConnectToPGSql.py

import psycopg2

def connect():
    """ Try Connect to the PostgreSQL database server """
    conn = None
    try:

        databasename = "MainAppTrackingsDb"

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...' + str(databasename))

        conn = psycopg2.connect(
            database=databasename, user='postgres', password='mario13', host='127.0.0.1', port='5432'
        )

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database trainers:')
        cur.execute('SELECT * FROM public."Trainers"')

        # display the PostgreSQL database
        #print("Result ", cur.fetchall())

        for item in cur.fetchall():
            print(item)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()