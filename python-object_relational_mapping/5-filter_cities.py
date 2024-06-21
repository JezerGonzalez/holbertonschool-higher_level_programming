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
        querry = "SELECT cities.name FROM cities\
                JOIN states ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC"
        cursor.execute(querry, (sys.argv[4],))
        cities = cursor.fetchall()

        print(", ".join(city[0] for city in cities))

        cursor.close()
        connection.close()
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL or execuiting query: {e}")
