

import psycopg2
frequency=[("1","YELLOW","5"),("2","BROWN","6"),("3","WHITE","16"),("4","BLUE","30"),
           ("5","BLACK","1"),("6","ORANGE","9"),("7","GREEN","10"),("8","PINK","5"),("9","RED","9"),
           ("10","ARSH","1"),("11","BLEW","1"),("12","CREAM","2")]


def InsertData(Data):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="12345",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="mydb3")
        cursor = connection.cursor()

        # print postgresSQL version
        print(connection.get_dsn_parameters(),"\n")

        # printing the postgreSQL version
        cursor.execute("SELECT version();")
        record=cursor.fetchone()
        print("you are connected to -",record,"\n")

        sql_insert_query = """ INSERT INTO  mydb3schema."Colour" (id, colour, frequency)
                           VALUES (%s,%s,%s) """

        # executemany() to insert multiple rows

        result = cursor.executemany(sql_insert_query,Data)
        connection.commit()
        count=cursor.rowcount
        print(cursor.rowcount, "Data inserted successfully into Colour table")

    except (Exception, psycopg2.Error) as error:
        print("Failed inserting Data into (Colour) table {}".format(error))
    # except (Exception, psycopg2.Error) as error:
    #     print("Error while connecting to postgreSQL".format(error))
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

Data = frequency
InsertData(Data)
