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

        cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                       ORDER BY id ASC")

        states = cursor.fetchall()
        for state in states:
            print(state)

        cursor.close()
        connection.close()
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL or execuiting query: {e}")
