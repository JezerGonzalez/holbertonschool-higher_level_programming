#!/usr/bin/python3
"""Lists all states in database"""
import MySQLdb
import sys


if __name__ == "__main__":
    try:
        connection = MySQLdb.connect(host='localhost',
                                     port=3306,
                                     user=sys.argv[1],
                                     password=sys.argv[2],
                                     db=sys.argv[3])

        cursor = connection.cursor()
        querry = "SELECT * FROM states WHERE name = BINARY '{}'\
                  ORDER BY id ASC".format(sys.argv[4])
        cursor.execute(querry)

        states = cursor.fetchall()
        for state in states:
            print(state)

        cursor.close()
        connection.close()
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL or execuiting query: {e}")
